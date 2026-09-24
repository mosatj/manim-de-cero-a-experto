from manim import *


class Venn(Scene):
    def construct(self):
        a = Circle(2, color=BLUE).shift(1.2 * LEFT)
        b = Circle(2, color=RED).shift(1.2 * RIGHT)
        solo_a = Difference(a, b, color=BLUE, fill_opacity=0.6,
                            stroke_width=0)
        self.add(solo_a, a, b)
        self.add(MathTex("A").next_to(a, UL, buff=-0.3),
                 MathTex("B").next_to(b, UR, buff=-0.3),
                 MathTex(r"A \setminus B").move_to(2.2 * LEFT))
