import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent  # codigo/c32
sys.path.insert(0, str(RAIZ / "proyecto2"))
from datos_grafo import ARISTAS, VERTICES
from dijkstra import pasos_dijkstra

# Nuevo vértice G unido a C y a F; el origen pasa a ser F
vertices = VERTICES + ["G"]
aristas = dict(ARISTAS)
aristas[("C", "G")] = 1
aristas[("F", "G")] = 4
*_, fin = pasos_dijkstra(vertices, aristas, "F")
_, dist, previo = fin
for v in vertices:
    camino, u = [], v
    while u is not None:  # se reconstruye hacia atrás
        camino.append(u)
        u = previo[u]
    print(
        f"{v}: {dist[v]:2d}  camino {' -> '.join(reversed(camino))}"
    )
