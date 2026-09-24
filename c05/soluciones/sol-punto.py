import math


class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.x, self.y = x, y

    def distancia_a(self, otro):
        return math.hypot(self.x - otro.x, self.y - otro.y)

    def punto_medio(self, otro):         # devuelve un objeto NUEVO
        return Punto((self.x + otro.x) / 2, (self.y + otro.y) / 2)

    def __str__(self):
        return f"({self.x}, {self.y})"


a, b = Punto(1, 2), Punto(7, 10)
print("distancia:", a.distancia_a(b), "| medio:", a.punto_medio(b))
print("a no cambió:", a)
