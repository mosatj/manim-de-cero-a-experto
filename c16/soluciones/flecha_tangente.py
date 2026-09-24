from manim import *


class FlechaTangente(Scene):
    def construct(self):
        R = 2.5
        circulo = Circle(radius=R, color=GREY_B)
        theta = ValueTracker(0)

        def flecha():
            a = theta.get_value()
            p = R * np.array([np.cos(a), np.sin(a), 0])
            tangente = np.array([-np.sin(a), np.cos(a), 0])
            return Arrow(p, p + 1.5 * tangente, buff=0,
                         color=YELLOW)

        velocidad = always_redraw(flecha)
        self.add(circulo, velocidad)
        self.play(theta.animate.set_value(0.8 * TAU), run_time=4,
                  rate_func=linear)
