from manim import *
from scipy.interpolate import make_interp_spline

# Ocho medidas «tomadas a mano» (simuladas con semilla fija)
rng = np.random.default_rng(7)
XS = np.arange(8)
YS = np.sin(XS / 2) * 2 + rng.normal(0, 0.15, 8) + 2.5


class Suavizar(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 7, 1], y_range=[0, 5, 1],
                    x_length=10, y_length=5, tips=False)
        puntos = VGroup(*[Dot(ejes.c2p(a, b), color=RED)
                          for a, b in zip(XS, YS)])
        quebrada = ejes.plot_line_graph(
            XS, YS, add_vertex_dots=False, line_color=GREY_B)
        self.add(ejes, puntos)
        self.play(Create(quebrada))
        # Spline cúbico que pasa por los puntos
        spline = make_interp_spline(XS, YS, k=3)
        suave = ejes.plot(spline, x_range=[0, 7], color=BLUE_C)
        self.play(Transform(quebrada, suave))
        rotulo = Text("make_interp_spline(k=3)", font_size=26,
                      color=BLUE_C).to_edge(DOWN)
        self.play(FadeIn(rotulo))
        self.wait()
