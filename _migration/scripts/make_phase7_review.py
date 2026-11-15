"""Phase 7: build _migration/phase7-review.html from _migration/phase7-equations.tsv. Run from the repo root.

usage: python3 -I _migration/scripts/make_phase7_review.py

Re-run after editing the TSV. View with `python3 -m http.server` from the repo root at
http://localhost:8000/_migration/phase7-review.html
"""
import csv, html, itertools

MIXED = [  # equations mixed with diagrams/plots/colour: left as images, for reference only
    ("2010-08-06-beauty-of-procrastination", "/images/beauty-of-procrastination/formula-graph1.png", "graph with a formula label"),
    ("2010-08-06-beauty-of-procrastination", "/images/beauty-of-procrastination/formula-graph2.png", "graph with a formula label"),
    ("2012-07-02-sharing-burger-between-three", "/images/sharing-burger-between-three/soln-1.png", "Wolfram Alpha screenshot (input and numeric solution)"),
    ("2012-07-02-sharing-burger-between-three", "/images/sharing-burger-between-three/soln-2.png", "Wolfram Alpha screenshot (input and numeric result)"),
    ("2011-07-30-social-posting-part-one-whos-online", "/images/social-posting-part-one-whos-online/M-example.png", "network diagram next to its adjacency matrix"),
    ("2011-07-30-social-posting-part-one-whos-online", "/images/social-posting-part-one-whos-online/W-example.png", "network diagram next to its weight matrix"),
    ("2011-07-30-social-posting-part-one-whos-online", "/images/social-posting-part-one-whos-online/antagonist-example.png", "network diagram next to its weight matrix"),
    ("2011-07-31-social-posting-part-two-we-post", "/images/social-posting-part-two-we-post/antagonist-stablepoint.png", "state vectors next to network diagrams"),
    ("2011-06-23-toilet-roll", "/images/toilet-roll/looroll-eqn-num.png", "colour-coded numbers that match a diagram"),
    ("2011-06-23-toilet-roll", "/images/toilet-roll/looroll-eqn1.png", "colour-coded symbols that match a diagram"),
    ("2011-08-03-toilet-seat-conundrum", "/images/toilet-seat-conundrum/Game1Matrix.png", "payoff table with text headings"),
    ("2011-08-03-toilet-seat-conundrum", "/images/toilet-seat-conundrum/Game2Matrix.png", "payoff table with text headings"),
    ("2011-07-24-tumbling-appendix-ii-getting-formal", "/images/tumbling-appendix-ii-getting-formal/network-example.png", "network diagram next to its adjacency matrix"),
]

rows = list(csv.DictReader(open("_migration/phase7-equations.tsv"), delimiter="\t"))
e = html.escape
out = []
for n, (post, group) in enumerate(itertools.groupby(rows, key=lambda r: r["post"])):
    group = list(group)
    out.append(f'<section><h2 id="p{n}">{e(post)} <small>({len(group)})</small></h2>')
    for r in group:
        tex = r["new"].strip()
        tex = tex[2:-2].strip() if tex.startswith("$$") and tex.endswith("$$") else tex
        cls = "conf-" + e(r["confidence"])
        note = f'<p class="note">{e(r["notes"])}</p>' if r["notes"] else ""
        appr = f' · approved: <b>{e(r["approved"])}</b>' if r["approved"].strip() else ""
        out.append(f'''<article class="{cls}">
  <div class="meta"><code>{e(r["image"].rsplit("/", 1)[-1])}</code> · <span class="conf">{e(r["confidence"])}</span>{appr}</div>
  <div class="pair">
    <figure><figcaption>Image</figcaption><img src="../static{e(r["image"])}" alt=""></figure>
    <figure><figcaption>LaTeX</figcaption><div class="math">\\[{e(tex)}\\]</div></figure>
  </div>
  <pre>{e(tex)}</pre>{note}
</article>''')
    out.append("</section>")

mixed = "".join(f'<article><div class="meta"><code>{e(p)}</code> · {e(why)}</div><img src="../static{e(i)}" alt=""></article>'
                for p, i, why in MIXED)
low = sum(r["confidence"] != "high" for r in rows)
toc = "".join(f'<li><a href="#p{n}">{e(p)}</a></li>' for n, p in enumerate(dict.fromkeys(r["post"] for r in rows)))

page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Equation Review</title>
<script>window.MathJax = {{ tex: {{ inlineMath: [['\\\\(', '\\\\)']], displayMath: [['\\\\[', '\\\\]']], processEscapes: false }} }};</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@4.1.3/tex-chtml.js"></script>
<style>
:root {{ --bg: #f8f8f8; --card: #fff; --text: #222; --muted: #666; --accent: #c2410c; --line: #ddd; }}
body {{ margin: 0 auto; max-width: 1100px; padding: 16px; background: var(--bg); color: var(--text); font: 15px/1.5 system-ui, sans-serif; }}
h1 {{ color: var(--accent); }} h2 {{ margin-top: 2em; border-bottom: 2px solid var(--accent); }}
article {{ background: var(--card); border: 1px solid var(--line); border-radius: 6px; padding: 12px; margin: 12px 0; }}
article.conf-medium, article.conf-low {{ border-left: 5px solid var(--accent); }}
.meta {{ color: var(--muted); font-size: 13px; }} .conf {{ font-weight: 600; }}
.pair {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; align-items: center; }}
@media (max-width: 700px) {{ .pair {{ grid-template-columns: 1fr; }} }}
figure {{ margin: 0; overflow-x: auto; }} figcaption {{ font-size: 12px; color: var(--muted); }}
img {{ max-width: 100%; background: #fff; }}
pre {{ background: #f3f3f3; padding: 8px; overflow-x: auto; font-size: 12px; white-space: pre-wrap; word-break: break-all; }}
.note {{ margin: 4px 0 0; font-size: 13px; color: var(--accent); }}
</style></head><body>
<h1>Equation images → LaTeX</h1>
<p>{len(rows)} proposals in {len(toc.split("<li>")) - 1} posts; {low} not high confidence (orange edge).
Compare each image with its LaTeX render, then mark <code>approved</code> y/n in <code>_migration/phase7-equations.tsv</code>
(or fix the LaTeX in its <code>new</code> column) and re-run <code>make_phase7_review.py</code>.</p>
<ul>{toc}<li><a href="#mixed">Mixed images (left as images)</a></li></ul>
{"".join(out)}
<section><h2 id="mixed">Mixed images, left as images ({len(MIXED)})</h2>{mixed}</section>
</body></html>
'''
open("_migration/phase7-review.html", "w").write(page)
print(f"wrote _migration/phase7-review.html: {len(rows)} proposals, {low} not high confidence")
