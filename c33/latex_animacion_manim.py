from manim import *


class SecanteATangente(Scene):
    """Tres segundos: la secante se convierte en tangente. Con
    --format png-sequence produce los fotogramas que el paquete
    animate de LaTeX reproduce dentro del PDF."""

    def construct(self):
        ejes = Axes(x_range=[0, 4, 1], y_range=[0, 4, 1],
                    x_length=7, y_length=4.5, tips=False)
        f = lambda x: x**2 / 4
        curva = ejes.plot(f, x_range=[0, 3.8], color="#6FA3C0")
        a, h = 2, ValueTracker(1.5)

        def secante():
            b = a + h.get_value()
            m = (f(b) - f(a)) / (b - a)
            recta = ejes.plot(lambda x: f(a) + m * (x - a),
                              x_range=[0.6, 3.6], color="#B04A5A")
            return recta

        recta = always_redraw(secante)
        p = Dot(ejes.c2p(a, f(a)), color="#E0B04A")
        q = always_redraw(lambda: Dot(
            ejes.c2p(a + h.get_value(), f(a + h.get_value())),
            color="#E0B04A"))
        rotulo = always_redraw(lambda: MathTex(
            rf"h={h.get_value():.2f}").to_corner(UR))
        self.add(ejes, curva, recta, p, q, rotulo)
        self.play(h.animate.set_value(0.02), run_time=3,
                  rate_func=rate_functions.ease_in_out_sine)
