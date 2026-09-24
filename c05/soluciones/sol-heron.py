import math


class Figura:
    def area(self):
        raise NotImplementedError

    def __repr__(self):
        return f"{type(self).__name__}(área={self.area():.2f})"


class Circulo(Figura):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r**2


class Rectangulo(Figura):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def area(self):
        return self.a * self.b


class Triangulo(Figura):
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("no cumple la desigualdad triangular")
        self.lados = (a, b, c)

    def area(self):                      # fórmula de Herón
        a, b, c = self.lados
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


figuras = [Rectangulo(2, 5), Triangulo(3, 4, 5), Circulo(1.5)]
print(sorted(figuras, key=lambda f: f.area()))
print("mayor:", max(figuras, key=lambda f: f.area()))
