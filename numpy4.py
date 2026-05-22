import numpy as np

# Create two arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])

print("First Array :", arr1)
print("Second Array:", arr2)

# Addition
add = arr1 + arr2
print("\nAddition:", add)

# Multiplication
multiply = arr1 * arr2
print("Multiplication:", multiply)

# Average of first array
average = np.mean(arr1)
print("\nAverage of First Array:", average)

# Find minimum and maximum
minimum = np.min(arr1)
maximum = np.max(arr1)

print("Minimum Value:", minimum)
print("Maximum Value:", maximum)

# Reshape array into matrix
matrix = arr1.reshape(5, 1)

print("\nReshaped Matrix:\n", matrix)