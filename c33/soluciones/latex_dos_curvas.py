import sys
from pathlib import Path
from manim import *

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from latex_tikz import figura_tikz, plantilla_tikz  # noqa: E402

# Las dos figuras comparten ejes y caja: \useasboundingbox fija el
# mismo tamaño aunque la segunda tenga más contenido.
EJES = r"""
\useasboundingbox (-1.2,-1.2) rectangle (9.5,7);
\begin{axis}[width=10cm,height=7cm,grid=major,xmin=0,xmax=3,
    ymin=0,ymax=9,xlabel=$x$,ylabel=$y$]
  \addplot[blue,thick,domain=0:3,samples=60] {x^2};
  %s
\end{axis}
"""
SEGUNDA = r"\addplot[red,thick,domain=0:3] {3*x};"


class DosCurvas(Scene):
    def construct(self):
        pgf = plantilla_tikz(
            paquetes=r"\usepackage{pgfplots}"
                     r"\pgfplotsset{compat=1.18}")
        opciones = {"plantilla": pgf, "grosor": 4, "height": 6}
        una = figura_tikz(EJES % "", **opciones)
        dos = figura_tikz(EJES % SEGUNDA, **opciones)
        dos.move_to(una)        # misma caja: se superponen exactas
        self.play(Create(una, run_time=3))
        self.wait(0.5)
        # La segunda figura contiene todo: aparece encima y la
        # primera se retira sin que nada se mueva
        self.add(dos)
        self.remove(una)
        self.wait()
