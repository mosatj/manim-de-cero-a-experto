class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho, self.alto = ancho, alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

    def es_cuadrado(self):
        return self.ancho == self.alto

    def __str__(self):
        return f"Rectángulo {self.ancho} × {self.alto}"


for r in [Rectangulo(3, 2), Rectangulo(4, 4)]:
    print(r, "| área:", r.area(), "| perímetro:", r.perimetro(),
          "| ¿cuadrado?", r.es_cuadrado())
