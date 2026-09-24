from manim import *


class PrimerVistazo(Scene):
    def construct(self):
        # 1. Crear los objetos (todavía no se ven)
        titulo = Text("Del cuadrado al círculo", font_size=40)
        titulo.to_edge(UP)
        cuadrado = Square(side_length=3, color=BLUE)
        circulo = Circle(radius=1.5, color=RED, fill_opacity=0.5)

        # 2. Animarlos, uno tras otro
        self.play(Write(titulo))
        self.play(Create(cuadrado))
        self.play(Transform(cuadrado, circulo))
        self.wait()
