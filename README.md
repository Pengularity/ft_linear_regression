ft_linear_regression (42)

A clean, single-variable linear regression trained with batch gradient descent.
It predicts car prices from mileage using only Python’s standard library.

Subject: docs/ft_linear_regression.subject.pdf
Goal: implement linear regression from scratch — no NumPy, no ML libraries.

⸻

SETUP AND QUICK START
	1.	Create and activate a virtual environment:
python3 -m venv .venv
source .venv/bin/activate
	2.	Install dependencies:
pip install -r requirements.txt
	3.	Train the model:
make
	4.	Predict a price:
make predict
	5.	Run bonus visualizations and metrics:
make bonus

Example:
python3 train.py –alpha 0.05 –epochs 20000
python3 predict.py
Enter a mileage (km): 100000
Estimated price: 6123.45 euros

⸻

PROJECT STRUCTURE

ft_linear_regression/
│
├── train.py                -> trains θ₀, θ₁
├── predict.py              -> predict price
├── data.csv                -> training dataset
├── thetas.json             -> learned parameters
│
├── src/
│   └── linear_regression/
│       ├── init.py
│       └── model.py       -> core logic (IO, gradient descent, predict)
│
├── bonus/
│   ├── init.py
│   ├── plot.py            -> scatter plot and regression line
│   └── precision.py       -> computes R², MSE, RMSE metrics
│
└── Makefile                -> build, clean, re, bonus commands

⸻

ALGORITHM SUMMARY

Hypothesis:
y_hat = θ₀ + θ₁ * x

Batch Gradient Descent (simultaneous updates):
θ₀ := θ₀ - α * (1/m) * Σ(y_hat - y)
θ₁ := θ₁ - α * (1/m) * Σ(y_hat - y) * x

Feature Standardization:
To improve numerical stability, the mileage feature is standardized before training.

z = (x - μ) / σ
θ₁ = b / σ
θ₀ = a - (b * μ / σ)

Where:
μ = mean of mileage values
σ = standard deviation of mileage values
a and b are parameters learned on the standardized data.

⸻

BONUS PROGRAMS

bonus/plot.py
Draws the regression line and the training data points.
Output: regression_plot.png

bonus/precision.py
Computes the model’s performance metrics:
	•	R² (coefficient of determination)
	•	MSE (mean squared error)
	•	RMSE (root mean squared error)

Typical results after proper training:
R² ≈ 0.73
MSE ≈ 445000
RMSE ≈ 667 euros

⸻

MAKEFILE COMMANDS

make              -> Train the model
make predict      -> Run the predictor
make bonus        -> Run the bonus scripts (plot + precision)
make clean        -> Remove caches, pycache, and images
make fclean       -> Full clean, including thetas.json
make re           -> fclean + rebuild (train again)
make lint         -> Run static check using pyflakes (optional)

⸻

TROUBLESHOOTING

Problem: θ₀ or θ₁ are NaN
Cause: Learning rate α is too high.
Fix: Reduce α (for example, 0.01 or 0.001).

Problem: R² < 0
Cause: The model is worse than predicting the mean (not converged).
Fix: Increase epochs or lower α.

Problem: ModuleNotFoundError: src
Cause: Running from the wrong directory.
Fix: Run from the project root with
python3 -m bonus.plot
or use the Makefile target make bonus.

Problem: matplotlib not found
Fix: Install dependencies with
pip install -r requirements.txt

⸻

DESIGN CHOICES
	•	100% pure Python, no external machine learning libraries.
	•	Modular design: CLI scripts (train.py, predict.py) separated from logic (src/linear_regression/model.py).
	•	Feature standardization for faster and more stable convergence.
	•	Model parameters stored in thetas.json (θ₀ and θ₁ in euros per kilometer).
	•	42-style Makefile containing all mandatory targets: all, clean, fclean, re, bonus.

⸻

PRECISION METRICS

R² (Coefficient of Determination):
Measures how much better the model predicts compared to simply guessing the mean.
R² = 1 means perfect fit.
R² = 0 means as good as predicting the mean.
R² < 0 means worse than predicting the mean.

MSE (Mean Squared Error):
Average of the squared prediction errors (in euros²).

RMSE (Root Mean Squared Error):
Square root of MSE, gives the average error in euros.

Example interpretation:
R² = 0.73 → good linear correlation.
RMSE = 667 → on average, the model is off by 667 euros.

⸻

LICENSE AND CREDITS

Educational project for 42.
Author: [Your name or 42 login].
No external ML frameworks were used — only Python’s standard library and matplotlib for the bonus visualizations.