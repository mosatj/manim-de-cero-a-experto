import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, r):
        if r <= 0:
            raise ValueError("el radio debe ser positivo")
        self._radio = r

    @property
    def diametro(self):
        return 2 * self._radio

    @diametro.setter
    def diametro(self, d):
        self.radio = d / 2               # reutiliza la validación

    @property
    def area(self):
        return math.pi * self._radio**2


c = Circulo(1)
c.diametro = 10
print("radio:", c.radio, "| diámetro:", c.diametro,
      "| área:", round(c.area, 2))
try:
    c.area = 5
except AttributeError as e:
    print("AttributeError:", e)
