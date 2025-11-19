#!/usr/bin/env python3
"""
predict.py — loads θ0, θ1 from thetas.json
and estimates price for a given mileage (km).
"""

from __future__ import annotations
import sys
from src.linear_regression.model import load_thetas, estimate_price

THETA_PATH = "thetas.json"


def _parse_mileage() -> float:
    """
    Ask the user for mileage (km).
    Rejects negatives and non-numeric input.
    """
    try:
        raw = input("Enter a mileage (km): ").strip()
    except EOFError:
        print("No input received.", file=sys.stderr)
        sys.exit(1)

    try:
        mileage = float(raw)
    except ValueError:
        print(
            "Invalid input. Please enter a numeric mileage (km).",
            file=sys.stderr
        )
        sys.exit(1)

    if mileage < 0:
        print("Mileage cannot be negative.", file=sys.stderr)
        sys.exit(1)

    return mileage


def main() -> None:
    theta0, theta1 = load_thetas(THETA_PATH)
    mileage = _parse_mileage()
    price = estimate_price(mileage, theta0, theta1)
    if price < 0:
        price = 0.0
    print(f"Estimated price: {price:.2f}€")


if __name__ == "__main__":
    main()
