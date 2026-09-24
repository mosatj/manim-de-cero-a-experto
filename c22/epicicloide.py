from manim import *


class Epicicloide(Scene):
    k = 3                     # razón R/r entre los radios

    def construct(self):
        R = 3.2 / (1 + 2 / self.k)      # la curva cabe en pantalla
        r = R / self.k
        fija = Circle(R, color=GRAY)
        # Punto de una rueda de radio r que rueda POR FUERA
        def punto(t):
            return np.array([(R + r) * np.cos(t)
                             - r * np.cos((R + r) / r * t),
                             (R + r) * np.sin(t)
                             - r * np.sin((R + r) / r * t), 0])
        def centro(t):
            return (R + r) * np.array([np.cos(t), np.sin(t), 0])
        t = ValueTracker(0.001)
        rueda = always_redraw(lambda: Circle(r, color=BLUE)
                              .move_to(centro(t.get_value())))
        traza = always_redraw(lambda: ParametricFunction(
            punto, t_range=[0, t.get_value()], color=YELLOW))
        marca = always_redraw(lambda: Dot(punto(t.get_value()),
                                          color=RED))
        self.add(fija, traza, rueda, marca)
        self.play(t.animate.set_value(TAU), run_time=6,
                  rate_func=linear)
        self.add(MathTex(rf"k = R/r = {self.k}").to_corner(UL))


class Cardioide(Epicicloide):
    k = 1                    # una sola cúspide: la cardioide
