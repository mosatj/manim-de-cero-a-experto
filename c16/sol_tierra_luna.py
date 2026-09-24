from manim import *


class SolTierraLuna(Scene):
    def construct(self):
        sol = Dot(radius=0.3, color=YELLOW)
        tierra = Dot(RIGHT * 2.6, radius=0.15, color=BLUE)
        luna = Dot(RIGHT * 3.4, radius=0.07, color=GREY_A)
        sistema = VGroup(tierra, luna)
        anio = ValueTracker(0)          # años transcurridos
        T = 6                           # segundos de vídeo por año

        anio.add_updater(lambda m, dt: m.increment_value(dt / T))
        # El grupo gira alrededor del Sol: arrastra a la Luna...
        always_rotate(sistema, rate=TAU / T, about_point=ORIGIN)
        # ...y la Luna, además, da 6 vueltas por año a la Tierra
        luna.add_updater(lambda m, dt: m.rotate(
            6 * TAU * dt / T, about_point=tierra.get_center()))
        rastro = TracedPath(luna.get_center, stroke_color=GREY_A,
                            stroke_width=2)

        self.add(anio, sol, sistema, rastro)
        # wait_until: esperar hasta que se cumpla una condición
        self.wait_until(lambda: anio.get_value() >= 1)
