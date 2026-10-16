import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from manim import *
from asy_puente import importar_asy


class EspiralAsy(Scene):
    """Un camino de Asymptote recorrido por un punto con estela."""

    def construct(self):
        figura = importar_asy("asy_espiral.asy", height=6.5)
        espiral, eje_x, eje_y = figura
        espiral.set_stroke(opacity=0.35)
        self.add(figura)
        punto = Dot(color="#E0B04A", radius=0.09)
        punto.move_to(espiral.get_start())
        estela = TracedPath(punto.get_center,
                            stroke_color="#E0B04A", stroke_width=4)
        self.add(estela, punto)
        self.play(MoveAlongPath(punto, espiral), run_time=6,
                  rate_func=linear)
        self.wait()
