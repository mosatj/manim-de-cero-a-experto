from manim import *


class TextoYCuadrado(Scene):
    def construct(self):
        # Cuadrícula de referencia: una unidad por casilla
        self.add(NumberPlane())
        saludo = Text("Hola", color=YELLOW, weight=BOLD,
                      font_size=100)
        saludo.shift(RIGHT * 3, UP * 2)   # suma: (3, 2)
        cuadrado = Square(side_length=3, color=RED)
        cuadrado.shift(LEFT * 3 + DOWN)   # (-3, -1)

        self.play(Write(saludo))
        self.play(Create(cuadrado))
        self.wait()
