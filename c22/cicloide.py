from manim import *


class Cicloide(Scene):
    def construct(self):
        r = 0.9                               # radio de la rueda
        x0 = -2 * PI * r              # caben dos vueltas
        suelo = Line([x0 - 0.5, -1, 0], [-x0 + 0.5, -1, 0],
                     color=GRAY)
        # Punto de la rueda tras girar un ángulo t (sin deslizar)
        punto = lambda t: np.array([x0 + r * (t - np.sin(t)),
                                    -1 + r * (1 - np.cos(t)), 0])
        centro = lambda t: np.array([x0 + r * t, -1 + r, 0])
        t = ValueTracker(0.001)
        rueda = always_redraw(lambda: Circle(r, color=BLUE)
                              .move_to(centro(t.get_value())))
        radio = always_redraw(lambda: Line(centro(t.get_value()),
                                           punto(t.get_value())))
        traza = always_redraw(lambda: ParametricFunction(
            punto, t_range=[0, t.get_value()], color=YELLOW))
        marca = always_redraw(lambda: Dot(punto(t.get_value()),
                                          color=RED))
        self.add(suelo, traza, rueda, radio, marca)
        self.play(t.animate.set_value(4 * PI), run_time=6,
                  rate_func=linear)
        formula = MathTex(r"x = r(t - \sin t),",
                          r"\quad y = r(1 - \cos t)")
        self.add(formula.to_edge(UP, buff=0.8))
