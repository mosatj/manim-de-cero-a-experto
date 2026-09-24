from manim import *
from impares import cuadrado_de_escuadras


class Miniatura(Scene):
    def construct(self):
        # Pocas palabras, muy grandes, y una sola imagen reconocible
        pregunta = Text("1+3+5+7…", font_size=96, weight=BOLD)
        remate = Text("¿por qué\nsiempre un\ncuadrado?", font_size=64,
                      color=YELLOW, line_spacing=0.8)
        textos = VGroup(pregunta, remate).arrange(DOWN, aligned_edge=LEFT,
                                                  buff=0.5)
        figura = cuadrado_de_escuadras(4, lado=1.2)
        VGroup(textos, figura).arrange(RIGHT, buff=1.0)
        self.add(textos, figura)
