"""Phase 4C: save non-Blogger images (other-images.tsv) locally.

usage: python3 -I _migration/scripts/fetch_other_images.py   (run from the repo root)

Order per image: Chris's local Dropbox copy (dl.dropbox /u/ links), the live URL, then the Wayback
snapshot nearest the post date (original bytes via the id_ URL). Imgur is skipped live: from the UK it
serves a "not viewable in your region" placeholder with a 200. Writes _migration/other-image-map.tsv.
Re-runnable: existing files are kept.
"""
import csv, json, os, shutil, time, urllib.parse, urllib.request

DROPBOX = os.path.expanduser("~/workspace/dropbox-Public")
NOT_IMAGES = ("commons.wikimedia.org/wiki/", "github.com/oatzy/")  # links to pages, not image files
MAGIC = (b"\x89PNG", b"\xff\xd8\xff", b"GIF8")
# dead originals whose only archived copy is a resized version of the same image (found via the CDX index)
ALTERNATES = {"http://www.sophos.com/images/blogs/gc/2010/09/onmouseover-popup.jpg":
              "http://www.sophos.com/images/blogs/gc/2010/09/onmouseover-popup-470.jpg"}
UA = {"User-Agent": "Mozilla/5.0 (blog image archiver)"}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return r.read()


def image(data):
    return data if data and data.startswith(MAGIC) else None


def wayback(url, date):
    q = urllib.parse.urlencode({"url": url, "timestamp": date})
    snap = json.loads(get(f"https://archive.org/wayback/available?{q}")).get("archived_snapshots", {}).get("closest")
    if not snap or not snap.get("available"):
        # the API misses captures that are only redirects (e.g. localhostr -> hostr.co); let Wayback follow them
        try:
            return image(get(f"https://web.archive.org/web/{date}id_/{url}")), f"{date} (via redirect)"
        except Exception:
            return None, None
    ts = snap["timestamp"]
    return image(get(f"https://web.archive.org/web/{ts}id_/{url}")), ts


def fetch(url, date):
    if "/u/4635169/" in url:
        p = os.path.join(DROPBOX, urllib.parse.unquote(url.split("/u/4635169/", 1)[1]))
        if os.path.exists(p):
            return open(p, "rb").read(), "dropbox-local"
    if "imgur.com" not in url:
        try:
            if d := image(get(url)):
                return d, "live"
        except Exception:
            pass
    try:
        d, ts = wayback(url, date)
        if d:
            return d, f"wayback {ts}"
    except Exception as e:
        return None, f"wayback error: {e}"
    return None, "unrecoverable"


def main():
    rows = list(csv.DictReader(open("_migration/other-images.tsv"), delimiter="\t"))
    out = []
    try:  # keep provenance of files saved by earlier runs
        prev = {r["old_url"]: r["status"] for r in csv.DictReader(open("_migration/other-image-map.tsv"), delimiter="\t")}
    except FileNotFoundError:
        prev = {}
    for r in rows:
        post, url = os.path.splitext(r["post"])[0], r["url"]
        if any(s in url for s in NOT_IMAGES):
            out.append((post, url, "", "skipped: not an image file"))
            continue
        slug = post[11:]
        src = ALTERNATES.get(url, url)
        name = os.path.basename(urllib.parse.urlparse(src).path)
        dest = f"static/images/{slug}/{name}"
        if os.path.exists(dest):
            out.append((post, url, dest[6:], prev.get(url, "ok (existing)")))
            continue
        data, how = fetch(src, post[:10].replace("-", ""))
        if data and src != url:
            how += " (resized version of the same image)"
        if data:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            open(dest, "wb").write(data)
            out.append((post, url, dest[6:], f"ok {how}"))
        else:
            out.append((post, url, "", how))
        time.sleep(1)
    with open("_migration/other-image-map.tsv", "w") as f:
        f.write("post\told_url\tlocal_path\tstatus\n")
        for o in out:
            f.write("\t".join(o) + "\n")
    for o in out:
        print(*o, sep="\t")


if __name__ == "__main__":
    assert image(b"\x89PNG....") and not image(b"<html>")
    main()
