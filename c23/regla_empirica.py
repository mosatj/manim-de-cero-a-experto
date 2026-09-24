from manim import *
from math import erf, sqrt


class ReglaEmpirica(Scene):
    def construct(self):
        ejes = Axes(
            x_range=[-4, 4, 1], y_range=[0, 0.45, 0.1],
            x_length=11, y_length=4.5, tips=False,
            x_axis_config={"include_numbers": True,
                           "font_size": 28},
        ).shift(0.8 * DOWN)
        curva = ejes.plot(lambda x: np.exp(-x ** 2 / 2) / sqrt(TAU),
                          color=BLUE_B)
        formula = MathTex(
            r"\varphi(z)=\frac{1}{\sqrt{2\pi}}e^{-z^2/2}",
            font_size=36).move_to(ejes.c2p(-2.6, 0.36))

        k = ValueTracker(1)
        area = always_redraw(lambda: ejes.get_area(
            curva, x_range=[-k.get_value(), k.get_value()],
            color=[BLUE_E, TEAL_D], opacity=0.8))
        # Texto fijo + dos números que cambian en cada fotograma
        izq = MathTex(r"P(|Z|\le", font_size=44)
        num_k = DecimalNumber(1, num_decimal_places=1,
                              font_size=44)
        der = MathTex(r")=", font_size=44)
        num_p = DecimalNumber(68.3, num_decimal_places=1,
                              unit=r"\%", font_size=44,
                              color=YELLOW)
        linea = VGroup(izq, num_k, der, num_p)
        linea.arrange(RIGHT, buff=0.12).to_edge(UP)
        num_k.add_updater(lambda m: m.set_value(k.get_value()))
        num_p.add_updater(lambda m: m.set_value(
            100 * erf(k.get_value() / sqrt(2))))

        self.add(ejes, curva, area, formula, linea)
        for destino in [2, 3]:
            self.play(k.animate.set_value(destino), run_time=2)
            self.wait(0.5)
