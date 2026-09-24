import numpy as np

A = np.array([[2, 1],
              [0, 1]])
v = np.array([1, 3])
print("A @ v =", A @ v)                # matriz por vector
print("A * v =", A * v, " (¡no es lo mismo: elemento a elemento!)")
B = np.array([[0, -1],
              [1, 0]])
print("A @ B =\n", A @ B)
print("B @ A =\n", B @ A)              # el producto no conmuta
print("A^T =\n", A.T)
print("det(A) =", np.linalg.det(A))
print("inversa:\n", np.linalg.inv(A))
print("A @ inv(A) =\n", A @ np.linalg.inv(A))
