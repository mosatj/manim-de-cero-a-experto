"""Funciones geométricas sencillas (módulo de ejemplo, cap. 4)."""
import math

PI = math.pi


def area_circulo(radio):
    """Área de un círculo de radio dado."""
    return PI * radio ** 2


def distancia(p, q):
    """Distancia entre los puntos p = (x1, y1) y q = (x2, y2)."""
    return math.hypot(q[0] - p[0], q[1] - p[1])


if __name__ == "__main__":
    # Solo se ejecuta al lanzar este archivo, no al importarlo
    print("Probando geometria.py ...")
    print(area_circulo(1), distancia((0, 0), (3, 4)))
