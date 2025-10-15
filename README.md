# ft_linear_regression (42)

A minimal, clean implementation of a **single-variable linear regression** trained with **batch gradient descent**.
It follows the 42 subject constraints: one predictor (mileage), hypothesis `θ0 + θ1 * mileage`, **simultaneous** updates of the parameters, and a separate predictor program.

- 📄 Subject: [Subject (PDF)](docs/ft_linear_regression.subject.pdf)

---

## What this repo contains

Feature Scaling: Standardization
To ensure stable and efficient convergence of the gradient descent algorithm, this project uses standardization (specifically Z-score normalization) on the input feature (km).

The Problem: Why Scale Features?
Gradient descent optimizes parameters by iteratively moving in the direction of the steepest descent of the cost function. The "shape" of the cost function is highly sensitive to the scale of the input features.

When features have vastly different scales (e.g., mileage in the hundreds of thousands vs. a target price in the thousands), the cost function becomes a steep, narrow ellipse. This forces the algorithm to "zig-zag" down the slope with a small learning rate, leading to slow or unstable convergence.

By standardizing the km feature, we reshape the cost function's contours to be more circular. This allows gradient descent to take a more direct and efficient path to the optimal minimum.

The Two-Phase Process
The implementation involves two critical phases: standardization before training and de-standardization after training.

1. Standardization (Pre-Training)
We transform the original mileage feature x (in km) into a standardized feature z using the formula:

z= 
σ
x−μ
​
 
Where:

μ (mu) is the mean of all mileage values.

σ (sigma) is the standard deviation of all mileage values.

This transformation gives the new feature z a mean of 0 and a standard deviation of 1. The script then trains the model on these standardized z values, learning the relationship:

y≈a+b⋅z
2. De-standardization (Post-Training)
The training process yields parameters a and b that work for the standardized feature z. To make predictions using the original mileage x, we must convert a and b back into θ₀ and θ₁ for the final model:

y≈θ 
0
​
 +θ 
1
​
 ⋅x
We derive the conversion by substituting the standardization formula back into our learned model:

Start with the learned model:

y=a+b⋅z
Substitute the definition of z:

y=a+b⋅( 
σ
x−μ
​
 )
Distribute the terms and rearrange to match the form y=θ 
0
​
 +θ 
1
​
 ⋅x:

y=a+ 
σ
b
​
 x− 
σ
bμ
​
 
y= 
θ 
0
​
 

(a− 
σ
bμ
​
 )
​
 
​
 + 
θ 
1
​
 

( 
σ
b
​
 )
​
 
​
 x
This gives us the exact formulas to convert our learned parameters a and b back to the final parameters θ₀ and θ₁:

θ 
1
​
 = 
σ
b
​
 

θ 
0
​
 =a− 
σ
bμ
​
