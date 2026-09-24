from manim import *


class LimiteRecta(Scene):
    def construct(self):
        ejes = Axes(x_range=[-1, 3, 1], y_range=[-1, 6, 1],
                    x_length=7, y_length=6.5, tips=False)
        ejes.add_coordinates(font_size=22).to_edge(LEFT)
        f = lambda x: 2 * x + 1
        recta = ejes.plot(f, x_range=[-1, 2.5], color=BLUE)
        eps = 0.8
        delta = eps / 2              # |f(x) − 3| = 2|x − 1| < ε
        p = ejes.c2p
        franja_e = Polygon(p(-1, 3 - eps), p(3, 3 - eps),
                           p(3, 3 + eps), p(-1, 3 + eps),
                           stroke_width=0, fill_color=YELLOW,
                           fill_opacity=0.25)
        franja_d = Polygon(p(1 - delta, -1), p(1 + delta, -1),
                           p(1 + delta, 6), p(1 - delta, 6),
                           stroke_width=0, fill_color=GREEN,
                           fill_opacity=0.25)
        trozo = ejes.plot(f, x_range=[1 - delta, 1 + delta],
                          color=WHITE, stroke_width=6)
        texto = MathTex(r"\varepsilon=0.8",
                        r"\qquad\delta=\frac{\varepsilon}{2}=0.4")
        texto.to_edge(RIGHT).shift(UP)
        texto[0].set_color(YELLOW)
        texto[1].set_color(GREEN)
        self.add(ejes, franja_e, franja_d, recta, trozo, texto)
