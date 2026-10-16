from manim import *
from latex_tikz import figura_tikz, plantilla_tikz

DIAGRAMA = (r"A \arrow{r}{f} \arrow[swap]{d}{g} & B \arrow{d}{h} \\ "
            r"C \arrow[swap]{r}{k} & D")


class DiagramaConmutativo(Scene):
    def construct(self):
        cd = plantilla_tikz(paquetes=r"\usepackage{tikz-cd}")
        diagrama = figura_tikz(DIAGRAMA, entorno="tikzcd",
                               plantilla=cd, height=4)
        conmuta = MathTex(r"h\circ f = k\circ g").next_to(
            diagrama, DOWN, buff=0.6)
        self.play(Write(diagrama, run_time=3))
        self.play(FadeIn(conmuta))
        self.wait()
