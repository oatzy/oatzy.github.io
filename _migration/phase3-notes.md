# Phase 3: Blogger HTML → markdown

All 108 Blogger `.html` posts in `content/posts/` are now `.md` (GFM, rendered by Goldmark). Wording is unchanged; this is a format conversion only.

- **Script:** `_migration/scripts/blogger_to_md.py` (runs a self-test first).
  - Re-runnable: it reads the original HTML from git (`2f24a8b`) and overwrites the `.md` files. Run it from the repo root with `python3 -I _migration/scripts/blogger_to_md.py`.
  - Tool: pandoc **3.12.1** (`~/.local/bin/pandoc`).
- **History:** the `git mv` renames are **staged on their own**, and the converted content is unstaged. Commit the staged renames first, then the content, so `git log --follow` keeps each post's history. A rename plus a full rewrite in one commit falls below git's similarity threshold.
- **Config:** `hugo.toml` no longer allows HTML content files.

## What the conversion does

- **Paragraphs:** runs of 2 or more `<br />` become paragraph breaks, and a single `<br />` stays a line break. Emphasis that spanned a break is split into two.
- **Wrappers:** spans, divs and fonts used for size, margins or fonts like Verdana are unwrapped.
  - **Kept as raw HTML**, because they carry meaning: coloured text (`color:` spans in `twitter-virus`, `christmas-eve`, `su-doku-solver`) and monospace (Courier) spans/divs. Their `style` keeps only `color` and `font-family`.
- **Code:** Blogger `<pre class="brush:…">` becomes fenced code (`python` for `brush:py`, `text` otherwise), with the code text identical and the `<br>`s turned into newlines.
- **Images:** every Blogger URL is rewritten from `_migration/image-map.tsv`, including the front-matter `thumbnail:`.
  - The thumbnail wrapper becomes `[![alt](/images/…)](/images/…)`.
  - **Captions:** the 27 image-caption layout tables (`tr-caption-container`; these are all the tables there were) become an image paragraph followed by a caption paragraph.
  - **Lost image:** `christmas-eve-graph.png` stays on its old (404) Blogger URL, for phase 4.
- **Emphasis:** where `*`/`**` wouldn't parse under CommonMark's flanking rules (e.g. `Now<i>,</i>`, or bold directly followed by italic), the converter writes `<em>`/`<strong>` instead. That's 56 `<em>` and 51 `<strong>`.
- **Bare URLs** in text are escaped (`http\://…`), so Goldmark's linkify doesn't turn text that was plain in Blogger into links. Only `friend-network-evolution` was affected.
- **Maths:** `\[…\]`, `\(…\)` and `$$…$$` regions (6 posts from 2015–16) are protected from pandoc and copied back byte-for-byte, so Hugo's passthrough hands MathJax exactly the original LaTeX (phase 6).
- **`[`:** pandoc escapes `[` as `\[`, which Hugo's passthrough would read as display maths. The converter unescapes it outside code; the build comparison confirms no links formed by accident.

### Left as raw HTML, and why

| What | Count | Why |
|---|---|---|
| `<object>`/`<embed>`/`<param>` | 8 objects in 4 posts (`handful-of-film-reviews`, `spread-through-network`, `musings-on-feasibility-of-real-pokemon`, `fibonaccis-rainstorm`) | Old Flash YouTube embeds. They're already dead in browsers, kept verbatim for phase 4 to replace or flag |
| `<iframe>` | 4 in `designing-general-relativity-based` | Embeds; markdown can't express them |
| coloured / monospace `<span>`, `<div>` | 87 spans, 5 divs | Markdown has no colour; the monospace is used for inline code-ish text and has no exact markdown equivalent without restyling |
| `<em>`/`<strong>` | 56/51 | See emphasis above |
| `<u>` | 5 | No underline in markdown |

## Verification (2026-11-14)

The "before" build is HEAD (`2f24a8b`, still HTML) and the "after" build is the converted posts. Both were built with `hugo` (no minify) and compared with `_migration/scripts/compare_builds.py`. It compares the `div.post` text with whitespace ignored, the `<pre>` text exactly, counts of img/a/table/li/pre/iframe/object/embed, and the hrefs (image links collapsed).

- **95 of 140 posts identical**, including all 32 that were already markdown.
- **Text differences:** none. Blogger posts keep a literal `...` (the converter writes `..\.` so Goldmark's typographer leaves it alone); 131 of 140 posts render identically to the pre-conversion build, the rest differ only in the explained table/link/`<br>`-in-code changes.
  - **To undo:** escaping the dots (`\.\.\.`) in the converted posts would keep them literal. That's a one-line addition to the converter, if wanted.
- **Explained differences:**
  - **Table counts** (4 posts): the image-caption tables were converted on purpose (see above).
  - **`<pre>` text** (3 posts): the old blocks contained `<br />`, which the comparison doesn't read as a newline. The new blocks have the same lines.
  - **`su-doku-solver`, one fewer `<a>`:** Blogger's empty `<a name='more'></a>` "read more" anchor was dropped. No href is lost.
  - **2 hrefs re-encoded:** `[`/`]` inside a URL query string became `%5B`/`%5D` (Goldmark). It's the same URL. Affects `acslaw-vs-internet` and `revisited-tweets-by-gender`.
  - **Embeds:** object/embed/iframe counts are unchanged after the fix.
- **URLs:** 208 of the 209 baseline URLs are still built (`/assets/main.css` was dropped in phase 2, as before).
- **Build:** `hugo` and `hugo --gc --minify` both run with no errors or warnings.
- **Hugo pitfalls:** no `{{<`/`{{%` or leftover placeholders. Maths delimiters appear only in the 6 maths posts.

### Visual differences to expect

- **Image size:** images now link to and display the **full-size** local file instead of Blogger's 320/400 px thumbnail. The CSS has `img { max-width: 100% }`, so they fill the column. Small diagrams may look larger than before.
- **Centring:** images are no longer centred. Blogger's `separator` div was `text-align: center`. Phase 5's theme can centre images in CSS.
- **Captions:** they're plain paragraphs under the image, not centred small text.
- **Paragraph spacing:** Blogger's `<br /><br />` now renders as real `<p>` spacing.

## Spot-check list (for Chris)

Run `hugo server` and open:

1. http://localhost:1313/2015/03/12/watch-face-concepts-for-android-wear.html: 32 code blocks, 13 captioned images, maths, monospace spans
2. http://localhost:1313/2015/02/23/designing-general-relativity-based.html: iframes, lots of maths, code
3. http://localhost:1313/2015/01/12/follow-up-binary-proof-and-trinary-clock.html: maths, captions, code
4. http://localhost:1313/2015/01/09/metric-and-binary-clocks-for-android.html: captions, code, maths
5. http://localhost:1313/2017/04/02/testing-python-unicode-handling-lazy-way.html: code blocks (Python and terminal output)
6. http://localhost:1313/2016/07/31/barber-queue.html: code, maths
7. http://localhost:1313/2015/06/29/the-pirate-game.html: captioned images
8. http://localhost:1313/2011/06/25/fibonaccis-rainstorm.html: dead Flash embeds, images
9. http://localhost:1313/2010/08/15/handful-of-film-reviews.html: Flash embeds, heavy emphasis
10. http://localhost:1313/2010/08/27/good-departed-pilgrim-flew-over.html: `*`-footnotes next to emphasis
11. http://localhost:1313/2014/10/14/dark-matter-and-machine-learning.html: many images, inline maths-like text
12. http://localhost:1313/2012/03/15/friend-network-evolution.html: escaped bare URLs
