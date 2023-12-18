a=("Testing Matix Solution")
print (a)

import numpy as np

A = np.array([
    [-1,3],
    [3,2]
], dtype=np.dtype(float))

b = np.array([7,1], dtype=np.dtype(float))

print("matrix A:")
print(A)
print("\nArray b:")
print(b)

print(f"Shape of A: {A.shape}")
print(f"Shape of b: {b.shape}")

x=np.linalg.solve(A,b)

print(f"Solution: {x}")

