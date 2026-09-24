class Cuadrado:
    def __init__(self, lado):
        self.lado = lado         # error 2: faltaba «self.»

    def area(self):          # error 1: faltaba el parámetro self
        return self.lado**2


c = Cuadrado(3)
print(c.area())          # error 3: se llamaba Cuadrado.area()
