from manim import *


class TransformarCiclo(Scene):
    def construct(self):
        figura = Circle(radius=1.8, color=BLUE, fill_opacity=0.5)
        cuadrado = Square(side_length=3.2, color=TEAL,
                          fill_opacity=0.5)
        triangulo = Triangle(color=YELLOW, fill_opacity=0.5)
        triangulo.scale(2.2)

        self.play(Create(figura))
        # «figura» adopta la forma del cuadrado y luego la del
        # triángulo
        self.play(Transform(figura, cuadrado))
        self.play(Transform(figura, triangulo))
