from manim import *


class LimiteEpsilonDelta(Scene):
    def construct(self):
        ejes = Axes(x_range=[-4, 4, 1], y_range=[-0.5, 1.5, 0.5],
                    x_length=11, y_length=5.6, tips=False)
        ejes.add_coordinates().shift(0.4 * DOWN)
        f = lambda x: np.sinc(x / PI)   # sen(x)/x sin dividir por 0
        curva = ejes.plot(f, x_range=[-4, 4], color=BLUE)
        # f no está definida en 0: dibujamos un hueco en (0, 1)
        hueco = Circle(radius=0.07, color=BLUE).set_z_index(5)
        hueco.set_fill(BLACK, 1).move_to(ejes.c2p(0, 1))

        eps = ValueTracker(0.4)
        # Con δ = √(6ε) se cumple |f(x) − 1| < ε si 0 < |x| < δ
        delta = lambda: np.sqrt(6 * eps.get_value())

        def banda_eps():
            e = eps.get_value()
            return Polygon(ejes.c2p(-4, 1 - e), ejes.c2p(4, 1 - e),
                           ejes.c2p(4, 1 + e), ejes.c2p(-4, 1 + e),
                           stroke_width=0, fill_color=YELLOW,
                           fill_opacity=0.25)

        def banda_delta():
            d = delta()
            return Polygon(ejes.c2p(-d, -0.5), ejes.c2p(d, -0.5),
                           ejes.c2p(d, 1.5), ejes.c2p(-d, 1.5),
                           stroke_width=0, fill_color=GREEN,
                           fill_opacity=0.25)

        franja_e = always_redraw(banda_eps)
        franja_d = always_redraw(banda_delta)
        # La gráfica sobre (−δ, δ) debe quedar dentro de la franja ε
        trozo = always_redraw(lambda: ejes.plot(
            f, x_range=[-delta(), delta()], color=WHITE,
            stroke_width=6))

        v_eps = DecimalNumber(0.4, num_decimal_places=3)
        v_eps.add_updater(lambda m: m.set_value(eps.get_value()))
        v_del = DecimalNumber(delta(), num_decimal_places=3)
        v_del.add_updater(lambda m: m.set_value(delta()))
        rot_e = MathTex(r"\varepsilon=", color=YELLOW)
        rot_d = MathTex(r"\delta=\sqrt{6\varepsilon}=", color=GREEN)
        panel = VGroup(VGroup(rot_e, v_eps).arrange(RIGHT),
                       VGroup(rot_d, v_del).arrange(RIGHT))
        panel.arrange(DOWN, aligned_edge=LEFT).to_corner(UR)
        limite = MathTex(
            r"\lim_{x\to 0}\frac{\operatorname{sen}x}{x}=1"
        ).to_corner(UL)

        self.add(hueco)
        self.play(Create(ejes), Create(curva), Write(limite))
        self.play(FadeIn(franja_e), FadeIn(panel[0]))
        self.play(FadeIn(franja_d), Create(trozo), FadeIn(panel[1]))
        self.play(eps.animate.set_value(0.12), run_time=2)
        self.play(eps.animate.set_value(0.04), run_time=2)
