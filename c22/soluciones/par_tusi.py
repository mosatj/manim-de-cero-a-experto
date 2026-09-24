from manim import *


class ParTusi(Scene):
    def construct(self):
        R = 3                                # k = R/r = 2
        r = R / 2
        fija = Circle(R, color=GRAY)
        # Hipocicloide: la rueda gira POR DENTRO de la fija
        def punto(t):
            return np.array([(R - r) * np.cos(t)
                             + r * np.cos((R - r) / r * t),
                             (R - r) * np.sin(t)
                             - r * np.sin((R - r) / r * t), 0])
        t = ValueTracker(0.001)
        rueda = always_redraw(lambda: Circle(r, color=BLUE).move_to(
            (R - r) * np.array([np.cos(t.get_value()),
                                np.sin(t.get_value()), 0])))
        traza = always_redraw(lambda: ParametricFunction(
            punto, t_range=[0, t.get_value()], color=YELLOW,
            stroke_width=6))
        marca = always_redraw(lambda: Dot(punto(t.get_value()),
                                          color=RED))
        self.add(fija, traza, rueda, marca)
        self.play(t.animate.set_value(3 * PI / 4), run_time=3,
                  rate_func=linear)
