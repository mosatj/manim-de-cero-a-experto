import sys
from pathlib import Path

from manim import *

sys.path.append(str(Path(__file__).parent.parent / "proyecto"))
from componentes import ACERO, CuadradoImpares, LeccionScene


class LeccionNumeradaScene(LeccionScene):
    """Añade el número de escena y una marca de agua."""

    numero = 0

    def setup(self):
        super().setup()      # encabezado y pie heredados
        etiqueta = Text(f"{self.numero:02d}", font_size=26,
                        color=ACERO)
        marca = Text("M. Toledo", font_size=18, color=ACERO)
        marca.set_opacity(0.5)
        self.add(etiqueta.to_corner(UL, buff=0.35),
                 marca.to_corner(DL, buff=0.3))


class Cuadrado4(LeccionNumeradaScene):
    titulo = "Cuatro capas"
    numero = 2

    def construct(self):
        self.play(FadeIn(CuadradoImpares(4), lag_ratio=0.1))
