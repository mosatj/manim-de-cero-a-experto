from manim import *
from escena_base import ProyectoScene
from componentes import Tarjeta
from estilo import PRIMARIO, SECUNDARIO


class Gancho(ProyectoScene):
    """Primer bloque del guion: una escena por bloque, numeradas."""

    def construct(self):
        a = Tarjeta("Figura A", PRIMARIO).shift(LEFT * 3)
        b = Tarjeta("Figura B", SECUNDARIO).shift(RIGHT * 3)
        self.next_section("gancho")
        self.decir("gancho", FadeIn(a, shift=UP),
                   FadeIn(b, shift=UP))
        self.next_section("idea")
        self.decir("idea", a.resaltar(), b.resaltar())
        self.next_section("cierre")
        par = VGroup(a, b)
        self.decir("cierre", par.animate.arrange(RIGHT, buff=1.5))
