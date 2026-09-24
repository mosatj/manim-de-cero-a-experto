from manim import *


class TangenteSeno(Scene):
    def construct(self):
        ejes = Axes(x_range=[-0.5, 6.5, 1], y_range=[-1.5, 1.5, 1],
                    x_length=11, y_length=4, tips=False)
        ejes.add_coordinates(font_size=22)
        curva = ejes.plot(np.sin, x_range=[0, 6.3], color=BLUE)
        x = ValueTracker(0)

        def tangente():
            x0 = x.get_value()
            p = ejes.c2p(x0, np.sin(x0))
            # Dirección (1, cos x0) en unidades de pantalla
            d = ejes.c2p(x0 + 1, np.sin(x0) + np.cos(x0)) - p
            d = 1.2 * d / np.linalg.norm(d)
            return Line(p - d, p + d, color=YELLOW)

        tang = always_redraw(tangente)
        punto = always_redraw(lambda: Dot(
            ejes.i2gp(x.get_value(), curva), color=YELLOW))
        valor = DecimalNumber(1, num_decimal_places=3)
        valor.add_updater(
            lambda m: m.set_value(np.cos(x.get_value())))
        panel = VGroup(MathTex(r"\cos x_0 ="), valor).arrange(RIGHT)
        panel.set_color(YELLOW).to_corner(UR)
        self.add(ejes, curva, tang, punto, panel)
        self.play(x.animate.set_value(2 * PI - 0.2), run_time=6,
                  rate_func=linear)
