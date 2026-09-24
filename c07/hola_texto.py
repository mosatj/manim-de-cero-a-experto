from manim import *


class HolaTexto(Scene):
    def construct(self):
        saludo = Text("Hola", color=BLUE_B,
                      weight=BOLD, font_size=100)
        self.play(Write(saludo))
        self.wait(2)
        self.play(Unwrite(saludo))
        # Un segundo texto, escrito y colocado en una línea
        adios = Text("Adiós", color=YELLOW, font_size=80)
        self.play(Write(adios.to_edge(UP)))
        self.wait()
