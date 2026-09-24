from manim import *


class Corregida(Scene):
    def construct(self):
        circulo = Circle(radius=2, color=RED)  # Circle, color
        self.play(Create(circulo))             # paréntesis
        self.wait()
