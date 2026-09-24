import sys
from pathlib import Path

# componentes.py está en la carpeta madre: la añadimos a la ruta
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import *
from componentes import Tarjeta


class TarjetaTeorema(Tarjeta):
    """Una Tarjeta con una línea de pie (autor, año...)."""

    def __init__(self, titulo, formula, pie, **kwargs):
        super().__init__(titulo, formula, **kwargs)
        self.pie = Text(pie, font_size=20, slant=ITALIC)
        self.pie.next_to(self.formula, DOWN, buff=0.25)
        # El marco debe crecer para abarcar el pie
        alto = self.titulo.get_top()[1] - self.pie.get_bottom()[1]
        self.marco.stretch_to_fit_height(alto + 0.6)
        self.marco.move_to(VGroup(self.titulo, self.pie))
        self.add(self.pie)


class EscenaTeorema(Scene):
    def construct(self):
        t = TarjetaTeorema("Euler", r"V - A + C = 2",
                           "poliedros convexos, 1758", color=GREEN)
        self.add(t.scale(1.4))
