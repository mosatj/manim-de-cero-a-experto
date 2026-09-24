from manim import *


class TangenteViva(Scene):
    def construct(self):
        ejes = Axes(x_range=[-1, 7], y_range=[-2, 2], x_length=11,
                    y_length=5).shift(DOWN * 0.3)
        curva = ejes.plot(np.sin, x_range=[-1, 7], color=BLUE)
        x = ValueTracker(0.3)

        def recta_tangente():
            a, m = x.get_value(), np.cos(x.get_value())
            recta = Line(ejes.c2p(a - 1, np.sin(a) - m),
                         ejes.c2p(a + 1, np.sin(a) + m))
            return recta.set_length(4).set_color(YELLOW)

        # always_redraw reconstruye el objeto en cada fotograma
        tangente = always_redraw(recta_tangente)
        punto = always_redraw(lambda: Dot(
            ejes.i2gp(x.get_value(), curva), color=RED))
        pendiente = DecimalNumber(0, include_sign=True)
        f_always(pendiente.set_value, lambda: np.cos(x.get_value()))
        texto = VGroup(MathTex(r"f'(x)="), pendiente).arrange(RIGHT)
        texto.to_corner(UR)

        self.add(ejes, curva, tangente, punto, texto)
        self.play(x.animate.set_value(PI), run_time=2)
        self.play(x.animate.set_value(5.2), run_time=2)
