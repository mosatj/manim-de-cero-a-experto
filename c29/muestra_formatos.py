from manim import *


class MuestraFormatos(Scene):
    def construct(self):
        cuadrado = Square(2.5, color=BLUE, fill_opacity=0.6)
        circulo = Circle(1.2, color=YELLOW, fill_opacity=0.6)
        self.play(DrawBorderThenFill(cuadrado), run_time=1)
        self.play(Transform(cuadrado, circulo), run_time=1)
