from manim import *


class SucesionE(Scene):
    def construct(self):
        a = lambda n: (1 + 1 / n)**n
        ejes = Axes(x_range=[0, 40, 5], y_range=[0, 3, 0.5],
                    x_length=11, y_length=5.5, tips=False)
        ejes.add_coordinates(font_size=22).shift(0.4 * DOWN)
        rot = ejes.get_x_axis_label(MathTex("n"))
        puntos = VGroup(*[Dot(ejes.c2p(n, a(n)), radius=0.05)
                          for n in range(1, 41)])
        recta_e = DashedLine(ejes.c2p(0, np.e), ejes.c2p(40, np.e),
                             color=YELLOW)
        nom_e = MathTex(r"e", color=YELLOW).next_to(recta_e, RIGHT)

        # Franja (e − ε, e + ε) y el primer N a partir del cual
        # todos los términos quedan dentro (a_n es creciente)
        eps = 0.05
        N = next(n for n in range(1, 1000) if np.e - a(n) < eps)
        abajo, arriba = np.e - eps, np.e + eps
        franja = Polygon(ejes.c2p(0, abajo), ejes.c2p(40, abajo),
                         ejes.c2p(40, arriba), ejes.c2p(0, arriba),
                         stroke_width=0, fill_color=YELLOW,
                         fill_opacity=0.25)
        marca = DashedLine(ejes.c2p(N, 0), ejes.c2p(N, 3))
        nom_N = MathTex(rf"N={N}", color=GREEN).next_to(marca, UP)
        dentro = VGroup(*puntos[N - 1:])
        formula = MathTex(r"a_n=\left(1+\frac{1}{n}\right)^{n}"
                          r"\longrightarrow e", font_size=40)
        formula.move_to(ejes.c2p(14.5, 1.3))
        cond = MathTex(rf"n\ge {N}\ \Rightarrow\ |a_n-e|<{eps}",
                       color=GREEN, font_size=40)
        cond.next_to(formula, DOWN)
        cond.align_to(formula, LEFT)

        self.play(Create(ejes), Write(rot), Write(formula))
        self.play(LaggedStart(*[FadeIn(p, scale=2) for p in puntos],
                              lag_ratio=0.1), run_time=3)
        self.play(Create(recta_e), Write(nom_e))
        self.play(FadeIn(franja), Create(marca), Write(nom_N))
        self.play(dentro.animate.set_color(GREEN), Write(cond))
