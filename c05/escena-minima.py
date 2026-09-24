from manim import *


class MiPrimeraEscena(Scene):            # hereda de Scene
    def construct(self):                 # sobrescribe el gancho
        circulo = Circle(radius=2, color=RED)
        cuadrado = Square(side_length=3, color=BLUE)
        fila = VGroup(circulo, cuadrado).arrange(RIGHT, buff=1)
        self.play(Create(fila))
        self.wait(0.5)
        self.play(cuadrado.animate.shift(0.5 * UP + 0.5 * RIGHT),
                  run_time=2)
