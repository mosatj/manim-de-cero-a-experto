from manim import *


class RegresionLineal(Scene):
    def construct(self):
        datos = np.loadtxt("datos/estudio.csv", delimiter=",",
                           skiprows=1)
        x, y = datos[:, 0], datos[:, 1]
        m_opt, b_opt = np.polyfit(x, y, 1)      # recta óptima
        xm, ym = x.mean(), y.mean()             # centro

        ejes = Axes(
            x_range=[0, 10, 2], y_range=[0, 20, 5],
            x_length=7.5, y_length=5.5, tips=False,
            axis_config={"include_numbers": True, "font_size": 26},
        ).to_edge(LEFT, buff=0.8).shift(0.3 * DOWN)
        rotulos = ejes.get_axis_labels(Tex("horas", font_size=32),
                                       Tex("nota", font_size=32))
        puntos = VGroup(*[Dot(ejes.c2p(a, c), radius=0.06,
                              color=TEAL_B) for a, c in zip(x, y)])

        # La recta gira alrededor de (xm, ym): cambia su pendiente
        m = ValueTracker(0)

        def recta_y(t):
            return ym + m.get_value() * (t - xm)

        recta = always_redraw(lambda: ejes.plot(
            recta_y, x_range=[0, 10], color=YELLOW))
        residuos = always_redraw(lambda: VGroup(*[
            Line(ejes.c2p(a, c), ejes.c2p(a, recta_y(a)),
                 color=RED_C, stroke_width=2)
            for a, c in zip(x, y)]))

        def sce():   # suma de los cuadrados de los residuos
            return ((y - recta_y(x)) ** 2).sum()

        rotulo = MathTex(r"\sum r_i^2 =", font_size=40)
        valor = DecimalNumber(sce(), num_decimal_places=1,
                              font_size=40, color=RED_C)
        valor.add_updater(lambda d: d.set_value(sce()))
        ecuacion = MathTex(rf"y = {m_opt:.2f}\,x + {b_opt:.2f}",
                           font_size=40, color=YELLOW)
        suma = VGroup(rotulo, valor).arrange(RIGHT)
        panel = VGroup(suma, ecuacion)
        panel.arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        panel.to_edge(RIGHT, buff=0.5)
        centro = Dot(ejes.c2p(xm, ym), color=WHITE, radius=0.09)

        self.add(ejes, rotulos)
        self.play(LaggedStart(*[GrowFromCenter(p) for p in puntos],
                              lag_ratio=0.05))
        self.play(FadeIn(centro), Create(recta), FadeIn(suma))
        self.play(Create(residuos))
        self.play(m.animate.set_value(1.85), run_time=1.5) # se pasa
        self.play(m.animate.set_value(m_opt), run_time=1.5)
        self.play(Write(ecuacion))
        self.wait()
