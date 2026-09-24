import math


class Punto:
    """Un punto del plano."""

    def __init__(self, x, y):       # se ejecuta al crear el objeto
        self.x = x                 # atributos: los datos del objeto
        self.y = y

    # Método: algo que el objeto sabe hacer
    def distancia_al_origen(self):
        return math.sqrt(self.x**2 + self.y**2)

    def desplazar(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


p = Punto(3, 4)          # p es un objeto (una instancia) de Punto
q = Punto(-1, 0)         # q es otro objeto, independiente de p
print("p =", (p.x, p.y), " distancia:", p.distancia_al_origen())
p.desplazar(1, 1)
print("p =", (p.x, p.y), " q =", (q.x, q.y))
print(type(p), isinstance(q, Punto))
