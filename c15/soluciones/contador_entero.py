from manim import *


class ContadorEntero(Scene):
    def construct(self):
        n = ValueTracker(0)
        numero = Integer(0, font_size=120)
        numero.add_updater(lambda m: m.set_value(n.get_value()))
        barra = Rectangle(width=0.1, height=0.4, color=BLUE,
                          fill_opacity=1).align_to(LEFT * 5, LEFT)
        barra.shift(DOWN * 2)
        barra.add_updater(lambda m: m.stretch_to_fit_width(
            0.1 + n.get_value() / 10).align_to(LEFT * 5, LEFT))
        self.add(numero, barra)
        self.play(n.animate.set_value(100), run_time=3,
                  rate_func=linear)
