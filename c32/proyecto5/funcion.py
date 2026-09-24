# La matemática de la lección, separada de la animación y comprobada
import numpy as np


def f(x, y):
    return 4 - x**2 / 2 - y**2


def fx(x, y):  # derivada parcial respecto de x
    return -x


def fy(x, y):  # derivada parcial respecto de y
    return -2 * y


def semiejes(c):
    """Curva de nivel f = c: elipse x^2/(2(4-c)) + y^2/(4-c) = 1."""
    return np.sqrt(2 * (4 - c)), np.sqrt(4 - c)


PUNTO = (1.0, 0.8)  # donde se calculan las parciales
NIVELES = [0.5, 1.5, 2.5, 3.5]

if __name__ == "__main__":
    a, b = PUNTO
    h = 1e-6
    print(f"f{PUNTO} = {f(a, b):.4f}")
    print(
        f"fx: fórmula {fx(a, b):.4f}   numérica "
        f"{(f(a + h, b) - f(a - h, b)) / (2 * h):.4f}"
    )
    print(
        f"fy: fórmula {fy(a, b):.4f}   numérica "
        f"{(f(a, b + h) - f(a, b - h)) / (2 * h):.4f}"
    )
    for c in NIVELES:
        sx, sy = semiejes(c)
        x, y = (
            sx * np.cos(0.7),
            sy * np.sin(0.7),
        )  # un punto cualquiera
        print(f"nivel {c}: f en la elipse = {f(x, y):.4f}")
