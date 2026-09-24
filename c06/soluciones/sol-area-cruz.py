import numpy as np


def area_triangulo(a, b, c):
    """Mitad de la norma del producto vectorial de dos lados."""
    a, b, c = map(np.asarray, (a, b, c))
    return np.linalg.norm(np.cross(b - a, c - a)) / 2


print(area_triangulo([0, 0, 0], [4, 0, 0], [0, 3, 0]))   # 6
print(area_triangulo([1, 1, 0], [3, 2, 0], [2, 4, 0]))   # 2.5
print(area_triangulo([1, 0, 0], [0, 1, 0], [0, 0, 1]))   # en 3D
print(area_triangulo([0, 0, 0], [1, 1, 0], [2, 2, 0]))   # alineados
