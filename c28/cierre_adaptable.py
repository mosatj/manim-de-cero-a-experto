from manim import *
from impares import cuadrado_de_escuadras


def componer_cierre():
    """El cierre de la lección, dispuesto según la forma del cuadro."""
    vertical = config.frame_height > config.frame_width
    figura = cuadrado_de_escuadras(4, lado=0.9 if vertical else 0.6)
    formula = MathTex(r"1+3+\cdots+(2n-1)=n^2", font_size=54)
    pregunta = Text("¿Y la suma de los pares?", font_size=36,
                    color=YELLOW)
    texto = VGroup(formula, pregunta).arrange(DOWN, buff=0.5)
    ancho_util = 0.85 * config.frame_width
    if texto.width > ancho_util:  # solo reduce, nunca agranda
        texto.scale_to_fit_width(ancho_util)
    grupo = VGroup(figura, texto)
    return grupo.arrange(DOWN if vertical else RIGHT, buff=0.9)


class CierreHorizontal(Scene):
    def construct(self):
        self.play(FadeIn(componer_cierre()))
