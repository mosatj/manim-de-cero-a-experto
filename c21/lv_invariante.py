import numpy as np
from metodos_edo import euler, heun, rk4, resolver

A, B, G, D = 2 / 3, 4 / 3, 1.0, 1.0


def F(t, p):
    x, y = p
    return np.array([A * x - B * x * y, D * x * y - G * y])


def V(p):                                   # cantidad conservada
    x, y = p
    return D * x - G * np.log(x) + B * y - A * np.log(y)


p0 = np.array([1.0, 1.5])
print(f"V inicial = {V(p0):.6f}")
for metodo in (euler, heun, rk4):
    _, datos = resolver(metodo, F, 0, p0, 0.05, 1000)   # t = 50
    deriva = V(datos[-1]) - V(p0)
    print(f"{metodo.__name__:5s}: V(50) = {V(datos[-1]):.6f}"
          f"  deriva = {deriva:+.2e}")
