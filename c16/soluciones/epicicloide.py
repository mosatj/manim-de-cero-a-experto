from manim import *


class Epicicloide(Scene):
    def construct(self):
        R, r = 1.8, 0.6            # fijo y rodante: R/r = 3
        giro = ValueTracker(0)     # ángulo del centro rodante
        k = (R + r) / r            # la rueda gira k veces más

        def centro(s):
            return (R + r) * np.array([np.cos(s), np.sin(s), 0])

        def marca(s):              # epicicloide
            return centro(s) - r * np.array(
                [np.cos(k * s), np.sin(k * s), 0])

        fijo = Circle(radius=R, color=GREY_B)
        rodante = always_redraw(lambda: Circle(radius=r, color=BLUE)
                                .move_to(centro(giro.get_value())))
        trazo = always_redraw(lambda: ParametricFunction(
            marca, t_range=[0, max(giro.get_value(), 1e-3)],
            color=YELLOW))
        punto = always_redraw(lambda: Dot(marca(giro.get_value()),
                                          color=RED))
        self.add(fijo, trazo, rodante, punto)
        self.play(giro.animate.set_value(TAU), run_time=6,
                  rate_func=linear)
