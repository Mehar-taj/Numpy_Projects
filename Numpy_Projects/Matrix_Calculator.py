import numpy as np

matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix 1:\n", matrix1)

print("\nMatrix 2:\n", matrix2)

print("\nMatrix Addition:\n", matrix1 + matrix2)

print("\nMatrix Subtraction:\n", matrix1 - matrix2)

print("\nMatrix Multiplication:\n", matrix1 @ matrix2)

print("\nMatrix Transpose:\n", matrix1.T)

print("\nMatrix Determinant:\n", np.linalg.det(matrix1))

print("\nMatrix Inverse:\n", np.linalg.inv(matrix1))