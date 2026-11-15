"""Phase 3: convert Blogger HTML posts to markdown (format only, wording untouched).

usage: python3 -I blogger_to_md.py [REV]   (run from the repo root)

Reads each original post from git (REV, default 2f24a8b = last commit with the .html files)
and writes content/posts/<name>.md. Re-runnable: it never reads the current .md files.
SUPERSEDED after phase 3: posts are now edited in place (phase 4 link rewrites onwards); re-running this
overwrites those later edits.
Pipeline: HTML pre-pass (regex) -> pandoc JSON AST -> filter below -> pandoc gfm.
"""
import csv, html, json, re, subprocess, sys

REV = sys.argv[1] if len(sys.argv) > 1 else "2f24a8b"
GAP = {"t": "Space"}
IMAGES = {}
with open("_migration/image-map.tsv") as f:
    for r in csv.DictReader(f, delimiter="\t"):
        if r["status"] == "ok":
            IMAGES[r["old_url"]] = r["local_path"]


def local(url):
    return IMAGES.get(url) or IMAGES.get(html.unescape(url)) or url


def prepass(body):
    # Image-with-caption layout tables -> image block + caption block (markdown has no captions).
    body = re.sub(
        r'<table[^>]*class="tr-caption-container"[^>]*>\s*<tbody>\s*<tr>\s*<td[^>]*>(.*?)</td>\s*</tr>\s*'
        r'<tr>\s*<td[^>]*class="tr-caption"[^>]*>(.*?)</td>\s*</tr>\s*</tbody>\s*</table>',
        r"<div>\1</div><div>\2</div>", body, flags=re.S)
    # pandoc only makes a code block from <pre><code>; Blogger's <pre> holds <br>/<span>, so flatten to text.
    def pre(m):
        lang = "python" if re.search(r"brush:\s*py", m.group(1)) else "text"  # a language keeps the block fenced
        code = re.sub(r"<[^>]+>", "", re.sub(r"<br\s*/?>", "\n", m.group(2)))
        return f'<pre><code class="{lang}">{code}</code></pre>'
    return re.sub(r"<pre([^>]*)>(.*?)</pre>", pre, body, flags=re.S)


MATHS = re.compile(r"\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$", re.S)


def protect_maths(body):
    """Hugo passes maths through verbatim, so keep the original text (minus tags) out of pandoc's escaping."""
    found = []
    def hide(m):
        found.append(re.sub(r"<[^>]+>", "", re.sub(r"<br\s*/?>", "\n", m.group(0))))
        return f"MATHSPLACEHOLDER{len(found) - 1}X"
    return MATHS.sub(hide, body), found


def keep_style(attr):
    """Spans/divs worth keeping as raw HTML: coloured or monospace text."""
    style = dict(attr[2]).get("style", "").lower()
    return "color" in style or "courier" in style or "monospace" in style


def clean_attr(attr):
    style = dict(attr[2]).get("style", "")
    keep = "; ".join(p.strip() for p in style.split(";") if re.match(r"\s*(color|font-family)\s*:", p))
    return ["", [], [["style", keep]]]


CONTAINERS = {"Emph", "Strong", "Underline", "Strikeout", "Superscript", "Subscript", "SmallCaps"}


def blank(i):
    t = i["t"]
    if t in ("Space", "SoftBreak", "LineBreak"):
        return True
    if t in CONTAINERS:
        return all(blank(x) for x in i["c"])
    if t == "Span":
        return all(blank(x) for x in i["c"][1])
    return False


def strip(seg):
    while seg and seg[0]["t"] in ("Space", "SoftBreak", "LineBreak"):
        seg = seg[1:]
    while seg and seg[-1]["t"] in ("Space", "SoftBreak", "LineBreak"):
        seg = seg[:-1]
    return seg


def split(inls):
    """Filter inlines and split at runs of >=2 <br>; containers spanning a split are split too."""
    segs, cur, brs, pending = [], [], 0, []
    for i in inls:
        t = i["t"]
        if t == "LineBreak":
            brs += 1; pending.append(i); continue
        if t in ("Space", "SoftBreak") and brs:
            pending.append(i); continue
        if brs >= 2:
            segs.append(cur); cur = []
        else:
            cur += pending
        brs, pending = 0, []
        for n, part in enumerate(inline(i)):
            if n:
                segs.append(cur); cur = []
            cur += part
    if brs < 2:
        cur += pending
    segs.append(cur)
    return [s for s in (strip(s) for s in segs) if s and not all(blank(x) for x in s)]


def inline(i):
    """Return the filtered inline as segments (list of inline lists); >1 segment means it was split."""
    t, c = i["t"], i.get("c")
    if t in CONTAINERS:
        return [[{"t": t, "c": s}] for s in split(c)] or [[]]
    if t == "Span":
        parts = split(c[1]) or [[]]
        if keep_style(c[0]):
            return [[{"t": "Span", "c": [clean_attr(c[0]), p]}] for p in parts]
        return parts
    if t == "Link":
        attr, text, (url, title) = c
        return [[{"t": "Link", "c": [["", [], []], s, [local(url), title]]}] for s in (split(text) or [[]])]
    if t == "Image":
        attr, alt, (url, title) = c
        return [[{"t": "Image", "c": [["", [], []], alt, [local(url), title]]}]]
    return [[i]]


def edge(i, last):
    """Approximate first/last rendered markdown character of an inline, for flanking checks."""
    t, c = i["t"], i.get("c")
    if t == "Str": return c[-1] if last else c[0]
    if t in ("Space", "SoftBreak", "LineBreak"): return " "
    if t in ("Emph", "Strong"): return "*"
    if t == "Span" and c[0][2]: return ">" if last else "<"
    if t == "Span": return edge(c[1][-1 if last else 0], last) if c[1] else " "
    if t == "Link": return ")" if last else "["
    if t == "Image": return ")" if last else "!"
    return "`" if t == "Code" else ">" if last else "<"


def punct(ch):
    return not ch.isalnum() and not ch.isspace()


def emphasis(inls, before=" ", after=" "):
    """Use <em>/<strong> where '*' delimiters wouldn't parse (CommonMark flanking rules), e.g. 'Now*,*'."""
    out = []
    for k, i in enumerate(inls):
        t, c = i["t"], i.get("c")
        prev = edge(inls[k - 1], True) if k else before
        nxt = edge(inls[k + 1], False) if k + 1 < len(inls) else after
        if t in ("Emph", "Strong") and c:
            mark = "*" if t == "Emph" else "**"
            first, last = edge(c[0], False), edge(c[-1], True)
            opens = not first.isspace() and (not punct(first) or prev.isspace() or (punct(prev) and prev != "*"))
            closes = not last.isspace() and (not punct(last) or nxt.isspace() or (punct(nxt) and nxt != "*"))
            inner = emphasis(c, mark[0], mark[0])
            if opens and closes and prev != "*" and nxt != "*":
                out.append({"t": t, "c": inner})
            else:
                tag = "em" if t == "Emph" else "strong"
                out += [{"t": "RawInline", "c": ["html", f"<{tag}>"]}, *emphasis(c, ">", "<"),
                        {"t": "RawInline", "c": ["html", f"</{tag}>"]}]
        elif t in CONTAINERS:
            out.append({"t": t, "c": emphasis(c, prev, nxt)})
        elif t == "Span":
            out.append({"t": t, "c": [c[0], emphasis(c[1], prev, nxt)]})
        elif t == "Link":
            out.append({"t": t, "c": [c[0], emphasis(c[1], "[", "]"), c[2]]})
        elif t == "Str" and re.search(r"https?://|www\.", c):
            # bare URLs were plain text in Blogger; stop Goldmark's linkify turning them into links
            esc = re.sub(r"([\\`*_\[\]<>!#|~&])", r"\\\1", c).replace("://", "\\://").replace("www.", "www\\.")
            out.append({"t": "RawInline", "c": ["markdown", esc]})
        elif t == "Str" and "..." in c:
            # keep literal '...' (Blogger never had '…'); an escaped dot stops Goldmark's typographer
            parts = c.split("...")
            for n, p in enumerate(parts):
                if n: out.append({"t": "RawInline", "c": ["markdown", "..\\."]})
                if p: out.append({"t": "Str", "c": p})
        else:
            out.append(i)
    return out


def blocks(bs, top=True):
    out = []
    for b in bs:
        t, c = b["t"], b.get("c")
        if t in ("Plain", "Para"):
            kind = "Para" if top or t == "Para" else "Plain"
            segs = split(c)
            out += [{"t": "Para" if len(segs) > 1 else kind, "c": emphasis(s)} for s in segs]
        elif t == "Div":
            inner = blocks(c[1], top)
            out += [{"t": "Div", "c": [clean_attr(c[0]), inner]}] if keep_style(c[0]) else inner
        elif t == "BlockQuote":
            out.append({"t": t, "c": blocks(c)})
        elif t == "BulletList":
            out.append({"t": t, "c": [blocks(item, False) for item in c]})
        elif t == "OrderedList":
            out.append({"t": t, "c": [c[0], [blocks(item, False) for item in c[1]]]})
        elif t == "CodeBlock":
            out.append({"t": t, "c": [["", c[0][1][:1], []], c[1]]})
        else:
            out.append(walk_any(b))
    return out


def walk_any(node):
    """Tables etc.: filter any nested inline/block lists we recognise, leave structure alone."""
    if isinstance(node, list):
        if node and isinstance(node[0], dict) and "t" in node[0]:
            if node[0]["t"] in ("Plain", "Para", "Div", "CodeBlock", "BlockQuote", "BulletList", "OrderedList",
                                "Table", "RawBlock", "Header", "HorizontalRule", "Figure", "LineBlock"):
                return blocks(node, False)
            return [x for s in split(node) for x in s]
        return [walk_any(x) for x in node]
    if isinstance(node, dict) and "c" in node:
        return {"t": node["t"], "c": walk_any(node["c"])}
    return node


def unescape_brackets(md):
    """pandoc writes '[' as '\\[' which Hugo's maths passthrough reads as display maths; Goldmark
    only needs the escape when a link could form, which the build comparison checks."""
    out, fence = [], False
    for line in md.split("\n"):
        if line.startswith("```"):
            fence = not fence
        out.append(line if fence else line.replace("\\[", "[").replace("\\]", "]"))
    return "\n".join(out)


def convert(src):
    m = re.match(r"---\n(.*?\n)---\n(.*)", src, re.S)
    front, body = m.group(1), m.group(2)
    front = re.sub(r"^(thumbnail: )(\S+)$", lambda m: m.group(1) + local(m.group(2)), front, flags=re.M)
    body, maths = protect_maths(prepass(body))
    ast = json.loads(subprocess.run(["pandoc", "-f", "html+raw_html", "-t", "json"], input=body,
                                    capture_output=True, text=True, check=True).stdout)
    ast["blocks"] = blocks(ast["blocks"])
    md = subprocess.run(["pandoc", "-f", "json", "-t", "gfm", "--wrap=none"], input=json.dumps(ast),
                        capture_output=True, text=True, check=True).stdout
    md = unescape_brackets(md)
    for n, tex in enumerate(maths):
        assert md.count(f"MATHSPLACEHOLDER{n}X") == 1, n
        md = md.replace(f"MATHSPLACEHOLDER{n}X", tex)
    return f"---\n{front}---\n\n{md}"


def main():
    names = subprocess.run(["git", "ls-tree", "--name-only", REV, "content/posts/"],
                           capture_output=True, text=True, check=True).stdout.split()
    names = [n for n in names if n.endswith(".html")]
    for n in names:
        src = subprocess.run(["git", "show", f"{REV}:{n}"], capture_output=True, text=True, check=True).stdout
        open(n[:-5] + ".md", "w").write(convert(src))
    print(f"converted {len(names)}")


def selftest():
    md = convert('---\ntitle: t\n---\n<div class="separator"><a href="u"><img border="0" src="u" width="3" /></a></div>'
                 'a [b]<br /><br /><i>x<br /><br />y</i><span style="font-size: small;">z</span>')
    assert "<div" not in md and "\\[" not in md and "width" not in md, md
    assert "*x*\n\n*y*z" in md, md
    assert "[![](u)](u)" in md, md
    md = convert('---\ntitle: t\n---\nNow<i>,</i> x <b>A</b><i>, b </i>c http://a_b.com')
    assert "Now<em>,</em>" in md and "<em>, b</em>" in md and "http\\://a\\_b" in md, md
    md = convert('---\ntitle: t\n---\nso \\[a_1\\\\b &amp; c\\]<pre class="brush:py">x<br />  y</pre>')
    assert "\\[a_1\\\\b &amp; c\\]" in md and "``` python\nx\n  y\n```" in md, md


if __name__ == "__main__":
    selftest()
    main()
