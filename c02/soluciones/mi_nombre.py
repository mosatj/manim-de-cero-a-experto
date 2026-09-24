from manim import *


class MiNombre(Scene):
    def construct(self):
        nombre = Text("Ada Lovelace", font_size=72, color=BLUE)
        lema = Text("Mi primera animación", font_size=36)
        lema.next_to(nombre, DOWN)
        self.play(Write(nombre))
        self.play(FadeIn(lema))
        self.wait(2)
