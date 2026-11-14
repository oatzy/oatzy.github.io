# Phase 2: Jekyll → Hugo (content unchanged)

Hugo **0.169.0 extended** (pinned in `.github/workflows/hugo.yml`; 0.170.0 was one day old at the time). Pagefind **1.5.2** (1.6.0 was under two weeks old).
Local binary: `~/.local/bin/hugo`. Build: `hugo --gc --minify`, output to `public/` (gitignored). Preview: `hugo server`.

## Decisions

- **Layout:** `_posts/` → `content/posts/`, `about.markdown` → `content/about.md` (`url: /about/`), `assets/` → `static/assets/`, `public/` → `static/public/`, all with `git mv`. `404.html` → `layouts/404.html`.
- **Post URLs:** permalink `/:year/:month/:day/:slug` with `uglyURLs` for posts (adds `.html`).
  - **Dates:** Jekyll used the front-matter date in UTC, so every post's `date:` was rewritten to UTC (`_migration/scripts/dates_to_utc.py`). That's the same instant, and live pages already displayed UTC dates.
  - **Slug:** `[frontmatter] publishDate = [":filename", ...]` is there only so Hugo takes the slug from the filename minus its date prefix, as Jekyll did. The URL date still comes from `date`.
  - **New posts:** keep the `YYYY-MM-DD-slug.md` filename and a `date:` in front matter.
- **HTML content:** Hugo blocks `.html` content files by default; `[security] allowContent` permits HTML and markdown. This can drop back to markdown-only after phase 3.
- **Markdown:** Goldmark with raw HTML on (`unsafe`), and the passthrough extension for `$$…$$`, `\[…\]` and `\(…\)` so LaTeX isn't mangled before MathJax (phase 6). Code highlighting outputs classes, so the existing `syntax.css` still applies.
- **Liquid:** only 2 uses, both `{% include callout.html … %}` (in `modularity-madness` and `modularity-vs-inheritance`). Both became `{{< callout type="info" content="…" >}}` (`layouts/_shortcodes/callout.html`) with identical arguments. There was no other Liquid and no kramdown-only syntax (`{: }`, `{:: }`, `markdown="1"`). Footnotes render natively in Goldmark.
- **Feeds:**
  - `/atom.xml`: all posts, full content.
  - `/feed.xml`: latest 10, jekyll-feed fields (author, categories, summary).
  - Links are now absolute `https://oatzy.github.io/...`.
  - Entry `<id>`s are kept **exactly** as Jekyll wrote them (relative, e.g. `/2026/11/09/ai-who-came-to-dinner`), so feed readers won't re-show old posts.
  - The feed-level `<id>` in `atom.xml` was empty and is now the site URL.
- **Templates:** a minimal port of the Lanyon layouts (`layouts/`) using the existing CSS.
  - **Dropped sidebar links:** "Download" (`/archive/v0.1.zip`, a 404), "GitHub project" (empty href) and "Currently v0.1".
  - **Home page title:** now "Questions Nobody Asked.." instead of " · Questions Nobody Asked..".
  - **Related posts:** Jekyll without LSI showed the 3 latest posts, and Hugo does the same.
  - Phase 5 replaces all of this.
- **Disabled kinds** until phase 5: taxonomy, term, section, rss, sitemap.

## Verification (2026-11-14)

- **URLs:** every one of the 209 baseline URLs is built except `/assets/main.css`, a leftover from the old minima theme that nothing references. No unexpected extra URLs; the only new ones are `/images/...` (phase 1).
- **Feeds:** `atom.xml` has 140/140 entries and `feed.xml` 10/10, with ids, titles, `updated` and order identical to the baseline, and all links absolute.
- **Post text:** all 140 live posts were compared with the Hugo build (`_migration/scripts/compare_post_text.py`, which compares the `div.post` text with whitespace ignored). Smart quotes and footnote arrows were normalised first. 138 are identical. The 2 differences are expected:
  - `first-program-i-ever-wrote`: the maths shows as `$$…$$` in the source, where kramdown wrote `\[…\]`. MathJax isn't loaded on either site; phase 6.
  - `advent-of-code-jq`: kramdown wrongly turned a paragraph ending in the emoticon `:|` into a one-cell table. Hugo renders the paragraph as written.
- `hugo --gc --minify`: no errors or warnings. Pagefind indexes 143 pages.

## Cut-over steps

1. Review and commit this branch.
2. **In GitHub → repo Settings → Pages, set Source to "GitHub Actions"** before, or at the same moment as, merging to master. While the source is still "Deploy from a branch", Pages tries to build the repo with Jekyll, and with no Jekyll config left that would publish a broken site.
3. Merge `hugo-migration` into master and push. The `Build and deploy` workflow runs; check it succeeds. It can also be run manually (workflow_dispatch).
4. Spot-check the live site: the home page, a Blogger post, a post with a code block, `/about/`, `/atom.xml`, `/feed.xml`, and a 404 page.
