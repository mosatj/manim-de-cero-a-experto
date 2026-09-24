# Prueba del modelo antes de animarlo: ¿los eventos son correctos?
from datos_grafo import VERTICES, ARISTAS, ORIGEN
from dijkstra import pasos_dijkstra

for evento in pasos_dijkstra(VERTICES, ARISTAS, ORIGEN):
    if evento[0] == "fijar":
        print(f"fijar {evento[1]} con distancia {evento[2]}")
    elif evento[0] == "relajar":
        _, u, v, d, mejora = evento
        print(
            f"   {u}->{v}: {d:2d}",
            "mejora" if mejora else "no mejora",
        )
    else:
        _, dist, previo = evento
        print("distancias:", dist)
        print("previos:   ", previo)
