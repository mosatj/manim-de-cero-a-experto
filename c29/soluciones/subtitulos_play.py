from manim import *


class SubtitulosPlay(Scene):
    def construct(self):
        cuadrado = Square(color=BLUE)
        circulo = Circle(color=YELLOW)
        # Dos formas: add_subcaption o dentro de play
        self.add_subcaption("Un cuadrado aparece.", duration=1)
        self.play(Create(cuadrado))
        self.play(Transform(cuadrado, circulo),
                  subcaption="Y se transforma en círculo.",
                  subcaption_duration=1.5)
