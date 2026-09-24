"""Tarjeta: rótulo y fórmula dentro de un marco redondeado."""
from manim import *

if __package__:        # importado como parte del paquete
    from .estilo import ACERO, GRANATE, TINTA
else:                  # ejecutado suelto, para probarlo
    from estilo import ACERO, GRANATE, TINTA


class Tarjeta(VGroup):
    def __init__(self, rotulo, formula, color=ACERO, **kwargs):
        super().__init__(**kwargs)
        self.rotulo = Text(rotulo, font_size=24, color=color)
        self.formula = MathTex(formula, font_size=44, color=TINTA)
        cuerpo = VGroup(self.rotulo, self.formula)
        cuerpo.arrange(DOWN, buff=0.25)
        self.marco = RoundedRectangle(
            corner_radius=0.2, width=cuerpo.width + 0.8,
            height=cuerpo.height + 0.6, color=color)
        self.marco.move_to(cuerpo)
        self.add(self.marco, cuerpo)

    def resaltar(self, color=GRANATE):
        """Devuelve la animación que colorea el marco."""
        return self.marco.animate.set_stroke(color, width=6)

