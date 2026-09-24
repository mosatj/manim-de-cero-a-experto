import numpy as np


def R(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]])


a, b = 0.7, 1.9
print("R(a) R(b) = R(a+b):", np.allclose(R(a) @ R(b), R(a + b)))
print("conmutan:", np.allclose(R(a) @ R(b), R(b) @ R(a)))
print("R^T = R^-1:", np.allclose(R(a).T, np.linalg.inv(R(a))))
print("det R = 1:", np.isclose(np.linalg.det(R(a)), 1))
doce = np.linalg.matrix_power(R(np.pi / 6), 12)    # R elevada a 12
print("12 giros de 30° = identidad:", np.allclose(doce, np.eye(2)))
