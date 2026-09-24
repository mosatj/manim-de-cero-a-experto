from manim import *


class SecanteParabola(Scene):
    def construct(self):
        ejes = Axes(x_range=[-0.5, 3.5, 1], y_range=[-1, 9, 1],
                    x_length=7, y_length=6.5, tips=False)
        ejes.add_coordinates(font_size=22).to_edge(LEFT)
        f = lambda x: x**2
        curva = ejes.plot(f, x_range=[-0.5, 3], color=BLUE)
        h = ValueTracker(2)
        secante = always_redraw(lambda: ejes.get_secant_slope_group(
            x=1, graph=curva, dx=h.get_value(),
            secant_line_color=YELLOW, secant_line_length=6))
        v_m = DecimalNumber(4, num_decimal_places=3, color=YELLOW)
        v_m.add_updater(lambda m: m.set_value(2 + h.get_value()))
        panel = VGroup(MathTex(r"m(h)=2+h=", color=YELLOW), v_m)
        panel.arrange(RIGHT).to_edge(RIGHT).shift(UP)
        self.add(ejes, curva, secante, panel)
        self.play(h.animate.set_value(0.01), run_time=4)
        tangente = ejes.plot(lambda x: 2 * x - 1, x_range=[-0.2, 3],
                             color=RED)
        self.play(Create(tangente))
