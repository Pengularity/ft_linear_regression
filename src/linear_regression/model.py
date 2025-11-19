from __future__ import annotations
import csv
import json
from typing import List, Tuple


def load_csv(path: str) -> Tuple[List[float], List[float]]:
    """
    Load a CSV with header 'km,price'
    Return two lists: xs (km), ys (price).
    """
    xs: List[float] = []
    ys: List[float] = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            raise ValueError(
                "Empty CSV. Expect header 'km,price' and numeric rows."
                )
        if len(header) < 2:
            raise ValueError(
                "Invalid header. Expect at least 2 columns: km,price"
                )
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


def save_thetas(theta0: float, theta1: float,
                out_path: str = "thetas.json") -> None:
    """
    Persist learned parameters (original units: $/km) to JSON.
    """
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"theta0": theta0, "theta1": theta1}, f)


def load_thetas(path: str = "thetas.json") -> tuple[float, float]:
    """
    Load θ0, θ1 from JSON;
    Fallback to zeros if file missing/corrupt.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        t0 = float(data.get("theta0", 0.0))
        t1 = float(data.get("theta1", 0.0))
        return t0, t1
    except Exception:
        return 0.0, 0.0


def mean_std(xs: list[float]) -> tuple[float, float]:
    m = len(xs)
    mu = sum(xs) / m
    var = sum((x - mu) * (x - mu) for x in xs) / m
    sigma = var ** 0.5 if var > 0 else 1.0
    return mu, sigma


def standardize(xs: list[float], mu: float, sigma: float) -> list[float]:
    return [(x - mu) / sigma for x in xs]


def train_batch_gradient_descent(xs: list[float],
                                 ys: list[float],
                                 alpha: float,
                                 epochs: int) -> tuple[float, float]:
    """
    Batch gradient descent for h(x) = θ0 + θ1 * x
    Simultaneous updates each epoch:
      θ0 := θ0 - α * (1/m) * Σ (h(x_i) - y_i)
      θ1 := θ1 - α * (1/m) * Σ (h(x_i) - y_i) * x_i
    Start from θ0=0, θ1=0.
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
        t0 = t0 - alpha * (sum_err / m)
        t1 = t1 - alpha * (sum_err_x / m)
    return t0, t1


def estimate_price(mileage_km: float, theta0: float, theta1: float) -> float:
    """Hypothesis in original units: price_hat = θ0 + θ1 * mileage (km)."""
    return theta0 + theta1 * mileage_km
