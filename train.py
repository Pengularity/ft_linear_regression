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


def train_batch_gradient_descent(xs: list[float], ys: list[float],
                                alpha: float, epochs: int) -> tuple[float, float]:
    """
    Batch gradient descent for h(x) = θ0 + θ1 * x

    Simultaneous updates each epoch:
      θ0 := θ0 - α * (1/m) * Σ (h(x_i) - y_i)
      θ1 := θ1 - α * (1/m) * Σ (h(x_i) - y_i) * x_i

    Starts from θ0=0.0, θ1=0.0
    """
    m = float(len(xs))
    t0 = 0.0
    t1 = 0.0

    for _ in range(int(epochs)):
        sum_err = 0.0
        sum_err_x = 0.0
 
        for x, y in zip(xs, ys):
            h = t0 + t1 * x
            e = h - y
            sum_err += e
            sum_err_x += e * x
        
        new_t0 = t0 - alpha * (sum_err / m)
        new_t1 = t1 - alpha * (sum_err_x / m)
        t0, t1 = new_t0, new_t1

    return t0, t1


def save_thetas(t0: float, t1: float, out_path: str) -> None:
    """Persist learned parameters to a small JSON file"""
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"thetas0": t0, "thetas1": t1}, f)


def main() ->None:
    args = parse_args()
    xs, ys = load_csv(args.data)
    t0, t1 = train_batch_gradient_descent(xs, ys, alpha=args.alpha, epochs=args.epochs)
    save_thetas(t0, t1, args.out)
    print(f"Saved thetas: θ0={t0:.6f}, θ1={t1:.6f} -> {args.out}")


if __name__ == "__main__":
    main()