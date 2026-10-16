from manim import *
from estilo import PRIMARIO, ACENTO, TEXTO, TAM_TEXTO


class Tarjeta(VGroup):
    """Rótulo con marco. Sus métodos devuelven animaciones; la
    escena decide cuándo reproducirlas y con qué duración."""

    def __init__(self, texto, color=PRIMARIO, **kwargs):
        super().__init__(**kwargs)
        self.rotulo = Text(texto, font_size=TAM_TEXTO, color=TEXTO)
        self.marco = SurroundingRectangle(
            self.rotulo, color=color, buff=0.3, corner_radius=0.1
        )
        self.add(self.marco, self.rotulo)

    def resaltar(self):
        marco = self.marco.animate
        return marco.set_color(ACENTO).set_stroke(width=6)
