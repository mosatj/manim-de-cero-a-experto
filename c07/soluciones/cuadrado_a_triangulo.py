from manim import *


class CuadradoATriangulo(Scene):
    def construct(self):
        cuadrado = Square(side_length=3, color=BLUE)
        triangulo = Triangle(color=GREEN, fill_opacity=0.5)
        triangulo.scale(2)
        self.play(Create(cuadrado))
        self.wait()
        self.play(Transform(cuadrado, triangulo))
        self.wait()
