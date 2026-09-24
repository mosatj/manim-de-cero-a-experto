# Vértices de un polígono regular inscrito en una circunferencia
import math


def vertices_poligono(n, radio=1.0, giro=0.0):
    """Lista de los n vértices (x, y), desde el ángulo giro."""
    vertices = []
    for k in range(n):
        angulo = giro + 2 * math.pi * k / n
        x = round(radio * math.cos(angulo), 3) + 0.0  # evita -0.0
        y = round(radio * math.sin(angulo), 3) + 0.0
        vertices.append((x, y))
    return vertices


print(vertices_poligono(4))
print(vertices_poligono(3, radio=2, giro=math.pi / 2))
hexagono = vertices_poligono(6)
lado = math.dist(hexagono[0], hexagono[1])
print(f"Hexágono: {len(hexagono)} vértices, lado = {lado:.3f}")
