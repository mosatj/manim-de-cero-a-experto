from manim import *
from latex_tikz import figura_tikz, plantilla_tikz

GRAFO = r"""
\foreach \i in {0,...,4}
  \node[circle,draw,minimum size=7mm] (n\i)
    at (72*\i+90:2) {$v_\i$};
\foreach \i/\j in {0/1,1/2,2/3,3/4,4/0,0/2,1/3}
  \draw[-{Stealth[length=2.5mm]}] (n\i) -- (n\j);
\draw[red,very thick] (n0) -- (n2) -- (n4);
"""


class GrafoTikz(Scene):
    def construct(self):
        flechas = plantilla_tikz("arrows.meta")
        grafo = figura_tikz(GRAFO, plantilla=flechas)
        grafo.set(height=5.5)
        titulo = Text("Un grafo dibujado con TikZ", font_size=32)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.play(Create(grafo, run_time=4))
        self.wait()
