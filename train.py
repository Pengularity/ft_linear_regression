#!/usr/bin/env python3
"""
Thin CLI: load data, standardize x,
train with batch GD, convert thetas back, save JSON.
"""

from __future__ import annotations
import argparse
from src.linear_regression.model import (
    load_csv,
    save_thetas,
    mean_std,
    standardize,
    train_batch_gradient_descent,
)


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--data", default="data.csv", help="CSV file with header: km,price"
    )
    ap.add_argument("--alpha", type=float, default=0.05, help="Learning rate")
    ap.add_argument(
        "--epochs", type=int, default=20000, help="Number of gradient steps"
    )
    ap.add_argument(
        "--out",
        default="thetas.json",
        help="Output JSON file for learned parameters",
    )
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    xs, ys = load_csv(args.data)

    # Standardize mileage
    mu, sigma = mean_std(xs)  # km
    zs = standardize(xs, mu, sigma)  # z = (x - mu)/sigma

    a, b = train_batch_gradient_descent(
        zs, ys, alpha=args.alpha, epochs=args.epochs
    )

    # Convert back to original units: y ≈ θ0 + θ1 * x
    theta1 = b / sigma
    theta0 = a - (b * mu) / sigma

    save_thetas(theta0, theta1, args.out)
    print(
        f"Saved thetas (original units): θ0={theta0:.6f}, "
        f"θ1={theta1:.12f} -> {args.out}"
    )
    with open("model_params.txt", "a", encoding="utf-8") as log:
        log.write(
            f"alpha={args.alpha}, epochs={args.epochs}, "
            f"theta0={theta0:.6f}, theta1={theta1:.6f}\n"
        )


if __name__ == "__main__":
    main()
