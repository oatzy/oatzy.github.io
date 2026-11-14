"""Rewrite each post's front-matter `date:` to UTC.

Jekyll built post URLs from the date in UTC; Hugo uses the date's own offset,
so normalising keeps the URLs identical. Idempotent.
"""
import re, sys, pathlib
from datetime import datetime, timezone

pat = re.compile(r"^date: '?([^'\n]+)'?$", re.M)
for p in sorted(pathlib.Path(sys.argv[1]).iterdir()):
    text = p.read_text()
    fm_end = text.index("\n---", 3)
    m = pat.search(text, 0, fm_end)
    assert m, p
    d = datetime.fromisoformat(m.group(1).strip())
    assert d.tzinfo, p  # every post has an explicit offset
    utc = d.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    p.write_text(text[:m.start()] + f"date: '{utc}'" + text[m.end():])
