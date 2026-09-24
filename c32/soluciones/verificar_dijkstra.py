import sys
from itertools import permutations
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent  # codigo/c32
sys.path.insert(0, str(RAIZ / "proyecto2"))
from datos_grafo import ARISTAS, VERTICES, ORIGEN
from dijkstra import pasos_dijkstra


def peso(u, v):
    return ARISTAS.get((u, v), ARISTAS.get((v, u)))


def fuerza_bruta(destino):
    """Prueba todos los caminos simples: lento, pero seguro."""
    mejor = float("inf")
    otros = [v for v in VERTICES if v not in (ORIGEN, destino)]
    for largo in range(len(otros) + 1):
        for medio in permutations(otros, largo):
            camino = [ORIGEN, *medio, destino]
            tramos = [
                peso(u, v) for u, v in zip(camino, camino[1:])
            ]
            if None not in tramos:
                mejor = min(mejor, sum(tramos))
    return mejor


*_, (_, dist, _) = pasos_dijkstra(VERTICES, ARISTAS, ORIGEN)
for v in VERTICES:
    if v != ORIGEN:
        assert dist[v] == fuerza_bruta(v), v
print(
    len(VERTICES) - 1, "distancias coinciden con la fuerza bruta."
)
