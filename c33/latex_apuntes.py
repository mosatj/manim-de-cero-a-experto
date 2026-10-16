from pathlib import Path
from manim import *
from latex_tikz import figura_tikz


class FiguraDeApuntes(Scene):
    def construct(self):
        codigo = Path("latex_apuntes_figura.tikz").read_text()
        figura = figura_tikz(codigo, height=5)
        self.play(Create(figura, run_time=4))
        self.play(figura.animate.shift(2 * LEFT), run_time=1)
        self.wait()
