from manim import *


def f(x):
    return np.sin(x) + 0.4 * np.sin(2.5 * x)


def df(x):                      # derivada exacta de f
    return np.cos(x) + np.cos(2.5 * x)


class RecorridoSuave(MovingCameraScene):
    def construct(self):
        marco = self.camera.frame
        ejes = Axes(x_range=[0, 20, 2], y_range=[-2, 2, 1],
                    x_length=24, y_length=5).add_coordinates()
        curva = ejes.plot(f, x_range=[0, 20], color=BLUE)
        x = ValueTracker(0.5)

        def tangente():
            a = x.get_value()
            color = GREEN if df(a) >= 0 else RED
            recta = Line(ejes.c2p(a - 1, f(a) - df(a)),
                         ejes.c2p(a + 1, f(a) + df(a)), color=color)
            return recta.set_length(2.5)

        recta = always_redraw(tangente)
        punto = always_redraw(lambda: Dot(
            ejes.i2gp(x.get_value(), curva), color=YELLOW))
        self.add(ejes, curva, recta, punto)
        self.play(marco.animate.set(width=7).move_to(punto))

        def seguir(m, dt):
            # Suavizado exponencial hacia un punto algo adelantado
            objetivo = punto.get_center() + 0.8 * RIGHT
            fraccion = 1 - np.exp(-3 * dt)
            m.shift((objetivo - m.get_center()) * fraccion)

        self.add(marco)
        marco.add_updater(seguir)
        self.play(x.animate.set_value(19.5), run_time=12,
                  rate_func=linear)
        marco.remove_updater(seguir)
        self.play(self.camera.auto_zoom([ejes], margin=1),
                  run_time=2)
