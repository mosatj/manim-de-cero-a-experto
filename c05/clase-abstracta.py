import math
from abc import ABC, abstractmethod


class Figura(ABC):
    """Clase abstracta: define el contrato, no se instancia."""

    @abstractmethod
    def area(self):
        """Toda figura concreta DEBE implementarlo."""

    def informe(self):                  # método concreto, se hereda
        return f"{type(self).__name__}: {self.area():.3f}"


class Circulo(Figura):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r**2


class Nube(Figura):                      # olvidó implementar area()
    pass


print(Circulo(1).informe())
for clase in (Figura, Nube):
    try:
        clase()
    except TypeError as error:
        print("TypeError:", error)
