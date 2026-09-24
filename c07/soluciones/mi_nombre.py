from manim import *


class MiNombre(Scene):
    def construct(self):
        nombre = Text("Ada Lovelace", color=YELLOW,
                      font_size=72).to_edge(UP)
        linea = Line(LEFT * 4, RIGHT * 4, color=YELLOW)
        linea.next_to(nombre, DOWN)
        self.play(Write(nombre))
        self.play(Create(linea))
        self.wait()
