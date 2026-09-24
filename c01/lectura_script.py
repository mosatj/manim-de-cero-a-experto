from manim import *


class CuadradoACirculo(Scene):
    def construct(self):
        cuadrado = Square()  # cuadrado inicial (lado 2)
        circulo = Circle()  # círculo al que se transformará
        circulo.set_fill(PINK, opacity=0.5)

        self.play(Create(cuadrado))  # se dibuja el borde
        self.wait(1)  # pausa de un segundo
        self.play(Transform(cuadrado, circulo))  # se deforma
        self.wait(1)
