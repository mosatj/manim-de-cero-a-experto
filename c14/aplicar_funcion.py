from manim import *


def ordenar(grupo):
    """Recibe una copia del grupo y la devuelve modificada."""
    grupo.arrange(RIGHT, buff=0.3)
    grupo.set_color(YELLOW)
    return grupo


class AplicarFuncion(Scene):
    def construct(self):
        figuras = VGroup(Circle(), Square(), Triangle()).scale(0.6)
        figuras.arrange(DOWN, buff=0.4)
        self.add(figuras)
        self.play(ApplyFunction(ordenar, figuras))
