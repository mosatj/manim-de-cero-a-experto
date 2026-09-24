from manim import *


class EtiquetaConAlways(Scene):
    def construct(self):
        cuadrado = Square(1.2, color=BLUE, fill_opacity=0.4)
        cuadrado.to_edge(LEFT)
        nombre = Text("cuadrado", font_size=30)
        nombre.always.next_to(cuadrado, DOWN)
        self.add(cuadrado, nombre)
        self.play(cuadrado.animate.to_edge(RIGHT).rotate(PI / 4))
