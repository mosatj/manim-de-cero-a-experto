import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent  # codigo/c32
sys.path.insert(0, str(RAIZ / "proyecto5"))
from manim import *
from funcion import f, fx, fy, semiejes, PUNTO


class GradienteNivel(Scene):
    """El gradiente es perpendicular a la curva de nivel."""

    def construct(self):
        plano = NumberPlane(
            x_range=[-4, 4],
            y_range=[-3, 3],
            background_line_style={"stroke_opacity": 0.3},
        )
        a, b = PUNTO
        sx, sy = semiejes(f(a, b))
        nivel = plano.plot_parametric_curve(
            lambda t: np.array([sx * np.cos(t), sy * np.sin(t)]),
            t_range=[0, TAU],
            color=BLUE,
        )
        p = plano.c2p(a, b)
        gradiente = Arrow(
            p,
            plano.c2p(a + fx(a, b), b + fy(a, b)),
            buff=0,
            color=YELLOW,
        )
        rotulo = MathTex(
            r"\nabla f(1,\,0.8) = (-1,\,-1.6)", color=YELLOW
        ).to_corner(UL)
        self.add(plano)
        self.play(Create(nivel), FadeIn(Dot(p)))
        self.play(GrowArrow(gradiente), Write(rotulo))
