from manim import *


class SecanteTangente(Scene):
    def construct(self):
        ejes = Axes(x_range=[-0.5, 4.5, 1], y_range=[-0.5, 6, 1],
                    x_length=7, y_length=6.5, tips=False)
        ejes.add_coordinates().to_edge(LEFT, buff=0.6)
        f = lambda x: x**2 / 4 + 1
        curva = ejes.plot(f, x_range=[-0.5, 4.5], color=BLUE)
        a = 2                                   # punto de tangencia
        h = ValueTracker(2)                     # incremento (h ≠ 0)

        # Secante por P(a, f(a)) y Q(a+h, f(a+h)) con su triángulo
        secante = always_redraw(lambda: ejes.get_secant_slope_group(
            x=a, graph=curva, dx=h.get_value(),
            dx_line_color=GREEN, dy_line_color=GREEN,
            secant_line_color=YELLOW, secant_line_length=7))
        P = Dot(ejes.c2p(a, f(a)), color=RED)
        Q = always_redraw(lambda: Dot(
            ejes.c2p(a + h.get_value(), f(a + h.get_value())),
            color=YELLOW))

        def pendiente():              # m(h) = (f(a+h) - f(a)) / h
            return (f(a + h.get_value()) - f(a)) / h.get_value()
        v_h = DecimalNumber(2, num_decimal_places=3)
        v_h.add_updater(lambda m: m.set_value(h.get_value()))
        v_m = DecimalNumber(2, num_decimal_places=3, color=YELLOW)
        v_m.add_updater(lambda m: m.set_value(pendiente()))
        fila_h = VGroup(MathTex("h ="), v_h).arrange(RIGHT)
        fila_m = VGroup(MathTex(r"m_{\text{sec}} =", color=YELLOW),
                        v_m).arrange(RIGHT)
        cociente = MathTex(r"m_{\text{sec}}=\frac{f(2+h)-f(2)}{h}")
        panel = VGroup(cociente, fila_h, fila_m)
        panel.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        panel.to_edge(RIGHT, buff=0.6).shift(UP)

        tangente = DashedLine(ejes.c2p(0, 0), ejes.c2p(4.5, 4.5),
                              color=RED)    # y = x, pues f'(2) = 1
        limite = MathTex(r"f'(2)=\lim_{h\to 0}(1+h/4)=1",
                         color=RED).next_to(panel, DOWN, buff=0.6)
        limite.align_to(panel, LEFT)

        self.play(Create(ejes), Create(curva))
        self.play(FadeIn(P, Q, secante), Write(panel))
        self.play(h.animate.set_value(1), run_time=2)
        self.play(h.animate.set_value(0.05), run_time=3)
        self.play(Create(tangente))
        self.play(Write(limite))
