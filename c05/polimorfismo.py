import math


class Circulo:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r**2


class Rectangulo:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def area(self):
        return self.a * self.b


class Triangulo:
    def __init__(self, base, altura):
        self.base, self.altura = base, altura

    def area(self):
        return self.base * self.altura / 2


# Una misma llamada, f.area(), y tres comportamientos distintos
figuras = [Circulo(1), Rectangulo(2, 3), Triangulo(4, 5)]
for f in figuras:
    print(f"{type(f).__name__:<10} → {f.area():6.2f}")
print("total:", round(sum(f.area() for f in figuras), 2))
