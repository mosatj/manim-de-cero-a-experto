from manim import *


class Termometro(Scene):
    def construct(self):
        temperatura = ValueTracker(10)       # entre 0 y 40 grados
        tubo = RoundedRectangle(corner_radius=0.3, width=0.8,
                                height=6)

        def columna():
            t = temperatura.get_value()
            alto = 0.1 + 5.8 * t / 40
            color = interpolate_color(BLUE, RED, t / 40)
            barra = Rectangle(width=0.6, height=alto, color=color,
                              fill_opacity=1)
            return barra.align_to(tubo, DOWN).shift(UP * 0.1)

        mercurio = always_redraw(columna)
        lectura = DecimalNumber(10, num_decimal_places=1,
                                unit=r"^\circ\mathrm{C}")
        lectura.add_updater(
            lambda m: m.set_value(temperatura.get_value()))
        lectura.add_updater(
            lambda m: m.next_to(mercurio, RIGHT, buff=0.8)
            .align_to(mercurio, UP))
        self.add(tubo, mercurio, lectura)
        self.play(temperatura.animate.set_value(36.5), run_time=3)
