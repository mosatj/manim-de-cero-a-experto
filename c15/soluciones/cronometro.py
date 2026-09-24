from manim import *


class Cronometro(Scene):
    def construct(self):
        t = ValueTracker(0)
        lectura = DecimalNumber(0, unit=r"\mathrm{s}",
                                unit_buff_per_font_unit=0.004,
                                font_size=96)
        lectura.add_updater(lambda m: m.set_value(t.get_value()))

        def correr(m, dt):
            m.increment_value(dt)
            if m.get_value() >= 3:        # meta alcanzada:
                m.set_value(3)
                m.remove_updater(correr)  # se retira solo

        t.add_updater(correr)
        self.add(t, lectura)
        self.wait(5)
