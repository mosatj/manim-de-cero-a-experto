from manim import *
from congelar import congelar


class Anagrama(Scene):
    def construct(self):
        colores = {"R": BLUE, "O": TEAL, "M": YELLOW, "A": RED}

        def palabra(texto):
            p = Text(texto, font_size=90)
            for letra, forma in zip(texto, p):
                forma.set_color(colores[letra])
            return p

        # Estela: la misma animación congelada en cinco instantes
        for alfa in [0, 0.25, 0.5, 0.75, 1]:
            ramo = palabra("RAMO").move_to(2.6 * UP)
            amor = palabra("AMOR").move_to(2.6 * DOWN)
            animacion = TransformMatchingShapes(ramo, amor,
                                                rate_func=linear)
            congelar(self, animacion, alfa)
