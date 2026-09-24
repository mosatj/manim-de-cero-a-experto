import math


class Figura:
    def __init__(self, color="blanco"):
        self.color = color

    def area(self):
        return 0.0

    def describir(self):                 # se hereda tal cual
        nombre = type(self).__name__
        return f"{nombre} {self.color} de área {self.area():.2f}"


class Circulo(Figura):
    def __init__(self, radio, color="rojo"):
        super().__init__(color)          # que Figura haga su parte
        self.radio = radio

    def area(self):                      # sobrescribe Figura.area
        return math.pi * self.radio**2


class Rectangulo(Figura):
    def __init__(self, ancho, alto, color="blanco"):
        super().__init__(color)
        self.ancho, self.alto = ancho, alto

    def area(self):
        return self.ancho * self.alto


class Cuadrado(Rectangulo):       # un cuadrado ES UN rectángulo
    def __init__(self, lado, color="azul"):
        super().__init__(lado, lado, color)


for f in [Circulo(1), Rectangulo(3, 2), Cuadrado(2)]:
    print(f.describir())
c = Cuadrado(5)
print(isinstance(c, Rectangulo), isinstance(c, Circulo),
      issubclass(Cuadrado, Figura))
print([k.__name__ for k in Cuadrado.mro()])
