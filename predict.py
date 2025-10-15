#!/usr/bin/env python3
"""
predict.py — loads θ0, θ1 from thetas.json and estimates price for a given mileage.
"""

from __future__ import annotations
import json
import sys

THETA_PATH = "thetas.json"

def load_thetas(path: str = THETA_PATH) -> tuple[float, float]:
    """
    Load θ0 and θ1 from a JSON file.
    If the file doesn't exist or keys are missing, fall back to (0.0, 0.0).
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        t0 = float(data.get("theta0", 0.0))
        t1 = float(data.get("theta1", 0.0))
        return t0, t1
    except FileNotFoundError:
        return 0.0, 0.0
    except Exception as e:
        print(f"Effor: failed to read {path}: {e}", file=sys.stderr)
        return 0.0, 0.0

def estimate_price(mileage: float, theta0: float, theta1: float) -> float:
    """
    Hypothesis: price_hat = θ0 + θ1 * mileage
    Thetas are in original units($/km), mileage is in km.
    """
    return theta0 + theta1 * mileage

def parse_mileage_from_imput() -> float:
    """
    Ask the user for mileage (km) via stdin.
    - Rejects negatives and non_numbers.
    """
    
    try:
        raw = input("Enter a mileage (km): ").strip()
    except EOFError:
        print("No input received.", file=sys.stderr)
        
    try:
        mileage = float(raw)
    except ValueError:
        print("Invalid input. Please enter a numeric mileage(km).", file=sys.stderr)
        sys.exit(1)
    
    if mileage < 0:
        print("Mileage cannot be negative.", file=sys.stderr)
        sys.exit(1)
    
    return mileage


def main() -> None:
    theta0, theta1 = load_thetas(THETA_PATH)
    mileage = parse_mileage_from_imput()
    price = estimate_price(mileage, theta0, theta1)
    
    if price < 0:
        price = 0.0
    
    print(f"Estimated price: ${price:.2f}")


if __name__ == "__main__":
    main()
    