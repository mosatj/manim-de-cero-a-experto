from manim import *


class Area(Scene):
    def construct(self):
        area = MathTex("A", "=", r"\pi", "r^2", font_size=96)
        area[0].set_color(YELLOW)   # A
        area[2].set_color(BLUE)     # pi
        area[3].set_color(GREEN)    # r^2
        self.add(area)
