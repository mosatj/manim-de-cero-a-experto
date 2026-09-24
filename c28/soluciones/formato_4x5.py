import sys
from pathlib import Path

from manim import *

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from impares import cuadrado_de_escuadras  # noqa: E402

# Formato 4:5 (1080 × 1350): mismo ancho lógico que el vertical
config.pixel_width, config.pixel_height = 1080, 1350
config.frame_width = 8
config.frame_height = 8 * 1350 / 1080  # 10 unidades


class Formato4x5(Scene):
    def construct(self):
        figura = cuadrado_de_escuadras(4, lado=0.8).shift(0.8 * UP)
        formula = MathTex(r"1+3+5+7=4^2", font_size=64)
        formula.next_to(figura, DOWN, buff=0.7)
        self.add(figura, formula)
