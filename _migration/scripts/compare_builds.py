"""Compare each post's rendered body between two Hugo builds (phase 3: before/after markdown conversion).

usage: compare_builds.py BEFORE_DIR AFTER_DIR URLS_FILE
Checks div.post text (whitespace ignored), <pre> text (exact, trailing whitespace ignored), and counts of
img, a (hrefs, with image hrefs collapsed), table, li, pre, iframe/object/embed.
"""
import sys, re, difflib
from html.parser import HTMLParser

VOID = {"br", "img", "hr", "input", "meta", "link", "area", "base", "col", "embed", "param", "source", "track", "wbr"}


class Post(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0; self.pre = 0; self.text = []; self.pres = []; self.tags = {}; self.hrefs = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if not self.depth:
            if tag == "div" and a.get("class") == "post": self.depth = 1
            return
        if tag in ("img", "a", "table", "li", "pre", "iframe", "object", "embed"):
            self.tags[tag] = self.tags.get(tag, 0) + 1
        if tag == "a" and "href" in a:
            h = a["href"]
            # image links: phase 3 points both thumbnail and full-size at one local file
            self.hrefs.append("IMG" if re.search(r"\.(png|jpe?g|gif|bmp)$", h, re.I) else h)
        if tag == "pre": self.pre += 1; self.pres.append("")
        if tag not in VOID: self.depth += 1
    def handle_endtag(self, tag):
        if not self.depth or tag in VOID: return
        if tag == "pre": self.pre -= 1
        self.depth -= 1
    def handle_data(self, d):
        if self.depth:
            self.text.append(d)
            if self.pre: self.pres[-1] += d


def parse(path):
    p = Post(); p.feed(open(path, encoding="utf-8").read())
    t = re.sub(r"\s+", "", "".join(p.text).translate(str.maketrans("‘’“”–—", "''\"\"--")))
    pres = ["\n".join(l.rstrip() for l in x.strip("\n").split("\n")) for x in p.pres]
    return t, pres, p.tags, sorted(p.hrefs)


before, after, urls = sys.argv[1:]
ok = 0
for path in open(urls).read().split():
    if not path.startswith("/20"): continue
    a, b = parse(before + path), parse(after + path)
    if a == b: ok += 1; continue
    print(f"\n## {path}")
    if a[0] != b[0]:
        sm = difflib.SequenceMatcher(None, a[0], b[0], autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != "equal":
                print(f"  text {op}: before={a[0][max(i1-25,0):i2+25][:160]!r} after={b[0][max(j1-25,0):j2+25][:160]!r}")
    if a[1] != b[1]: print(f"  pre differs: {len(a[1])} vs {len(b[1])} blocks")
    if a[2] != b[2]: print(f"  tags: {a[2]} -> {b[2]}")
    if a[3] != b[3]:
        print(f"  hrefs only before: {sorted(set(a[3]) - set(b[3]))[:5]}  only after: {sorted(set(b[3]) - set(a[3]))[:5]}  counts {len(a[3])}->{len(b[3])}")
print(f"\nidentical: {ok}")
