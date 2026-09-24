import numpy as np


def a_rgb(hexa):
    hexa = hexa.lstrip("#")
    return np.array([int(hexa[i:i + 2], 16) for i in (0, 2, 4)])


def a_hex(rgb):
    r, g, b = np.round(rgb).astype(int)
    return f"#{r:02X}{g:02X}{b:02X}"


def gradiente(c1, c2, n):
    t = np.linspace(0, 1, n)[:, None]       # columna de n valores
    colores = (1 - t) * a_rgb(c1) + t * a_rgb(c2)
    return [a_hex(c) for c in colores]


print(gradiente("#0B2A3C", "#E9F2F7", 5))
print(gradiente("#2A8FBD", "#B3174A", 3))
