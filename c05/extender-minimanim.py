import math
from minimanim import *


class Estrella(Figura):                  # una figura nueva...
    def __init__(self, puntas=5, radio=2.0, color="verde"):
        self.puntas, self.radio = puntas, radio
        super().__init__(color=color)

    def generar_puntos(self):        # ...solo aporta su geometría
        n = 2 * self.puntas
        self.puntos = []
        for k in range(n):
            r = self.radio if k % 2 == 0 else 0.4 * self.radio
            angulo = math.pi / 2 + 2 * math.pi * k / n
            self.puntos.append((r * math.cos(angulo),
                                r * math.sin(angulo)))


class Girar(Animacion):                  # una animación nueva
    def __init__(self, figura, angulo, **opciones):
        super().__init__(figura, **opciones)
        self.angulo = angulo

    def iniciar(self):
        self.cx, self.cy = self.figura.centro()
        self.inicio = [f.puntos[:] for f in self.figura.familia()]

    def interpolar(self, alfa):
        a = alfa * self.angulo
        co, se = math.cos(a), math.sin(a)
        cx, cy = self.cx, self.cy
        for f, pts in zip(self.figura.familia(), self.inicio):
            f.puntos = [(cx + co * (x - cx) - se * (y - cy),
                         cy + se * (x - cx) + co * (y - cy))
                        for x, y in pts]


class EstrellaQueGira(Escena):
    def construir(self):
        estrella = Estrella(radio=2.8).desplazar(-3, 0)
        luna = Circulo(radio=1, color="azul").desplazar(2, 0)
        self.reproducir(Crear(estrella), Crear(luna))
        self.reproducir(Girar(estrella, math.pi / 5),   # 36 grados
                        Desplazar(luna, 2, 0, duracion=2))


EstrellaQueGira().render()
