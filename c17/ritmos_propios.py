from manim import *
from manim.utils.rate_functions import unit_interval


@unit_interval                      # fuera de [0, 1] devuelve 0 o 1
def escalones(t, n=4):
    """Avanza a saltos: n mesetas unidas por tramos suaves."""
    k = min(int(t * n), n - 1)      # tramo actual
    return (k + smooth(t * n - k)) / n


def pasarse_y_volver(t):
    """Se pasa de la meta cerca de un 18 % y regresa."""
    return smooth(t) + 0.6 * np.sin(PI * t) * t ** 2


RITMOS = [
    ("escalones", escalones),
    ("squish_rate_func(smooth,0.3,0.7)",
     squish_rate_func(smooth, 0.3, 0.7)),
    ("pasarse_y_volver", pasarse_y_volver),
]


class RitmosPropios(Scene):
    def construct(self):
        paneles = VGroup()
        for nombre, f in RITMOS:
            ejes = Axes(x_range=[0, 1, 0.5], y_range=[0, 1.25, 0.5],
                        x_length=3.4, y_length=2.8, tips=False,
                        axis_config={"include_numbers": True,
                                     "font_size": 22})
            meta = DashedLine(ejes.c2p(0, 1), ejes.c2p(1, 1),
                              color=GRAY, stroke_width=2)
            curva = ejes.plot(f, x_range=[0, 1, .005], color=YELLOW)
            titulo = Text(nombre, font="Menlo", font_size=16)
            titulo.next_to(ejes, UP, buff=0.3)
            paneles.add(VGroup(ejes, meta, curva, titulo))
        paneles.arrange(RIGHT, buff=0.7)
        self.add(*[VGroup(p[0], p[1], p[3]) for p in paneles])
        # Las tres curvas se dibujan a la vez, a velocidad constante
        self.play(*[Create(p[2]) for p in paneles],
                  run_time=2, rate_func=linear)
        self.wait()
