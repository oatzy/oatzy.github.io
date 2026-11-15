# Phase 6: Maths (MathJax)

## Inventory

7 posts contain LaTeX (outside code). Typeset count = number of maths regions in the source:

| Post | Delimiters | Typeset |
|---|---|---|
| 2015-01-09 metric-and-binary-clocks-for-android | `\( \)` | 3 |
| 2015-01-11 follow-up-binary-proof-and-trinary-clock | `\[ \]`, `\( \)` | 30 |
| 2015-02-23 designing-general-relativity-based | `\[ \]`, `\( \)` | 80 |
| 2015-03-12 watch-face-concepts-for-android-wear | `\[ \]`, `\( \)` | 17 |
| 2015-06-28 the-pirate-game | `\[ \]`, `\( \)` | 4 |
| 2016-07-31 barber-queue | `\[ \]`, `\( \)` | 7 |
| 2020-09-06 first-program-i-ever-wrote | `$…$` inline, `$$…$$` display | 4 |

`random-as-good-as-full` has no LaTeX: it uses code blocks for its equations ("apologies for the code-block equations").
No post uses `$$` inline inside a paragraph; the one `$$` use (first-program) is a standalone display block.

## Approach

- `hugo.toml` passthrough is unchanged: block `$$…$$`, `\[…\]`; inline `\(…\)`. Single `$` is deliberately **not** a delimiter, so prices and shell prompts in prose can never become maths.
- `layouts/_markup/render-passthrough.html` sets `.Page.Store "hasMath"` and emits `\[…\]` / `\(…\)`. It `htmlUnescape`s the LaTeX first: the Blogger-era maths holds HTML entities (`&amp;` in `align*`/`pmatrix`, `&nbsp;`), which were being escaped twice and caused 5 "Misplaced &" errors. That double-escaping also existed in the phase 2–5 builds. The browser now sees the same LaTeX the Blogger pages served.
- `layouts/_partials/head.html` calls `.WordCount` (so content, and the hook, render first), then loads MathJax only if `hasMath` is set. It uses `defer` in `<head>`, so typesetting starts as soon as the DOM is parsed.
- MathJax **4.1.3** (`cdn.jsdelivr.net/npm/mathjax@4.1.3/tex-chtml.js`), released 2026-07-03. Version 4 also renders the `\\` line breaks in first-program's display block, which version 3 ignores outside an environment.

## Delimiter changes in post text

Only `2020-09-06-first-program-i-ever-wrote.md`: three single-`$` inline maths (`$a^2 + b^2 = c^2$`, `$3^2 + 4^2 = 5^2$`, `$5^2 + 7^2 = 12^2$`) → `\(…\)`. They never rendered under Jekyll (kramdown only knows `$$`); the post says "I need to figure how to make Jekyll do LaTeX". The maths text is unchanged.

## Verification

- MathJax loads on exactly the 7 posts above, and on no other page or feed (normal and `--minify` builds).
- Headless Chromium (playwright's chromium-1255, `--dump-dom`): typeset counts match the source on all 7 posts, with 0 `mjx-merror`, no raw `\(`, `\[`, `$$` or `\begin` left visible outside code, and no literal `amp;`/`nbsp;` text.
- `compare_builds.py` against the phase 5 build: 136 posts identical. The other 4 differ only inside maths: first-program's 3 delimiters, and `&amp;`/`&nbsp;` now decoded in 3 Blogger posts.
- Feeds: only first-program's entry changes (`$…$` → `\(…\)`), and the LaTeX stays readable as text for feed readers. Blogger maths in feeds now shows `&` rather than `&amp;`.
- Screenshots in `phase6-screens/` (gitignored): first-program (desktop and phone), binary-proof, general-relativity and watch-face. All checked visually.

## Known limits

- Home-page card summaries are plain text, so any maths in the first ~40 words shows as raw LaTeX there. None of the 7 maths posts is among the latest 10, so the home page is unaffected today; tag and archive pages show no summaries.
- Not changed: the `5^2 + 7^2 = 12^2` triplet in first-program is the post's own text (5, 12, 13 is the triplet mentioned two paragraphs later).

## Phase 7 candidates

`phase7-candidates.tsv`: 189 images in 43 posts. 45 match by filename (`eqn`, `equation`, `formula`, `math`, …) and 144 are images ≤100 px tall in posts tagged maths/probability/statistics/physics. This is a rough heuristic that over-includes (small graphs, icons); review each one before converting. Biggest: sexuality-and-population-dynamics (16), sharing-burger-between-three (14), too-many-lotteries (14), is-there-formula-for-perfect-christmas (13).
