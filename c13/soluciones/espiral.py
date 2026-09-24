from manim import *


class Espiral(Scene):
    def construct(self):
        figuras = VGroup(
            Circle(color=BLUE, fill_opacity=0.6),
            Square(color=TEAL, fill_opacity=0.6),
            Triangle(color=YELLOW, fill_opacity=0.6),
            Star(color=RED, fill_opacity=0.6),
        ).arrange(RIGHT, buff=0.8)
        # Cada pieza llega girando en espiral hasta su sitio
        self.play(SpiralIn(figuras), run_time=3)
