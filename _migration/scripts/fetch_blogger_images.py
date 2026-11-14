#!/usr/bin/env python3
"""Phase 1: download Blogger-hosted images to static/images/<slug>/ and write the old->new map.

Re-runnable: files already on disk are not re-downloaded.
Run from the repo root: python3 -I _migration/scripts/fetch_blogger_images.py
"""
import collections
import pathlib
import re
import time
import urllib.parse
import urllib.request

POSTS = pathlib.Path("_posts")
OUT = pathlib.Path("static/images")
MAP = pathlib.Path("_migration/image-map.tsv")
OTHER = pathlib.Path("_migration/other-images.tsv")

BLOGGER = re.compile(r"""https?://[a-z0-9.-]*(?:bp\.blogspot|googleusercontent)\.com/[^"'\s)<>]+""")
# old-style Blogger path: /<a>/<b>/<c>/<d>/<size>/<name>; every URL in this blog has this shape (checked)
SHAPE = re.compile(r"^https?://[^/]+/([^/]+/[^/]+/[^/]+/[^/]+)/([^/]+)/([^/]+)$")
OTHER_IMG = re.compile(
    r"""<img[^>]*?src=["'](https?://[^"']+)|!\[[^\]]*\]\((https?://[^)\s]+)|"""
    r"""(https?://[^"'\s)<>]+\.(?:png|jpe?g|gif|svg|webp))(?=["'\s)<>]|$)""",
    re.I,
)
MAGIC = (b"\x89PNG", b"\xff\xd8\xff", b"GIF8", b"RIFF", b"BM")


def slug(post):
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", post.stem)


def safe(name):
    name = urllib.parse.unquote(name).replace("+", " ")
    name = re.sub(r"[^A-Za-z0-9._-]+", "-", name).strip("-.")
    return name or "image"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (blog image backup)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    if not data.startswith(MAGIC):
        raise ValueError("not an image (%r)" % data[:16])
    return data


def main():
    uses = []  # (post, exact url)
    others = []
    for post in sorted(POSTS.iterdir()):
        text = post.read_text(encoding="utf-8")
        uses += [(post, u) for u in BLOGGER.findall(text)]
        for m in OTHER_IMG.finditer(text):
            u = next(g for g in m.groups() if g)
            if not BLOGGER.match(u) and "youtube.com" not in u and "soundcloud.com" not in u:
                others.append((post.name, u))

    # group sizes of the same image: key = id path + filename, ignoring host number and size segment
    groups = collections.OrderedDict()
    for post, u in uses:
        m = SHAPE.match(u)
        assert m, u
        key = (m.group(1), m.group(3))
        groups.setdefault(key, []).append((post, u))

    taken = {}  # local path -> key, for collision handling
    result = {}  # key -> (local site path, status)
    for key, members in groups.items():
        first_post = members[0][0]
        ident, name = key
        d = OUT / slug(first_post)
        base = safe(name)
        stem, dot, ext = base.rpartition(".")
        path, n = d / base, 1
        while taken.get(path, key) != key:
            n += 1
            path = d / (f"{stem}-{n}.{ext}" if dot else f"{base}-{n}")
        taken[path] = key
        site = "/" + str(path.relative_to("static"))
        if path.exists():
            result[key] = (site, "ok")
            continue
        host = re.match(r"https?://[^/]+", members[0][1]).group(0).replace("http://", "https://")
        candidates = [f"{host}/{ident}/s0/{name}", f"{host}/{ident}/s1600/{name}"] + [u for _, u in members]
        status = None
        for c in dict.fromkeys(candidates):
            try:
                data = fetch(c)
            except Exception as e:  # try next size
                status = f"failed: {e}"
                time.sleep(0.5)
                continue
            d.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            status = "ok" if "/s0/" in c else f"ok ({c.split('/')[-2]})"
            break
        result[key] = (site, status)
        print(status, site, flush=True)
        time.sleep(0.2)

    with MAP.open("w") as f:
        f.write("post\told_url\tlocal_path\tstatus\n")
        for key, members in groups.items():
            site, status = result[key]
            for post, u in dict.fromkeys(members):
                f.write(f"{post.name}\t{u}\t{site}\t{status}\n")
    with OTHER.open("w") as f:
        f.write("post\turl\n")
        for row in dict.fromkeys(others):
            f.write("\t".join(row) + "\n")


if __name__ == "__main__":
    assert slug(pathlib.Path("2010-12-06-pagerank.html")) == "pagerank"
    assert safe("Screen%20Shot+1.png") == "Screen-Shot-1.png"
    main()
