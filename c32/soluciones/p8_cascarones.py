# Ejercicio 32.18 (complemento): la región del proyecto 8 girada alrededor
# del eje y. Cambian la fórmula y las piezas; la partición y la estructura
# (matemática / piezas / escenas) no cambian.
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent  # codigo/c32
sys.path.insert(0, str(RAIZ / "proyecto8"))
from manim import *
from scipy.integrate import quad
from funcion import f, A, B, particion
from estilo import COLOR_CURVA, COLOR_SOLIDO, COLOR_DISCO
from estilo import COLOR_ACENTO, TAM_ROTULO


# --- La matemática (lo que cambiaría en funcion.py) -----------------


def volumen_exacto_y():
    """2 pi por la integral de x f(x) en [A, B]."""
    integral, _ = quad(lambda x: x * f(x), A, B)
    return 2 * np.pi * integral


def volumen_cascarones(n):
    """Suma de n cascarones 2 pi x_i f(x_i) dx, con x_i en el centro."""
    xs, dx = particion(n)
    return float(np.sum(2 * np.pi * xs * f(xs) * dx))


# --- Las piezas (lo que cambiaría en piezas.py) ---------------------


def ejes_simetricos():
    # El sólido ocupa -4 <= x <= 4: el eje de giro (y) queda en el centro
    return Axes(
        x_range=[-4.5, 4.5, 1], y_range=[0, 1.8, 1],
        x_length=10.8, y_length=3.6,
        tips=False, axis_config={"stroke_width": 2},
    )


def cascaron_de_perfil(ejes, x, dx):
    """Un cascarón visto de frente: dos franjas de altura f(x),
    a distancia x del eje y a cada lado, unidas por elipses."""
    franjas = VGroup(*[
        Rectangle(
            width=ejes.c2p(dx, 0)[0] - ejes.c2p(0, 0)[0],
            height=ejes.c2p(0, f(x))[1] - ejes.c2p(0, 0)[1],
            fill_color=COLOR_DISCO, fill_opacity=0.45,
            stroke_color=COLOR_DISCO, stroke_width=1,
        ).move_to(ejes.c2p(s * x, f(x) / 2)) for s in (-1, 1)
    ])
    ancho = ejes.c2p(x, 0)[0] - ejes.c2p(-x, 0)[0]
    bordes = VGroup(*[
        Ellipse(width=ancho, height=0.35, color=COLOR_DISCO,
                stroke_width=1.5).move_to(ejes.c2p(0, h))
        for h in (0, f(x))
    ])
    return VGroup(franjas, bordes)


class Cascarones(Scene):
    def construct(self):
        ejes = ejes_simetricos().shift(DOWN * 1.1)
        derecha = ejes.plot(f, x_range=[A, B], color=COLOR_CURVA,
                            stroke_width=4)
        izquierda = ejes.plot(lambda x: f(-x), x_range=[-B, -A],
                              color=COLOR_CURVA, stroke_width=4)
        eje_giro = DashedLine(ejes.c2p(0, 0), ejes.c2p(0, 1.8),
                              color=COLOR_ACENTO)
        region = ejes.get_area(derecha, x_range=(A, B),
                               color=COLOR_SOLIDO, opacity=0.4)
        self.play(Create(ejes), Create(derecha), Create(eje_giro))
        self.play(FadeIn(region))
        # El giro deja el mismo perfil reflejado al otro lado del eje
        self.play(TransformFromCopy(derecha, izquierda))
        n = 4
        xs, dx = particion(n)
        cascarones = VGroup(*[cascaron_de_perfil(ejes, x, 0.8 * dx)
                              for x in xs])
        self.play(FadeOut(region),
                  LaggedStart(*[FadeIn(c) for c in cascarones],
                              lag_ratio=0.3))
        formula = MathTex(
            rf"V=2\pi\int_0^4 x\,f(x)\,dx={volumen_exacto_y():.3f}",
            font_size=TAM_ROTULO, color=COLOR_ACENTO,
        )
        aproximaciones = VGroup(*[
            MathTex(rf"n={k}:\ V\approx{volumen_cascarones(k):.3f}",
                    font_size=TAM_ROTULO, color=COLOR_DISCO)
            for k in (4, 16, 64)
        ]).arrange(RIGHT, buff=0.8)
        VGroup(formula, aproximaciones).arrange(DOWN, buff=0.3)\
            .to_edge(UP, buff=0.4)
        self.play(Write(formula))
        self.play(FadeIn(aproximaciones, shift=DOWN * 0.2))
        self.wait()


if __name__ == "__main__":
    exacto = volumen_exacto_y()
    print(f"Volumen exacto (eje y): {exacto:.6f}")
    for n in (4, 16, 64):
        print(f"n = {n:>3}: {volumen_cascarones(n):.6f}")
