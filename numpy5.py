# NumPy Code for Machine Learning Basics

import numpy as np

# 1. Create Dataset
# Features (Hours studied, Sleep hours)
X = np.array([
    [2, 7],
    [4, 6],
    [6, 5],
    [8, 4],
    [10, 3]
])

# Target values (Marks)
y = np.array([40, 50, 60, 70, 80])

print("Features Dataset:\n", X)
print("\nTarget Dataset:\n", y)

# 2. Shape of Dataset

print("\nShape of X:", X.shape)
print("Shape of y:", y.shape)

# 3. Mean and Standard Deviation

mean = np.mean(X, axis=0)
std = np.std(X, axis=0)

print("\nMean:", mean)
print("Standard Deviation:", std)

# 4. Normalize Data
# Formula = (X - mean) / std

X_normalized = (X - mean) / std

print("\nNormalized Data:\n", X_normalized)

# 5. Matrix Operations

# Transpose of matrix
X_transpose = X.T

print("\nTranspose Matrix:\n", X_transpose)

# Matrix multiplication
result = np.dot(X_transpose, X)

print("\nDot Product:\n", result)

# 6. Random Weights for ML

weights = np.random.rand(2)

print("\nRandom Weights:\n", weights)

# 7. Prediction using Dot Product

predictions = np.dot(X, weights)

print("\nPredictions:\n", predictions)

# 8. Loss Calculation

loss = np.mean((predictions - y) ** 2)

print("\nMean Squared Error Loss:\n", loss)