from manim import *


class Cicloide(Scene):
    def construct(self):
        r, x0, y0 = 0.8, -5, -2      # radio, inicio, suelo
        giro = ValueTracker(0)      # ángulo girado (rad)

        def centro():               # sin deslizar: avanza r·giro
            return np.array([x0 + r * giro.get_value(), y0 + r, 0])

        def marca(s):               # punto de la llanta
            return np.array([x0 + r * (s - np.sin(s)),
                             y0 + r * (1 - np.cos(s)), 0])

        modelo = VGroup(Circle(radius=r, color=BLUE), *[
            Line(ORIGIN, r * DOWN, color=GREY_B).rotate(
                k * TAU / 6, about_point=ORIGIN) for k in range(6)])
        rueda = always_redraw(lambda: modelo.copy().rotate(
            -giro.get_value()).move_to(centro()))
        # El trazo sale de la fórmula: no depende de los fotogramas
        trazo = always_redraw(lambda: ParametricFunction(
            marca, t_range=[0, max(giro.get_value(), 1e-3)],
            color=YELLOW, stroke_width=4))
        punto = always_redraw(lambda: Dot(marca(giro.get_value()),
                                          color=RED))
        # Centro instantáneo de rotación: el punto de contacto
        contacto = always_redraw(lambda: Dot(centro() + r * DOWN,
                                             color=GREEN))
        radio_vector = always_redraw(lambda: DashedLine(
            centro() + r * DOWN, marca(giro.get_value()),
            color=GREEN))
        suelo = Line([-6.5, y0, 0], [6.5, y0, 0], color=GREY)

        self.add(suelo, trazo, rueda, radio_vector, contacto, punto)
        for final, tiempo in [(PI, 2), (2 * PI, 2), (3.3 * PI, 3)]:
            self.play(giro.animate.set_value(final),
                      run_time=tiempo, rate_func=linear)
