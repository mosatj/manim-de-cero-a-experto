import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from manim import *
from asy_puente import importar_asy
from asy_utiles import glifos, por_color


class LogisticaAsy(Scene):
    """El campo, las soluciones y un punto que recorre una."""

    def construct(self):
        fig = importar_asy("asy_logistica.asy", height=6.4)
        fig.to_edge(LEFT, buff=0.3)
        ejes = por_color(fig, "#E9F2F7")
        numeros = glifos(fig).set_fill("#E9F2F7")
        campo = por_color(fig, "#6FA3C0")
        soluciones = por_color(fig, "#E0B04A")
        self.play(Create(ejes), Write(numeros))
        self.play(LaggedStart(*[Create(s) for s in campo],
                              lag_ratio=0.01), run_time=2)
        self.play(campo.animate.set_stroke(opacity=0.45),
                  LaggedStart(*[Create(s) for s in soluciones],
                              lag_ratio=0.3), run_time=3)
        punto = Dot(soluciones[1].get_start(), color="#B04A5A",
                    radius=0.1)
        self.play(MoveAlongPath(punto, soluciones[1]), run_time=3)
        ecuacion = MathTex(r"y' = y\,(1-y)", font_size=48)
        ecuacion.to_corner(UR, buff=0.6)
        self.play(Write(ecuacion))
        self.wait()
