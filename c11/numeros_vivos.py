from manim import *


class NumerosVivos(Scene):
    def construct(self):
        # DecimalNumber: un número con formato, que puede cambiar
        pi_aprox = DecimalNumber(3.14159, num_decimal_places=4,
                                 font_size=72)
        # Con signo explícito y unidad (la unidad es LaTeX)
        temperatura = DecimalNumber(-2.5, include_sign=True,
                                    unit=r"^\circ\mathrm{C}")
        # Integer: un DecimalNumber sin decimales
        contador = Integer(0, font_size=72, color=YELLOW)
        # Variable: etiqueta = valor, con su propio ValueTracker
        x = Variable(1.0, "x", num_decimal_places=2)
        grupo = VGroup(pi_aprox, temperatura, contador, x)
        grupo.arrange(DOWN, buff=0.6)
        self.add(grupo)
        self.play(ChangeDecimalToValue(contador, 100), run_time=2)
        self.play(x.tracker.animate.set_value(2.72))
        self.wait()
