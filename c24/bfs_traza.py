from collections import deque

# Lista de adyacencia: cada vértice con sus vecinos (en orden)
adyacencia = {
    "A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "E"],
    "D": ["B", "F"], "E": ["B", "C", "F", "G"],
    "F": ["D", "E", "H"], "G": ["E", "H"], "H": ["F", "G"],
}


def bfs(adyacencia, inicio):
    distancia = {inicio: 0}
    cola = deque([inicio])
    while cola:
        u = cola.popleft()               # FIFO: sale el más antiguo
        nuevos = []
        for v in adyacencia[u]:
            if v not in distancia:       # primera vez que lo veo
                distancia[v] = distancia[u] + 1
                cola.append(v)
                nuevos.append(v)
        print(f"saco {u} (d={distancia[u]}), descubro {nuevos}, "
              f"cola = {list(cola)}")
    return distancia


print(bfs(adyacencia, "A"))
