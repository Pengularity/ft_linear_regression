#!/usr/bin/env python3
"""
precision.py — evaluate model precision R² score ans MSE(Mean Squared Error).
"""

from __future__ import annotations
import math
from src.linear_regression import load_csv, load_thetas, estimate_price


def compute_r2(xs, ys, t0, t1):
    y_mean = sum(ys) / len(ys)
    ss_res = sum((y - estimate_price(x, t0, t1)) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - y_mean) ** 2 for y in ys)
    return 1 - (ss_res / ss_tot)


def compute_mse(xs, ys, t0, t1):
    return sum((y - estimate_price(x, t0, t1)) ** 2 for x, y in zip(xs, ys)) / len(xs)


def main():
    xs, ys = load_csv("data.csv")
    t0, t1 = load_thetas("thetas.json")

    r2 = compute_r2(xs, ys, t0, t1)
    mse = compute_mse(xs, ys, t0, t1)
    rmse = math.sqrt(mse)

    print(f"Model precision:")
    print(f"  R² score = {r2:.4f}")
    print(f"  MSE      = {mse:.2f}")
    print(f"  RMSE     = {rmse:.2f}€")


if __name__ == "__main__":
    main()