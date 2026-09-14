import csv
from pathlib import Path

path = Path("./lin-fr-proverbs.tsv")

# Load existing rows
with path.open("r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter="\t")
    rows = list(reader)

header = rows[0]
existing = rows[1:]

new_rows = [] # new list

# Avoid duplicates by Lingala proverb text
seen = {r[0].strip() for r in existing if r}
added = []
for r in new_rows:
    if r[0] not in seen:
        existing.append(r)
        seen.add(r[0])
        added.append(r)

with path.open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter="\t", lineterminator="\n")
    writer.writerow(header)
    writer.writerows(existing)

print(f"Updated {path}")
print(f"Added {len(added)} new entries. Total: {len(existing)}.")
