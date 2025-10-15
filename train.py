#!/usr/bin/env python3
"""
train.py — trains θ0 and θ1 for a 1D linear regression
using batch gradient descent.

Responsibilities:
- Parse CLI arguments (data path, alpha, epochs, output path).
- Load data from CSV (expects header: km,price).
- Run training loop with SIMULTANEOUS updates of θ0 and θ1.
- Save learned thetas to JSON.
"""

from __future__ import annotations
import argparse
import csv
import json
from typing import List, Tuple


def parse_args() -> argparse.Namespace:
    """
    Parse CLI flags.

    --data   : path to CSV (default: data.csv)
    --alpha  : learning rate (float)
    --epochs : number of gradient steps (int)
    --out    : where to save thetas (JSON)
    """

    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data.csv", help="CSV file with header: km, price")
    ap.add_argument("--alpha", type=float, default=0.1, help="Learning rate")
    ap.add_argument("--epochs", type=int, default=1000, help="Number of gradient steps")
    ap.add_argument("--out", default="thetas.json", help="Output JSON file for learned parameters")
    return ap.parse_args()


def load_csv(path: str) -> Tuple[List[float], List[float]]:
    """
    Load a CSV with header 'km, price' and return two lists: xs (km), ys (price).

    Defensive parsing:
    - Skips empty lines and non-numeric rows.
    - Raises valueError if no valid rows are found.
    """

    xs: List[float] = []
    ys: List[float] = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            raise ValueError("Empty CSV.")

        if len(header) < 2:
            raise ValueError("Invalid header. Expect at least 2 columns: km, price")

        for row in reader:
            if not row or len(row) < 2:
                continue
            try:
                x = float(row[0].strip())
                y = float(row[1].strip())
            except (ValueError, IndexError):
                continue
            xs.append(x)
            ys.append(y)

    if not xs:
        raise ValueError("No valid rows found in data.")
    return xs, ys 

