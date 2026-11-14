# Live-site URL baseline (phase 0)

Captured 2026-11-14 from https://oatzy.github.io with sequential `curl -I`.

- `urls.txt`: 209 paths that return 200 (140 posts, 7 pages/feeds incl. `/index.html`, 62 files from `assets/` + `public/`). This is the set the Hugo build must still serve.
- `url-check.tsv`: every path checked, with status and why it was checked.
- `atom.xml` (140 entries, all posts, full content) and `feed.xml` (jekyll-feed, latest 10): copies of the live feeds.

Post URLs were taken from the live `atom.xml`, not derived from filenames. Internal links in the homepage and both feeds' content were also checked and added nothing new.

## Surprises

- **Post URL date = front-matter `date` converted to UTC, not the filename date.** This holds for all 140 posts. 53 differ from their filename: 49 are a day later (Blogger `-07:00`/`-08:00` evening posts, plus `2026-11-08-ai-who-came-to-dinner` dated 11-09) and 4 are earlier (`first-program-i-ever-wrote`, `fungus-simulation` (−3 days), `data-structure-pokemon-cards`, `random-as-good-as-full`). Hugo formats `:year/:month/:day` in the date's own offset, so phase 2 must normalise dates to UTC (or set an explicit `url`) to keep these URLs.
- The filename-derived URLs for those 53 return 404 (recorded in `url-check.tsv`).
- `/about` 301s to `/about/`. `/assets/main.css` (minima leftover) is served.
- The homepage sidebar links to `/archive/v0.1.zip` (Lanyon template leftover), which is a 404. Nothing serves `/tags/`, `/sitemap.xml` or `/robots.txt`.
- Feed `<link>`s are relative (`/2026/...`) in both feeds, because `site.url` is empty.
