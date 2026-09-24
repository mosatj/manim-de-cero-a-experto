from manim import *


class IndicarPalabras(Scene):
    def construct(self):
        frase = VGroup(*[Text(p, font_size=56) for p in
                         ("La", "derivada", "mide", "el",
                          "cambio")])
        frase.arrange(RIGHT, buff=0.35)
        self.add(frase)
        # Una palabra detrás de otra, como si se leyera en voz alta
        self.play(Succession(*[Indicate(p) for p in frase]))
        self.play(Circumscribe(frase[-1], color=RED, fade_out=True))
        self.play(frase[-1].animate.set_color(RED))
