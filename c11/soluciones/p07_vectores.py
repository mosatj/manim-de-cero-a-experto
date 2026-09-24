from manim import *


class Vectores(Scene):
    def construct(self):
        plantilla = TexTemplate()
        plantilla.add_to_preamble(r"\usepackage{esvect}")
        plantilla.add_to_preamble(r"\usepackage{cancel}")
        suma = MathTex(r"\vv{AB} + \vv{BC} = \vv{AC}",
                       tex_template=plantilla, font_size=80)
        frac = MathTex(r"\frac{\cancel{(x-1)}(x+1)}{\cancel{x-1}}"
                       r" = x+1", tex_template=plantilla,
                       font_size=64)
        self.add(VGroup(suma, frac).arrange(DOWN, buff=1))
