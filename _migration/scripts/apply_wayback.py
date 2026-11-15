"""Phase 4 follow-up: point dead links that have a Wayback copy at the snapshot (approved by Chris 2026-11-15).

usage: python3 -I _migration/scripts/apply_wayback.py   (run from the repo root)

Only link targets change (`](url)`, `](url "title")`, `href="url"`); link text is kept.
Also fixes the malformed `http://http//` links. Appends to _migration/link-rewrites.tsv.
Re-runnable: replaced URLs no longer match.
"""
import csv, html, re

def targets(url):
    # the URL as it may appear in a link target: raw or HTML-escaped
    return {url, html.escape(url, quote=False)}

def replace(text, old, new):
    n = 0
    for o in targets(old):
        pat = re.compile(r'(\]\(|href=")' + re.escape(o) + r'(?=[)"\s])')
        text, k = pat.subn(lambda m: m.group(1) + new, text)
        n += k
    return text, n

log, missing = [], []
rows = [r for r in csv.DictReader(open("_migration/dead-links.tsv"), delimiter="\t")
        if r["status"].startswith("dead") and r["wayback_url"]]
for r in rows:
    path = f"content/posts/{r['post']}.md"
    text = open(path).read()
    text, n = replace(text, r["url"], r["wayback_url"])
    if n:
        open(path, "w").write(text)
        log.append([r["post"], "wayback", r["url"], r["wayback_url"]])
    else:
        missing.append(r)

post = "content/posts/2012-03-24-some-twitter-infographics.md"
text = open(post).read()
for old in sorted(set(re.findall(r"http://http//[^)\s\"]+", text))):
    new = "http://" + old[len("http://http//"):]
    text, n = replace(text, old, new)
    assert n, old
    log.append(["2012-03-24-some-twitter-infographics", "typo", old, new])
open(post, "w").write(text)

with open("_migration/link-rewrites.tsv", "a") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(log)
print(f"rewrote {len(log)} links; {len(missing)} wayback rows not found in posts")
for r in missing:
    print("  not found:", r["post"], r["url"])
