# Blog migration plan

Jekyll (Lanyon/minima hybrid) → Hugo + Pagefind, deployed via GitHub Actions.
This folder is underscore-prefixed so Jekyll doesn't publish it; Hugo ignores it (not under `content/`).

## Decisions

- Generator: **Hugo**, search: **Pagefind**, deploy: GitHub Actions (Pages source must be switched to "GitHub Actions").
- Dropbox files go to `oatzy/question-nobody-asked` (`~/workspace/question-nobody-asked`), **one folder per post**.
- Keep **tags** as browsable pages.
- Post wording is never changed; conversions are format-only. Equation-image → LaTeX swaps are reviewed by Chris post by post.

## Current state (findings)

- 140 posts: 108 Blogger HTML, 32 markdown. Blogger posts have `blogger_orig_url` in front matter (exact old→new mapping).
- MathJax is never loaded (`mathjax: true` does nothing; no script in `_includes/head.html`).
- Header logo is a CSS `::before` (`public/css/lanyon.css`), outside the home link, so not clickable.
- ~1144 blogspot image refs, 230 links to oatzy.blogspot posts, ~2200 unique external URLs, 82 Dropbox links.
- 35 Dropbox links are `dl.dropbox.com/u/4635169/...` (Public folder, dead since 2017): files must come from Chris's Dropbox. 47 are `/s/` or `/sh/` shared links (may still work with `?dl=1`).
- Feeds: custom `/atom.xml` (with empty `site.url`, so links are relative) and jekyll-feed `/feed.xml`. Both URLs must survive.
- Post URLs: `/:year/:month/:day/:slug.html`.

## Phases

0. **Baseline**: record every URL the live site serves (posts, pages, feeds, assets) into `_migration/baseline/`, plus copies of the current feeds. Used to verify phase 2.
1. **Save blogspot images**: download full-size (`s1600`) versions to `static/images/<post-slug>/`, write old-URL→local-path map, report failures.
2. **Generator swap (content unchanged)**: Hugo config, matching permalinks, `/atom.xml` + `/feed.xml` with absolute baseURL, Actions workflow (hugo → pagefind → deploy). Diff URL list against `_migration/baseline/urls.txt`. **Gotcha:** URL dates are the front-matter `date` in UTC, not the filename date; 53 posts differ, so Hugo must use UTC dates or set an explicit `url` per post. Keep `/about/`. Make feed links absolute.
3. **HTML → markdown**: pandoc with a pre-pass for Blogger `<br />` soup; collapse thumbnail-link wrappers to a single image linking to full size; point at local images; spot-check tables/code.
4. **Links**:
   - blogspot post links → github.io URLs via `blogger_orig_url`
   - Dropbox `/s/`, `/sh/`: download, commit to `question-nobody-asked/<post-slug>/`, rewrite links; flag failures
   - Dropbox `/u/`: list filenames for Chris to supply from Dropbox, then copy + rewrite
   - external links: lychee dead-link report; suggest Wayback snapshots, apply only approved ones
5. **Theme**: small custom theme, one CSS file, orange accent/link colour via CSS vars, no sidebar. Header logo + title inside home link; nav: Home, About, Archive, Tags, Search, RSS. Home = cards for latest N posts (title, date, summary, thumbnail), archive for the rest. Pagefind search page.
6. **Maths**: MathJax 3 only on pages with maths, via Hugo math passthrough. Verify existing maths posts.
7. **Stretch: equation images → LaTeX**: find candidate images (small, maths-tagged posts), transcribe by reading the images, Chris reviews.

## Status

- [x] 0 Baseline (see `baseline/README.md`)
- [ ] 1 Images
- [ ] 2 Hugo swap
- [ ] 3 HTML → md
- [ ] 4 Links
- [ ] 5 Theme / home / search
- [ ] 6 MathJax
- [ ] 7 Equation images (stretch)
