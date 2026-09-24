import math


class Punto:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def distancia(self, otro):
        return math.hypot(self.x - otro.x, self.y - otro.y)


class Triangulo:
    """Un triángulo TIENE tres puntos: composición."""

    def __init__(self, a, b, c):
        self.vertices = [a, b, c]

    def perimetro(self):
        a, b, c = self.vertices
        return a.distancia(b) + b.distancia(c) + c.distancia(a)

    def desplazar(self, dx, dy):         # delega en sus partes
        for v in self.vertices:
            v.x, v.y = v.x + dx, v.y + dy


t = Triangulo(Punto(0, 0), Punto(3, 0), Punto(0, 4))
print("perímetro:", t.perimetro())
t.desplazar(10, 10)
print("vértices:", [(v.x, v.y) for v in t.vertices])
print("perímetro tras moverlo:", t.perimetro())
