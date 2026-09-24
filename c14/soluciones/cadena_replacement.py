from manim import *


class CadenaReplacement(Scene):
    def construct(self):
        formas = [
            Circle(radius=1.5, color=BLUE, fill_opacity=0.5),
            Square(side_length=3, color=TEAL, fill_opacity=0.5),
            Triangle(color=YELLOW, fill_opacity=0.5).scale(2),
            Star(outer_radius=1.8, color=RED, fill_opacity=0.5),
        ]
        self.play(Create(formas[0]))
        for actual, siguiente in zip(formas[:-1], formas[1:]):
            # Tras cada paso, «siguiente» es la que está en escena
            self.play(ReplacementTransform(actual, siguiente))
        self.play(formas[-1].animate.set_fill(opacity=1))
