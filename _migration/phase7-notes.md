# Phase 7: equation images → LaTeX (proposals, awaiting review)

No posts have been changed yet. Every replacement waits for Chris to approve it.

## Counts

- **Candidates examined:** 231. That's every image used in a post body that is at most 200px tall, plus everything in phase 6's `phase7-candidates.tsv`. I looked at each one myself.
- **Equations:** 137.
  - 136 become proposals in `phase7-equations.tsv`.
  - The other one, `compartmental-model-of-follower-growth/SIR-final-eqns.png`, is only a text link ("new model") to the image, not an embedded image, so there's nothing to replace.
- **Mixed:** 13, left as images and listed at the bottom of the review page:
  - two graphs with a formula label (beauty-of-procrastination)
  - two Wolfram Alpha screenshots (sharing-burger)
  - five network diagrams next to a matrix (social-posting parts one and two, tumbling-appendix-ii)
  - two colour-coded equations that match a diagram (toilet-roll)
  - two payoff tables with text headings (toilet-seat-conundrum)
- **Not equations:** 81. These are graphs, photos, maps, tweets, sudoku grids and hand-drawn diagrams.
- **Posts affected:** 25.
  - Biggest: sexuality-and-population-dynamics (17), too-many-lotteries (16), sharing-burger-between-three (15).
  - Full list in the TSV and the review page's table of contents.
- **Inline or display:** all 136 are display. Every equation image is its own paragraph (`[![](img)](img)` on its own line), so each becomes `$$ … $$`, also on its own line.
- **Confidence:** 130 high, 6 medium, none low.

## Medium confidence (check these first)

| Post | Image | Why |
|---|---|---|
| cost-of-loyalty | loyalty-formulas.png | The image writes the floor function as `fl(P)`, but the post text calls it `f()`. |
| rush-hour | Norm-eqn.png | Small Mathematica output. Check the four constants. |
| rush-hour | trigplot-eqn-crop.png | 15 Mathematica constants. Written as `\cos[…]`/`\sin[…]` with square brackets. |
| social-posting-part-one-whos-online | W-def-alt.png | The sums only have a `j` above the sigma, which is kept. |
| social-posting-part-two-we-post | example-external-conditions.png | The one-case braces for E₁ and E₂ are drawn as a plain `{`. |
| tumbling-appendix-ii-getting-formal | Tumblr-model-equations.png | A four-line system. `{0, 1, .., N}` is written with `\ldots`. |

## Transcription choices

- **Written as they appear:**
  - italic `ln`, `cos`, `sin`, `min`
  - `<N>` for the expectation, rather than `\langle N\rangle`
  - sums with only an upper index, e.g. `\sum^{j}`
  - ellipses as `\ldots`
- **Word styling:** italic words in definitions ("otherwise", "follows", "with") use `\textit{}`. The procrastination formulas use upright `\text{}`.
- **Layout:** multi-line equations use `aligned` (aligned on `=`) or `gathered` (centred lines).

## Verification

- **Review page:** rendered in headless Chromium (playwright chromium-1255). All 136 equations typeset, with no MathJax errors.
- **Sample check by eye:** 22 of the hardest equations, compared side by side with their images, including:
  - the Mathematica trig series
  - every case and matrix layout
  - the multi-line Taylor and binomial expansions

  None needed correcting. One review-page bug was fixed: the image paths were wrong.
- **Full apply test, in a throwaway git worktree** (since removed):
  - Approved every row. The dry run changed nothing, the real run replaced all 136 in 25 posts, and a second run reported all 136 as already applied.
  - Hugo built cleanly.
  - Every affected post loads MathJax and typesets exactly as many equations as it has proposals, with no errors. This includes the `<N>` equations, which Goldmark leaves alone inside `$$`.

## Thumbnails

These 9 posts use an equation image as their front-matter `thumbnail`. The apply script leaves thumbnails and image files alone, so the home and archive cards keep showing the image.

- beauty-of-procrastination
- cost-of-loyalty
- how-long-will-prime-number-be
- procrastination-dieting-and-will-power
- social-posting-part-one-whos-online
- social-posting-part-two-we-post
- too-many-lotteries
- train-problem
- twitter-bffs

Posts *without* a front-matter thumbnail fall back to their first image in the body. After applying, that could become a later image or none at all, e.g. for sexuality-and-population-dynamics and sharing-burger-between-three.

## How to review and apply

1. **Serve the review page:**
   ```
   python3 -m http.server
   ```
   Run this from the repo root, then open http://localhost:8000/_migration/phase7-review.html.
   - Each row shows the image next to its MathJax render and the raw LaTeX.
   - Medium-confidence rows have an orange edge.
   - Mixed images are listed at the end, for information only.
2. **Edit `_migration/phase7-equations.tsv`:**
   - Set `approved` to `y` or `n`.
   - To fix a transcription, edit the LaTeX in the `new` column. Keep it on one line, wrapped in `$$ … $$`.
   - Re-run `python3 -I _migration/scripts/make_phase7_review.py` to see your edits.
3. **Dry run:**
   ```
   python3 -I _migration/scripts/apply_equations.py --dry-run
   ```
   It lists what would change. If any approved row's image paragraph isn't found exactly once, it stops and writes nothing.
4. **Apply:**
   ```
   python3 -I _migration/scripts/apply_equations.py
   ```
   It only changes post bodies, and logs each change to `link-rewrites.tsv` as `equation`. Re-running is safe.
5. **Rebuild and spot-check** a few posts in `hugo server`.
