import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from manim import *
from asy_puente import importar_asy


class IncentroAsy(Scene):
    """Bisectrices, incentro y circunferencia inscrita."""

    def construct(self):
        fig = importar_asy("asy_incentro.asy", height=6.8)
        fig.to_edge(LEFT, buff=0.8)
        triangulo, bisectrices, inscrita = fig[0], fig[1:4], fig[4]
        punto, letra = fig[5], fig[6].set_fill("#E9F2F7")
        texto = Text("Bisectrices: incentro I", font_size=36)
        texto.to_corner(UR, buff=0.6)
        self.play(Create(triangulo))
        self.play(Write(texto), LaggedStart(
            *[Create(b) for b in bisectrices], lag_ratio=0.4))
        self.play(GrowFromCenter(punto), Write(letra))
        # El radio: del incentro al lado AB (el más bajo)
        radio = Line(punto.get_center(),
                     [punto.get_x(), triangulo.get_bottom()[1], 0],
                     color="#E0B04A")
        self.play(Create(radio))
        self.play(Create(inscrita), run_time=1.5)
        self.wait()
