# Phase 5: theme, home, archive, tags, search

## What was built
- Own small theme in `layouts/` with one stylesheet, `static/css/site.css` (colours as CSS variables, Chroma `github` syntax style appended). The Lanyon sidebar, its JS, Google Fonts and the five old CSS files are gone.
- **Header:** the logo is the home link (alt text = site title; the logo *is* the title wordmark, so the title isn't repeated as text). Nav: Home, Archive, Tags, Search, About, RSS (`/atom.xml`). Favicon and touch icon kept.
- **Home:** cards for the latest 10 posts: title, date, ~40-word plain-text summary, tags, thumbnail. Thumbnail = local front-matter `thumbnail`, else the first local image in the post, else none (105/140 posts have one). Summary partial (`_partials/summary.html`) drops headings and code blocks so cards start with prose; Blogger bold-as-heading lines can still lead (e.g. "No SIR So having…"). Links to the archive.
- **Archive** `/archive/`: all posts grouped by year.
- **Tags** `/tags/` (alphabetical with counts) and `/tags/<tag>/` (grouped by year); tags shown under each post and on cards.
- **Search** `/search/`: Pagefind default UI, orange accent; supports `?q=`. Only post pages are indexed (`data-pagefind-body` on `div.post`; the date is `data-pagefind-ignore`), 140 pages.
- **Related posts:** Hugo related content by tags (top 3, older or newer). 5 posts have no tag overlap above the threshold, so no block.
- Images centred, max-width 100%. Callout styles kept for the variants in use.

## Design
- Background `#f8f8f8` (matches the logo's background), text `#333` (11.9:1), muted `#666` (5.4:1).
- Accent / links `#c2410c`: **4.88:1** on the background, 5.18:1 on white cards, 4.54:1 on code background. All pass WCAG AA for normal text.
- Fonts: system stacks only, nothing downloaded. Body serif (Charter → Cambria → Georgia), UI sans (`system-ui`), mono `ui-monospace`.
- Column ~44rem; header and cards reflow at phone width (checked at 390px).
- Not done: dark mode (many old graphs have white backgrounds), caption styling (phase 3 captions are plain paragraphs, indistinguishable from body text without changing content).

## Tags
- 172 tags, every post tagged. No case clashes. Hugo was title-casing names ("Pokemon Tcg Pocket"); `capitalizeListTitles = false` now shows them as written (mostly lowercase Blogger labels, plus "AI").
- 75 tags are used by only one post.
- Odd: `ACS:Law` (URL `/tags/acs-law/`). Left as is.

## Removed URLs (baseline, no longer built)
- `/public/css/{poole,lanyon,syntax,customstyles,colorful}.css`: old theme CSS, unused.
- `/assets/main.css`: dropped in phase 2.

## Verification
- Post body text: 140/140 identical to the pre-phase-5 build (`compare_builds.py`).
- `/atom.xml` and `/feed.xml`: identical apart from the build timestamp.
- `/about/` and 404 text unchanged. All other baseline URLs built.
- All internal links/srcs resolve.
- `hugo --gc --minify` (as CI) has no warnings; `npx pagefind@1.5.2 --site public` indexes 140 pages; the workflow needs no change.
- Screenshots (desktop 1280px, phone 390px) of home, post, tag, search and archive in `_migration/phase5-screens/` (gitignored). Fixed from them: cards without a thumbnail pushed date and tags into a second column; the search page was unstyled.

## To look at
- Home page cards on desktop and phone; whether 10 is the right number.
- A long Blogger post with many images (e.g. watch-face-concepts-for-android-wear) to see full-size images centred.
- Search: `hugo` then `npx pagefind@1.5.2 --site public`, then serve `public/` (`hugo server` doesn't include the index).
