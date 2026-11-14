"""Compare the visible text of each post (div.post) between saved live pages and the Hugo build.

usage: compare_post_text.py LIVE_DIR BUILD_DIR URLS_FILE
LIVE_DIR holds pages saved as the URL path with '/' replaced by '_'.
"""
import sys, re, difflib, html
from html.parser import HTMLParser

class PostText(HTMLParser):
    VOID = {"br", "img", "hr", "input", "meta", "link", "area", "base", "col", "embed", "param", "source", "track", "wbr"}
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0; self.skip = 0; self.out = []
    def handle_starttag(self, tag, attrs):
        if tag in self.VOID: return
        if self.depth: self.depth += 1
        elif tag == "div" and ("class", "post") in attrs: self.depth = 1
        if self.depth and tag in ("script", "style"): self.skip += 1
    def handle_endtag(self, tag):
        if tag in self.VOID or not self.depth: return
        if tag in ("script", "style") and self.skip: self.skip -= 1
        self.depth -= 1
    def handle_data(self, data):
        if self.depth and not self.skip: self.out.append(data)

def words(path):
    p = PostText(); p.feed(open(path, encoding="utf-8").read())
    t = "".join(p.out)
    # smart quotes / footnote arrows differ between kramdown and goldmark; whitespace differs with highlighter spans
    t = t.translate(str.maketrans("‘’“”–—", "''\"\"--", "\ufe0e"))
    return list(re.sub(r"\s+", "", t))

live, build, urls = sys.argv[1:]
same = 0
for path in open(urls).read().split():
    if not path.startswith("/20"): continue
    a = words(f"{live}/{path.replace('/', '_')}"); b = words(build + path)
    if a == b: same += 1; continue
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    print(f"\n## {path}  ({len(a)} vs {len(b)} chars, ratio {sm.ratio():.4f})")
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            print(f"  {op}: live={''.join(a[max(i1-30,0):i2+30])[:200]!r}  hugo={''.join(b[max(j1-30,0):j2+30])[:200]!r}")
print(f"\nidentical: {same}")
