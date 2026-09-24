from manim import *


class TrianguloACirculo(Scene):
    def construct(self):
        titulo = Text("Del triángulo al círculo", font_size=40)
        titulo.to_edge(UP)
        triangulo = Triangle(color=YELLOW).scale(2)  # otra figura
        circulo = Circle(radius=1.5, color=GREEN, fill_opacity=0.5)

        self.play(Write(titulo))
        self.play(Create(triangulo))
        self.play(Transform(triangulo, circulo), run_time=3)
        self.wait()
