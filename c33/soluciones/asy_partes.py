import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from manim import *
from asy_puente import importar_asy


class PartesAsy(Scene):
    """Cada submobject con su índice: el orden del archivo .asy."""

    def construct(self):
        figura = importar_asy("../asy_construccion.asy", height=6)
        figura.shift(LEFT * 2.3)
        colores = color_gradient(["#6FA3C0", "#E0B04A", "#B04A5A"],
                                 len(figura))
        etiquetas = VGroup()
        for k, (parte, color) in enumerate(zip(figura, colores)):
            parte.set_color(color)
            numero = Integer(k, font_size=22, color=color)
            numero.next_to(parte.point_from_proportion(0.3), UR,
                           buff=0.05)
            etiquetas.add(numero)
        self.add(figura)
        self.play(LaggedStart(*[FadeIn(e) for e in etiquetas],
                              lag_ratio=0.15), run_time=2)
        nota = Text(f"{len(figura)} partes, en el orden del .asy",
                    font_size=28).to_edge(DOWN)
        self.play(Write(nota))
        self.wait()
