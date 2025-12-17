# ft_linear_regression

> A clean, single-variable linear regression model trained with batch gradient descent. It predicts car prices from mileage using only Python’s standard library.

This project is an implementation of linear regression from scratch as required by the 42 school curriculum. The goal is to build the model without relying on NumPy, scikit-learn, or any other machine learning libraries.

---

## 🐳 Dockerized Environment

In strict adherence to the **"System Isolation"** guideline, this project is fully containerized. 
It does **not** pollute your local shell with `pip` packages or virtual environments.

* **Isolation:** Runs in a pristine `python:3.11-slim` container.
* **Reproducibility:** Guarantees identical results on every machine.
* **Persistence:** Trained models (`thetas.json`) are saved to your local host machine via volume mounting.

## 🚀 Setup and Quick Start

1.  **Prerequisite:** Ensure **Docker** is installed and running.


2.  **Train the model:**
    ```bash
    make
    ```

3.  **Predict a price:**
    ```bash
    make predict
    ```

4.  **Run bonus visualizations and metrics:**
    ```bash
    make bonus
    ```

## ⚙️ Custom Parameters

    Parameters  Default  Description

    ALPHA       0.05     Learning Rate (step size)
    EPOCHS      20000    Number of training iterations

**Example Usage:**
```bash
# Train with custom hyperparameters
make train ALPHA=0.01 EPOCHS=50000

# Predict a value
make predict
Enter a mileage (km): 100000
Estimated price: 6123.45 euros
```

***📂 Project Structureft_linear_regression/***
```bash
│
├── train.py                # Trains the model parameters θ₀ and θ₁
├── predict.py              # Predicts a price based on a given mileage
├── data.csv                # Training dataset
├── thetas.json             # Stores the learned parameters
│
├── src/
│   └── linear_regression/
│       ├── __init__.py
│       └── model.py        # Core logic (data I/O, gradient descent, prediction)
│
├── bonus/
│   ├── __init__.py
│   ├── plot.py             # Generates a scatter plot with the regression line
│   └── precision.py        # Computes R², MSE, and RMSE metrics
│
├── Dockerfile              # Environment definition
└── Makefile                # Commands for build, clean, re, and bonus
```
## 🧠 Algorithm Summary

Hypothesis Function:
```bash
ŷ = θ₀ + θ₁ * x
```

Where ŷ is the predicted price, x is the mileage, and θ₀ (intercept) and θ₁ (slope) are the model parameters.

Batch Gradient Descent:
```bash
θ₀ := θ₀ - α * (1/m) * Σ(ŷ - y)
θ₁ := θ₁ - α * (1/m) * Σ(ŷ - y) * x
```

Where:
- α is the learning rate
- m is the number of training samples
- y is the actual price

The goal is to find θ₀ and θ₁ that minimize the Mean Squared Error (MSE).

Feature Standardization:
To improve numerical stability and speed up convergence, the mileage feature (x) is standardized before training using the formula:
```bash
z = (x - μ) / σ
```

Where μ is the mean of all mileage values and σ is the standard deviation.
After training, the final parameters θ₀ and θ₁ are converted back to original units for real-world predictions:
```bash
θ₁ = b / σ
θ₀ = a - (b * μ / σ)
```
---

## ✨ Bonus Programs

```bash
bonus/plot.py:
```
Generates a scatter plot of the training data and overlays the regression line.
The output is saved as ```regression_plot.png```.

```bash
bonus/precision.py:
```
Computes the model’s performance using three key metrics:

- Coefficient of Determination (R²): Measures how much variance in the price can be explained by mileage.
  R² = 1 means perfect fit; R² = 0 means no better than predicting the mean; R² < 0 means worse than the mean.

- Mean Squared Error (MSE): Average of squared differences between predicted and actual values.

- Root Mean Squared Error (RMSE): The square root of MSE, giving the error in euros.

Typical Results After Training:
```bash
R² score ≈ 0.73
MSE      ≈ 445000
RMSE     ≈ 667€
```

---

## 🛠️ Makefile Commands

```bash
make              -> Train the model and save thetas.json
make train        -> Train the model with custom parameters (ALPHA= , EPOCHS=)
make predict      -> Run the interactive price predictor
make bonus        -> Run both bonus scripts (plot and precision)
make clean        -> Remove caches, __pycache__, and generated images
make fclean       -> Perform a full clean, also removing thetas.json
make re           -> Run fclean then retrain from scratch
make lint         -> Run a static code check using Pyflakes
```

---

## 🔍 Troubleshooting

Problem: ```θ₀``` or ```θ₁``` are NaN after training
Cause: The learning rate ```α``` is too high, causing divergence.
Fix: Reduce ```α``` (e.g., try 0.01 or 0.001).

Problem: R² score is negative
Cause: The model has not converged and performs worse than the mean baseline.
Fix: Increase the number of ```epochs``` or reduce ```α```.

Problem: ```matplotlib``` not found
Cause: Dependencies not installed.
Fix: Run ```pip install -r requirements.txt```.

---

## 📜 License and Credits

This is an educational project for the 42 school curriculum.
Author: William Nguyen
The model is built entirely with Python’s standard library. No external ML frameworks were used, and matplotlib is used only for bonus visualizations.
