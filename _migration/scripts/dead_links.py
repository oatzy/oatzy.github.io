"""Phase 4D: turn a lychee JSON report into _migration/dead-links.tsv (report only, nothing applied).

usage: python3 -I _migration/scripts/dead_links.py LYCHEE_JSON   (run from the repo root)

lychee was run on the built post pages (see phase4-notes.md). Here: drop root-relative noise, re-check
soft failures once with a browser UA, classify, and look up the Wayback snapshot nearest each post's date
for links that are dead. Social sites that block bots or need a login are 'unverifiable' whatever status
they returned (twitter/x answer 200 even for deleted tweets).
"""
import csv, glob, json, os, sys, time, urllib.error, urllib.parse, urllib.request

SOCIAL = ("twitter.com", "x.com", "t.co", "facebook.com", "fb.me", "linkedin.com", "instagram.com",
          "plus.google.com", "myspace.com", "foursquare.com", "letterboxd.com", "trakt.tv", "runkeeper.com")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"}
POSTS = {os.path.basename(p)[11:-3]: os.path.basename(p)[:-3] for p in glob.glob("content/posts/*.md")}


def social(url):
    h = (urllib.parse.urlparse(url).hostname or "").lower()
    return any(h == s or h.endswith("." + s) for s in SOCIAL)


def recheck(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
            return str(r.status)
    except urllib.error.HTTPError as e:
        return str(e.code)
    except Exception as e:
        return f"error: {type(e).__name__}"


def wayback(url, date):
    q = urllib.parse.urlencode({"url": url, "timestamp": date})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(f"https://archive.org/wayback/available?{q}", timeout=60) as r:
                snap = json.load(r).get("archived_snapshots", {}).get("closest")
            return snap["url"].replace("http://web.archive.org", "https://web.archive.org") if snap and snap.get("available") and snap.get("status", "200").startswith(("2", "3")) else ""
        except Exception:
            time.sleep(5)
    return "lookup failed"


def main(path):
    d = json.load(open(path))
    found = {}  # (post, url) -> status
    for m in ("error_map", "timeout_map", "success_map"):
        for f, es in d.get(m, {}).items():
            post = POSTS.get(os.path.basename(f)[:-5])
            for e in es:
                u = e["url"]
                if not u.startswith("http") or not post:
                    continue
                if m == "success_map" and not social(u):
                    continue
                s = e["status"]
                found[(post, u)] = "200" if m == "success_map" else str(s.get("code") or s.get("text") or "")[:60]
    checked, rows = {}, []
    rewritten = {r["old"] for r in csv.DictReader(open("_migration/link-rewrites.tsv"), delimiter="\t")}
    for (post, u), status in sorted(found.items()):
        if u in rewritten:  # already replaced by rewrite_links.py since lychee ran
            continue
        if social(u):
            rows.append((post, u, f"unverifiable ({status})", ""))
            continue
        if status not in ("404", "410"):  # soft failure: one more try before calling it
            if u not in checked:
                checked[u] = recheck(u)
                time.sleep(0.5)
            status = f"{status} / recheck {checked[u]}"
            if checked[u][0] in "23":
                continue
        code = status.split("recheck ")[-1]
        if code in ("401", "403", "429", "999"):
            rows.append((post, u, f"unverifiable ({status})", ""))
        else:
            rows.append((post, u, f"dead ({status})", None))
    cache = {}
    for i, r in enumerate(rows):
        if r[3] is None:
            key = (r[1], r[0][:10])
            if key not in cache:
                cache[key] = wayback(r[1], r[0][:10].replace("-", ""))
                time.sleep(1)
            rows[i] = r[:3] + (cache[key],)
    with open("_migration/dead-links.tsv", "w") as f:
        f.write("post\turl\tstatus\twayback_url\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    dead = [r for r in rows if r[2].startswith("dead")]
    print(f"rows {len(rows)}: dead {len(dead)} ({sum(1 for r in dead if r[3].startswith('http'))} with wayback), "
          f"unverifiable {len(rows) - len(dead)}")


if __name__ == "__main__":
    assert social("https://mobile.twitter.com/x") and not social("https://notx.com/")
    main(sys.argv[1])
