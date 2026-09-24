import sys
sys.path.insert(0, "..")            # para encontrar minimanim.py
from minimanim import *


class Triangulo(Figura):
    def __init__(self, lado=3.0, color="verde"):
        self.lado = lado
        super().__init__(color=color)

    def generar_puntos(self):
        h = self.lado * 3**0.5 / 2
        a = self.lado / 2
        self.puntos = [(-a, -h / 3), (a, -h / 3), (0, 2 * h / 3)]


class CambiarColor(Animacion):
    def __init__(self, figura, color, **opciones):
        super().__init__(figura, **opciones)
        self.color_final = color

    def iniciar(self):
        self.color_inicial = self.figura.color

    def interpolar(self, alfa):     # sin mezcla: salta a la mitad
        final = alfa >= 0.5
        color = self.color_final if final else self.color_inicial
        self.figura.pintar(color)


class Prueba(Escena):
    def construir(self):
        t = Triangulo(lado=5).desplazar(-3, -0.5)
        c = Cuadrado(3, color="rojo").desplazar(3, 0)
        self.reproducir(Crear(t), Crear(c))
        self.reproducir(CambiarColor(t, "azul"),
                        CambiarColor(c, "blanco"))


Prueba().render()
