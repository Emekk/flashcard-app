"""Load cards from a CSV file."""

import csv


def from_csv(filename, encoding="utf-8-sig"):
    with open(filename, "r", encoding=encoding) as f:
        reader = csv.reader(f)
        cards = list(reader)
    return cards
