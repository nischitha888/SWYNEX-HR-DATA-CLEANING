import csv
from pathlib import Path

csv_path = Path(__file__).with_name("HR Dataset.csv")

with csv_path.open(newline="", encoding="utf-8-sig") as file:
    rows = list(csv.reader(file))

headers = rows[0]
data = rows[1:]

# Find a suitable width for each column
widths = [
    max(len(header), *(len(row[i]) for row in data))
    for i, header in enumerate(headers)
]

# Print the header, divider, and rows
print(" | ".join(header.ljust(widths[i]) for i, header in enumerate(headers)))
print("-+-".join("-" * width for width in widths))

for row in data:
    print(" | ".join(value.ljust(widths[i]) for i, value in enumerate(row)))