from manim import *
from latex_tikz import figura_tikz, plantilla_tikz

GRAFICA = r"""
\begin{axis}[width=10cm,height=7cm,grid=major,
    xlabel=$x$,ylabel=$y$,legend pos=north west]
  \addplot[blue,thick,domain=0:3,samples=60] {x^2};
  \addlegendentry{$x^2$}
  \addplot[red,thick,domain=0:3] {3*x};
  \addlegendentry{$3x$}
\end{axis}
"""


class GraficaPgfplots(Scene):
    def construct(self):
        pgf = plantilla_tikz(
            paquetes=r"\usepackage{pgfplots}"
                     r"\pgfplotsset{compat=1.18}")
        grafica = figura_tikz(GRAFICA, plantilla=pgf, grosor=4)
        grafica.set(height=6)
        self.play(Create(grafica, run_time=4))
        self.wait()
