from manim import *


class Corregido(Scene):
    def construct(self):
        texto = Text("Hola", color=BLUE_B, weight=BOLD,
                     font_size=100).to_edge(UP)
        rect = RoundedRectangle(fill_opacity=0.2, color=RED,
                                corner_radius=0.2)
        rect.shift(LEFT * 3 + DOWN)
        triangulo = Triangle(fill_opacity=0.2, color=BLUE)
        triangulo.scale(2).shift(RIGHT * 3 + DOWN)

        self.play(Write(texto))
        self.play(Write(rect), Create(triangulo))
        self.wait(2)
