from manim import *


class Frase(Scene):
    def construct(self):
        frase = Text("Manim es genial", font_size=64,
                     t2c={"genial": YELLOW}, t2w={"genial": BOLD})
        subtitulo = Text("animación matemática con Python",
                         font_size=32, slant=ITALIC, color=GRAY_B)
        self.add(VGroup(frase, subtitulo).arrange(DOWN, buff=0.4))
