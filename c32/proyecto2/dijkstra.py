# El algoritmo como generador: no dibuja, solo anuncia qué ocurre
import heapq


def vecinos(aristas, u):
    for (x, y), peso in aristas.items():
        if x == u:
            yield y, peso
        elif y == u:
            yield x, peso


def pasos_dijkstra(vertices, aristas, origen):
    """Produce eventos ('fijar', u, d), ('relajar', u, v, d, mejora)
    y, al terminar, ('fin', distancias, previos)."""
    dist = {v: float("inf") for v in vertices}
    previo = {v: None for v in vertices}
    dist[origen] = 0
    cola, fijados = [(0, origen)], set()
    while cola:
        d, u = heapq.heappop(cola)
        if u in fijados:
            continue  # entrada vieja de la cola
        fijados.add(u)
        yield ("fijar", u, d)
        for v, peso in vecinos(aristas, u):
            if v in fijados:
                continue
            nueva = d + peso
            mejora = nueva < dist[v]
            yield ("relajar", u, v, nueva, mejora)
            if mejora:
                dist[v], previo[v] = nueva, u
                heapq.heappush(cola, (nueva, v))
    yield ("fin", dist, previo)
