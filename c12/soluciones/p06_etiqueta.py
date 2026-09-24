from manim import *


class Etiqueta(VGroup):
    """Texto en un rectángulo redondeado del color pedido."""

    def __init__(self, texto, color=BLUE, font_size=32, **kwargs):
        super().__init__(**kwargs)
        self.texto = Text(texto, font_size=font_size)
        self.fondo = SurroundingRectangle(
            self.texto, buff=0.2, corner_radius=0.15, color=color,
            fill_color=color, fill_opacity=0.25)
        self.add(self.fondo, self.texto)


class EscenaEtiquetas(Scene):
    def construct(self):
        etiquetas = VGroup(Etiqueta("definición"),
                           Etiqueta("teorema", color=GREEN),
                           Etiqueta("ejemplo", color=ORANGE))
        self.add(etiquetas.arrange(RIGHT, buff=0.5))
