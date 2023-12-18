import numpy as np

A_2= np.array([
        [-3, 8, 1],
        [2, 2, -1],
        [-5, 6, 2]
    ], dtype=np.dtype(float))

d_2 = np.linalg.det(A_2)

print("Determinant of matrix A_2:", (d_2))

