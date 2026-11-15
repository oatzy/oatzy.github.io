"""Phase 4: rewrite links in posts (URLs only, wording untouched). Run from the repo root.

usage: python3 -I _migration/scripts/rewrite_links.py

A. oatzy.blogspot post links -> https://oatzy.github.io/<path> via each post's blogger_orig_url.
B. Dropbox links -> files copied from ~/workspace/dropbox-Public into ~/workspace/question-nobody-asked/<slug>/
   (GitHub blob/tree URLs); runnable HTML pages + their js/css go to static/files/<slug>/; images to
   static/images/<slug>/ (already saved by fetch_other_images.py).
C. Non-Blogger images -> local copies listed in _migration/other-image-map.tsv.
Logs every replacement to _migration/link-rewrites.tsv. Re-runnable: replaced URLs no longer match.
"""
import csv, glob, os, re, shutil, urllib.parse

HOME = os.path.expanduser("~/workspace")
DROPBOX = f"{HOME}/dropbox-Public"
QNA = f"{HOME}/question-nobody-asked"
QNA_URL = "https://github.com/oatzy/question-nobody-asked"
SITE = "https://oatzy.github.io"
BLOGSPOT = re.compile(r"https?://(?:www\.)?oatzy\.blogspot\.[a-z.]+(/\d{4}/\d{2}/[^\s)\"'<>\]#?]+\.html)(?:\?m=1)?")
PAGE_DEPS = re.compile(r'(?:src|href)="([^":]+)"', re.I)  # relative resources an HTML page loads

posts = {}  # name (no ext) -> dict(path, text, slug, url, title)
for p in sorted(glob.glob("content/posts/*.md")):
    name = os.path.basename(p)[:-3]
    text = open(p).read()
    fm = text.split("\n---", 1)[0]
    date = re.search(r"^date: '?(\d{4})-(\d{2})-(\d{2})", fm, re.M).groups()
    orig = re.search(r"^blogger_orig_url: (\S+)", fm, re.M)
    title = re.search(r"^title: (.*)$", fm, re.M).group(1).strip().strip("'\"")
    slug = name[11:]
    posts[name] = dict(path=p, text=text, slug=slug, title=title,
                       url=f"{SITE}/{'/'.join(date)}/{slug}.html",
                       orig=urllib.parse.urlparse(orig.group(1)).path if orig else None)

baseline = set(open("_migration/baseline/urls.txt").read().split())
by_orig = {v["orig"]: v["url"] for v in posts.values() if v["orig"]}
assert all(u[len(SITE):] in baseline for u in by_orig.values()), "post URL not in baseline"

log, unmatched, missing = [], [], []


def split_fm(t):
    """(front matter, body): only the body is rewritten; front matter keeps blogger_orig_url etc."""
    i = t.index("\n---", 3) + 4
    return t[:i], t[i:]


def replace(name, old, new, kind):
    fm, body = split_fm(posts[name]["text"])
    if old not in body:
        missing.append((name, old))
        return
    posts[name]["text"] = fm + body.replace(old, new)
    log.append((name, kind, old, new))


# A. blogspot posts
for name, v in posts.items():
    for m in sorted({m.group(0) for m in BLOGSPOT.finditer(split_fm(v["text"])[1])}):
        new = by_orig.get(BLOGSPOT.match(m).group(1))
        if new:
            replace(name, m, new, "blogspot")
        else:
            unmatched.append((name, m))


def copy(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)


# B. Dropbox
images = {r["old_url"]: r["local_path"] for r in csv.DictReader(open("_migration/other-image-map.tsv"), delimiter="\t")
          if r["local_path"]}
readme_posts = set()
for r in csv.DictReader(open("_migration/dropbox-map.tsv"), delimiter="\t"):
    name, old, f = r["post"].rsplit(".", 1)[0], r["old_url"], r["dropbox_file"]
    slug = posts[name]["slug"]
    if old in images:  # images: local copy already saved
        new = images[old]
    elif f.endswith(".htm"):  # runnable page: serve from the blog with the files it loads
        src_dir, page = os.path.split(f)
        for dep in [page] + PAGE_DEPS.findall(open(f"{DROPBOX}/{f}").read()):
            copy(f"{DROPBOX}/{src_dir}/{dep}", f"static/files/{slug}/{dep}")
        new = f"/files/{slug}/{page}"
    elif f.endswith("/"):  # folder share
        folder = os.path.basename(f.rstrip("/"))
        shutil.copytree(f"{DROPBOX}/{f}", f"{QNA}/{slug}/{folder}", dirs_exist_ok=True)
        new = f"{QNA_URL}/tree/main/{slug}/{urllib.parse.quote(folder)}"
        readme_posts.add(name)
    else:
        # android-wear files sit beside the folder share they also belong to
        rel = f if f.startswith("android-wear/") else os.path.basename(f)
        copy(f"{DROPBOX}/{f}", f"{QNA}/{slug}/{rel}")
        new = f"{QNA_URL}/blob/main/{slug}/{urllib.parse.quote(rel)}"
        readme_posts.add(name)
    replace(name, old, new, "dropbox")

for name in readme_posts:
    v = posts[name]
    open(f"{QNA}/{v['slug']}/README.md", "w").write(f"Files for the blog post [{v['title']}]({v['url']}).\n")

# C. other images (the Dropbox ones were done in B)
for r in csv.DictReader(open("_migration/other-image-map.tsv"), delimiter="\t"):
    if r["local_path"] and "dropbox" not in r["old_url"]:
        replace(r["post"], r["old_url"], r["local_path"], "image")

for v in posts.values():
    open(v["path"], "w").write(v["text"])

new_log = not os.path.exists("_migration/link-rewrites.tsv")
with open("_migration/link-rewrites.tsv", "a") as f:
    if new_log:
        f.write("post\tkind\told\tnew\n")
    for row in log:
        f.write("\t".join(row) + "\n")
print(f"rewrote {len(log)} links:", {k: sum(1 for r in log if r[1] == k) for k in ("blogspot", "dropbox", "image")})
for name, old in unmatched:
    print("UNMATCHED blogspot", name, old)
for name, old in missing:
    print("NOT FOUND in post", name, old)
