"""Phase 7: replace approved equation images with LaTeX. Run from the repo root.

usage: python3 -I _migration/scripts/apply_equations.py [--dry-run] [TSV]

Applies rows of _migration/phase7-equations.tsv whose `approved` column is `y`: the exact `old`
markdown (the image paragraph) in the post body becomes `new`. Every approved row is checked first
(its `old` text must appear exactly once in the post body), so nothing is written if any row fails.
Image files and front-matter thumbnails are left alone. Logs each change to
_migration/link-rewrites.tsv with kind `equation`. Re-running is safe: applied rows no longer match
and are reported as already applied.
"""
import csv, sys

args = [a for a in sys.argv[1:] if a != "--dry-run"]
dry = "--dry-run" in sys.argv
tsv = args[0] if args else "_migration/phase7-equations.tsv"
rows = [r for r in csv.DictReader(open(tsv), delimiter="\t") if r["approved"].strip().lower() == "y"]

def split(text):
    # front matter is the leading '---' block; only the body may change
    end = text.index("\n---", 3) + 4
    return text[:end], text[end:]

posts, todo, done, errors = {}, [], [], []
for r in rows:
    path = f"content/posts/{r['post']}.md"
    if path not in posts:
        posts[path] = split(open(path).read())
    body = posts[path][1]
    n = body.count(r["old"])
    if n == 1:
        todo.append((path, r))
    elif n == 0 and r["new"] in body:
        done.append(r)
    else:
        errors.append(f"{r['post']}: {r['image']} found {n} times")

if errors:
    sys.exit("not applied, fix these rows first:\n  " + "\n  ".join(errors))

for path, r in todo:
    fm, body = posts[path]
    posts[path] = (fm, body.replace(r["old"], r["new"]))
    print(("would replace" if dry else "replaced"), r["post"], r["image"])
for r in done:
    print("already applied", r["post"], r["image"])

if not dry and todo:
    for path in {p for p, _ in todo}:
        open(path, "w").write("".join(posts[path]))
    with open("_migration/link-rewrites.tsv", "a") as f:
        csv.writer(f, delimiter="\t", lineterminator="\n").writerows(
            [r["post"], "equation", r["old"], r["new"]] for _, r in todo)
print(f"{len(todo)} {'to apply' if dry else 'applied'}, {len(done)} already applied, {len(rows)} approved rows")
