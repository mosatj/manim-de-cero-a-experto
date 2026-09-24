from manim import *


class Cometa(Scene):
    def construct(self):
        t = ValueTracker(0)
        t.add_updater(lambda m, dt: m.increment_value(dt))

        def lissajous(s):
            return [5 * np.sin(1.5 * s), 3 * np.sin(2 * s), 0]

        guia = ParametricFunction(lissajous, t_range=[0, 4 * PI],
                                  stroke_width=1, color=GREY)
        cabeza = always_redraw(
            lambda: Dot(lissajous(t.get_value()), color=YELLOW))
        # La estela se borra sola: cada tramo vive 1 segundo
        estela = TracedPath(cabeza.get_center, dissipating_time=1,
                            stroke_width=6, stroke_color=YELLOW)
        self.add(t, guia, cabeza, estela)
        self.wait_until(lambda: t.get_value() >= 5.2)
