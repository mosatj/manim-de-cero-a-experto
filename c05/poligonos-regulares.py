import math


class PoligonoRegular:
    nombre = "polígono"

    def __init__(self, n, lado):
        self.n, self.lado = n, lado

    def perimetro(self):
        return self.n * self.lado

    def apotema(self):
        return self.lado / (2 * math.tan(math.pi / self.n))

    def area(self):                      # válida para todo n
        return self.perimetro() * self.apotema() / 2

    def __str__(self):
        return (f"{self.nombre:<10} n = {self.n:<4} "
               f"P = {self.perimetro():.2f}, A = {self.area():.3f}")


class TrianguloEquilatero(PoligonoRegular):
    nombre = "triángulo"

    def __init__(self, lado):
        super().__init__(3, lado)

    def area(self):                      # fórmula propia (y exacta)
        return math.sqrt(3) / 4 * self.lado**2


class Hexagono(PoligonoRegular):
    nombre = "hexágono"

    def __init__(self, lado):
        super().__init__(6, lado)


figuras = [Hexagono(2), TrianguloEquilatero(2),
           PoligonoRegular(4, 2), PoligonoRegular(1000, 0.00628)]
for f in sorted(figuras, key=lambda f: f.area()):
    print(f)
t = TrianguloEquilatero(2)
print("comprobación:", round(t.area(), 6),
      round(PoligonoRegular.area(t), 6))
