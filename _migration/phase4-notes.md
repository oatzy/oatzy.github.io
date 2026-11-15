# Phase 4 notes: links

Scripts (run from the repo root, all re-runnable):
- `scripts/fetch_other_images.py`: non-Blogger images → `static/images/<slug>/`, writes `other-image-map.tsv`
- `scripts/rewrite_links.py`: rewrites post bodies (A, B, C below), copies Dropbox files, appends to `link-rewrites.tsv`
- `scripts/dead_links.py LYCHEE_JSON`: writes `dead-links.tsv` (report only)

Posts are edited in place from now on; `blogger_to_md.py` is marked superseded. Only URLs changed: front matter is
byte-identical to HEAD (including `blogger_orig_url`), and the rendered text of all 140 posts is identical to the
pre-phase-4 build (`compare_builds.py`). Every href/src that changed is in `link-rewrites.tsv` (198 rows).

## A. Blogspot → github.io
- 105 unique links (122 occurrences) in 62 posts rewritten to absolute `https://oatzy.github.io/...` URLs via `blogger_orig_url`.
  All targets are in the baseline URL list. (The earlier "230" count included the 108 `blogger_orig_url` front-matter fields.)
- No label/search/archive/homepage blogspot links exist, and none were unmatched. No blogspot links remain.
- Other people's blogspot blogs (amidstdancers, nibblestew, ...) are untouched; they're external links (see D).

## B. Dropbox → `question-nobody-asked`
- All 82 Dropbox links rewritten; none remain. Source: `~/workspace/dropbox-Public/`.
- Copied into `~/workspace/question-nobody-asked/<slug>/` (29 folders, 94 files + a one-line README.md each naming the post): 5.3 MB, no file over 20 MB.
  Links use `https://github.com/oatzy/question-nobody-asked/blob/main/...` (files) and `tree/main/...` (the 3 folder shares).
  **These 404 until that repo is committed and pushed.**
- Folder shares: `watch-face-concepts-for-android-wear/android-wear/` (the per-face links point into the same folder),
  `designing-general-relativity-based/gravity/`, `metric-and-binary-clocks-for-android/autumn-theme/`.
- `checkins.txt` is used by two posts and copied into both folders (15 KB).
- Runnable HTML pages go in the blog, not the repo (GitHub won't serve them as pages), with the js/css each one loads:
  `static/files/decimalising-time/index1.htm`, `static/files/needlessly-incomprehensible-clock/index{,-alt}.htm`,
  `static/files/metric-and-binary-clocks-for-android/index-alt.htm` (14 files, 188 KB).
- The two Dropbox images (`BB-draft.jpg`, `SIR-final-eqns.png`) went to `static/images/<slug>/` like other images.
- The 60 Dropbox files no post links to were not copied.

## C. Non-Blogger images (`other-image-map.tsv`)
- 13 of 16 saved locally and relinked: 5 live, 2 from the local Dropbox copy, 6 from the Wayback Machine.
  - imgur serves a "not viewable in your region" placeholder from the UK, so both imgur images came from Wayback.
  - `twitter-virus`: the full-size Sophos screenshot was never archived; the article's 470px version of the same image was, and is used instead. **Check it's acceptable.**
- 2 were not images (a Wikimedia Commons page, a GitHub page) and were left as links.
- **Unrecoverable (1):** `acslaw-vs-internet`: the `antagonising` link to `localhostr.com/files/34804c/1285181519074.png` (dead, never archived). The link is left as it is.

## D. Dead-link report (`dead-links.tsv`, nothing applied)
lychee 0.24.2 (musl build in `~/.local/bin`; the gnu build needs a newer glibc) checked every external link on the
140 built post pages and /about/: 1188 unique URLs, concurrency 6 / 2 per host, 30 s timeout, 2 retries, browser UA.
Soft failures (network errors, timeouts, 5xx, 4xx other than 404/410) were re-checked once; links that worked on the re-check were dropped.

- **Dead: 112 links in 53 posts.** 80 have a Wayback snapshot near the post date; 32 don't.
  Biggest groups: 13 IBM Many Eyes visualisations (service shut down 2015), several Google Play app pages (Pirate Game unpublished), old news/blog articles.
- **Unverifiable: 52** (social/login sites, or 401/403/429 bot blocks: tumblr, foursquare, Google Spreadsheets, facebook, ...).
  Twitter/X answers 200 even for deleted tweets, so the 31 social-site links that passed are not proof they work either.
- Two links in `some-twitter-infographics` are malformed in the post itself (`http://http//tweetstats.com/`, `http://http//www.mapmyfollowers.com`).
- Internal links: all 3272 site-relative / `oatzy.github.io` links in the build resolve.

### For Chris to decide
1. Dead links with a Wayback copy (80): swap in the Wayback URL? (Suggested default: yes, keeping the link text.)
2. Dead links without one (32): leave, unlink (keep text), or add a "(dead link)" note?
3. The malformed `http://http//...` links: fix to `http://...` (they're dead anyway, so this only matters with option 1/2).
4. Commit and push `question-nobody-asked` before (or with) the blog going live, or its links 404.
5. The 470px Sophos image substitute (C).

## Verification
- Hugo build: 145 pages, no errors or warnings. 208/209 baseline URLs (only minima's unused `main.css` missing, as in phase 2).
- Text identical for all 140 posts; only hrefs/srcs changed, all accounted for in `link-rewrites.tsv`.
- No `dl.dropbox`, `dropbox.com` or `oatzy.blogspot` links remain in posts.

## Decisions (Chris, 2026-11-15)

1. Dead links with a Wayback copy now point to the snapshot, link text unchanged (`scripts/apply_wayback.py`, logged in `link-rewrites.tsv` as `wayback`). 77 applied. The other 3 are the Flash SoundCloud players in `fibonaccis-rainstorm` (embed params, not links); left as they are, since Flash can't play anyway.
2. The 32 dead links without a copy are left unchanged; Chris will review them himself.
3. `http://http//` typos in `some-twitter-infographics` fixed (2 URLs, 4 occurrences; logged as `typo`). Not re-checked for liveness.
4. 470px Sophos image accepted.
