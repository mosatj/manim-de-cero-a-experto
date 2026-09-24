from manim import *


class TresPalabras(Scene):
    def construct(self):
        palabras = VGroup(*[Text(p, font_size=60) for p in
                            ("Ver", "entender", "recordar")])
        palabras.arrange(RIGHT, buff=0.8)
        self.play(LaggedStart(
            *[FadeIn(p, shift=RIGHT) for p in palabras],
            lag_ratio=0.5, run_time=2.5))
