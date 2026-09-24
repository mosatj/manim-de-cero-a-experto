from manim import *


class Binomio(Scene):
    def construct(self):
        f = MathTex(r"{{(a+b)^2}} = {{a^2}} + {{2ab}} + {{b^2}}",
                    font_size=80)
        f.set_color_by_tex("a^2", BLUE)
        f.set_color_by_tex("2ab", YELLOW)
        f.set_color_by_tex("b^2", GREEN)
        self.add(f)
