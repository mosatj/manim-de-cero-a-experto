import math


class Tortuga:
    def __init__(self):
        self.x, self.y, self.rumbo = 0.0, 0.0, 0.0  # rumbo: grados
        self.camino = [(0.0, 0.0)]

    def avanzar(self, d):
        self.x += d * math.cos(math.radians(self.rumbo))
        self.y += d * math.sin(math.radians(self.rumbo))
        # redondeamos (y + 0.0 convierte -0.0 en 0.0)
        self.camino.append((round(self.x, 6) + 0.0,
                            round(self.y, 6) + 0.0))
        return self

    def girar(self, grados):
        self.rumbo = (self.rumbo + grados) % 360
        return self


t = Tortuga()
for _ in range(4):
    t.avanzar(2).girar(90)          # encadenamiento: un cuadrado
print("camino:", t.camino)
print("¿volvió al inicio?", t.camino[-1] == (0.0, 0.0))
