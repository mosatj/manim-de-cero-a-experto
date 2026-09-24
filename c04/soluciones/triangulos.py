# Propuesto: triángulos que se forman con 5 puntos
from itertools import combinations

puntos = [(0, 0), (2, 0), (4, 0), (1, 2), (3, 2)]


def area_doble(p, q, r):
    """Dos veces el área (con signo) del triángulo pqr."""
    return ((q[0] - p[0]) * (r[1] - p[1])
            - (r[0] - p[0]) * (q[1] - p[1]))


ternas = list(combinations(puntos, 3))
validos = [t for t in ternas if area_doble(*t) != 0]
print("Ternas posibles:", len(ternas))
print("Triángulos de verdad:", len(validos))
print("Alineados:", [t for t in ternas if area_doble(*t) == 0])
