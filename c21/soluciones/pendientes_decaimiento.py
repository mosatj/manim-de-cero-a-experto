from manim import *


class PendientesDecaimiento(Scene):
    def construct(self):
        f = lambda t, y: -2 * y                # y' = -2y
        ejes = Axes(x_range=[0, 3, 0.5], y_range=[-2, 2, 1],
                    x_length=10, y_length=6, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24})
        campo = VGroup()
        for t in np.arange(0.1, 3, 0.2):
            for y in np.arange(-1.9, 2, 0.25):
                v = (ejes.c2p(t + 0.01, y + 0.01 * f(t, y))
                     - ejes.c2p(t, y))
                v = 0.13 * v / np.linalg.norm(v)
                c = ejes.c2p(t, y)
                campo.add(Line(c - v, c + v, color=BLUE_C,
                               stroke_width=2))
        soluciones = VGroup(*[
            ejes.plot(lambda t, y0=y0: y0 * np.exp(-2 * t),
                      x_range=[0, 3], color=YELLOW)
            for y0 in (-2, -1, -0.5, 0.5, 1, 2)])
        self.add(ejes, campo)
        self.play(Create(soluciones, lag_ratio=0.2), run_time=3)
        self.add(MathTex(r"y' = -2y,\quad y = y_0 e^{-2t}")
                 .add_background_rectangle().to_corner(UR))
