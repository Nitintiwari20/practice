import numpy as np

# Create a 3x3 matrix with random integers
matrix = np.random.randint(1, 50, size=(3, 3))

print("Original Matrix:\n", matrix)

# Matrix transpose
transpose_matrix = matrix.T
print("\nTranspose Matrix:\n", transpose_matrix)

# Matrix multiplication
result = np.dot(matrix, transpose_matrix)
print("\nMatrix Multiplication:\n", result)

# Find determinant
determinant = np.linalg.det(matrix)
print("\nDeterminant:", determinant)

# Find eigenvalues
eigenvalues = np.linalg.eigvals(matrix)
print("\nEigenvalues:\n", eigenvalues)

# Find row-wise sum
row_sum = np.sum(matrix, axis=1)
print("\nRow-wise Sum:", row_sum)

# Find column-wise sum
col_sum = np.sum(matrix, axis=0)
print("\nColumn-wise Sum:", col_sum)