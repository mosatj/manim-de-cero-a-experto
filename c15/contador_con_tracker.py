from manim import *


class ContadorConTracker(Scene):
    def construct(self):
        recta = NumberLine(x_range=[0, 10, 1], length=11,
                           include_numbers=True).shift(DOWN)
        x = ValueTracker(2)  # un número «animable»: no se ve

        flecha = Arrow(UP, DOWN, buff=0, color=YELLOW)
        flecha.add_updater(
            lambda m: m.next_to(recta.n2p(x.get_value()), UP))
        valor = DecimalNumber(x.get_value(), num_decimal_places=2,
                              font_size=44, color=YELLOW)
        valor.add_updater(lambda m: m.set_value(x.get_value()))
        valor.add_updater(lambda m: m.next_to(flecha, UP))

        self.add(recta, flecha, valor)
        self.play(x.animate.set_value(8.5), run_time=2)
        self.play(x.animate.increment_value(-3))
        self.play(x.animate.set_value(x.get_value() * 1.2))
