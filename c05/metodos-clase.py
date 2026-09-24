import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    @classmethod
    def desde_diametro(cls, d):      # recibe la CLASE, no un objeto
        return cls(d / 2)

    @classmethod
    def desde_area(cls, area):
        return cls(math.sqrt(area / math.pi))

    @staticmethod
    def es_radio_valido(r):          # no recibe ni clase ni objeto
        return isinstance(r, (int, float)) and r > 0

    def __repr__(self):
        return f"Circulo(radio={self.radio:.3f})"


print(Circulo.desde_diametro(10))
print(Circulo.desde_area(math.pi * 9))
print(Circulo.es_radio_valido(-2), Circulo.es_radio_valido(2.5))
