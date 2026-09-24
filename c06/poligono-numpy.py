import numpy as np


def poligono_regular(n, radio=1.0):
    """Vértices (n, 3) de un n-ágono regular inscrito."""
    ang = np.pi / 2 + 2 * np.pi * np.arange(n) / n
    x, y = radio * np.cos(ang), radio * np.sin(ang)
    return np.column_stack([x, y, np.zeros(n)])


def area_lazada(v):
    """Fórmula del cordón (shoelace) para un polígono simple."""
    x, y = v[:, 0], v[:, 1]
    x_sig, y_sig = np.roll(x, -1), np.roll(y, -1)  # el siguiente
    return 0.5 * abs(np.dot(x, y_sig) - np.dot(y, x_sig))


for n in (3, 4, 6, 12, 100):
    v = poligono_regular(n)
    exacta = n / 2 * np.sin(2 * np.pi / n)
    lados = np.linalg.norm(v - np.roll(v, -1, axis=0), axis=1)
    print(f"n = {n:>3}: área {area_lazada(v):.5f} "
          f"(exacta {exacta:.5f})  perímetro {lados.sum():.4f}")
