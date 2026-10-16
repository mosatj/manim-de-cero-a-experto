import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent  # codigo/c32
sys.path.insert(0, str(RAIZ / "proyecto8"))
from manim import *
from scipy.integrate import quad
from funcion import f, A, B, particion
from piezas import ejes2d, curva, discos_2d
from estilo import COLOR_SOLIDO, COLOR_DISCO, COLOR_ACENTO
from estilo import TAM_ROTULO

G = 0.5  # el radio interior: la región va de y = g a y = f


def g(x):
    return G + 0 * x


def volumen_arandelas(n):
    xs, dx = particion(n)
    return float(np.sum(np.pi * (f(xs) ** 2 - g(xs) ** 2) * dx))


class Arandelas(Scene):
    def construct(self):
        ejes = ejes2d().shift(DOWN * 0.4)
        arriba, abajo = curva(ejes), ejes.plot(
            g, x_range=[A, B], color=COLOR_ACENTO, stroke_width=3
        )
        region = ejes.get_area(
            arriba, x_range=(A, B), bounded_graph=abajo,
            color=COLOR_SOLIDO, opacity=0.4,
        )
        self.play(Create(ejes), Create(arriba), Create(abajo))
        self.play(FadeIn(region))
        # Cada arandela: la elipse exterior (f) y la interior (g)
        n = 8
        exteriores = discos_2d(ejes, n)
        xs, dx = particion(n)
        ancho = 0.6 * (ejes.c2p(dx, 0)[0] - ejes.c2p(0, 0)[0])
        alto = ejes.c2p(0, G)[1] - ejes.c2p(0, -G)[1]
        interiores = VGroup(*[
            Ellipse(width=ancho, height=alto, color=COLOR_ACENTO,
                    fill_opacity=0.6, stroke_width=1.5)
            .move_to(ejes.c2p(x, 0)) for x in xs
        ])
        self.play(FadeOut(region), FadeIn(exteriores))
        self.play(FadeIn(interiores))
        exacto, _ = quad(lambda x: f(x) ** 2 - g(x) ** 2, A, B)
        rotulo = MathTex(
            rf"V=\pi\int_0^4\bigl(f^2-g^2\bigr)\,dx"
            rf"={np.pi * exacto:.3f}",
            rf"\qquad n={n}:\ V\approx{volumen_arandelas(n):.3f}",
            font_size=TAM_ROTULO,
        ).to_edge(UP, buff=0.3)
        rotulo[1].set_color(COLOR_DISCO)
        self.play(Write(rotulo))
        self.wait()
