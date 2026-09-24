from manim import *


class OsciladorArmonico(Scene):
    def construct(self):
        t = ValueTracker(0)                     # reloj de la escena
        t.add_updater(lambda m, dt: m.increment_value(dt))
        A, w, g = 1.6, 3, 0.15          # amplitud, pulsación, freno

        def x(s):                               # solución exacta
            return A * np.exp(-g * s) * np.cos(w * s)

        techo = Line(LEFT * 5.8, LEFT * 4.2).shift(UP * 3.3)
        masa = always_redraw(lambda: Square(
            0.7, color=BLUE, fill_opacity=0.8).move_to(
            [-5, x(t.get_value()), 0]))

        def resorte():
            arriba, abajo = 3.3, masa.get_top()[1]
            ys = np.linspace(arriba, abajo, 26)
            xs = [-5 + (0.25 if k % 2 else -0.25) * (0 < k < 25)
                  for k in range(26)]
            return VMobject(color=GREY_A).set_points_as_corners(
                [[a, b, 0] for a, b in zip(xs, ys)])

        muelle = always_redraw(resorte)
        ejes = Axes(x_range=[0, 6.5, 1], y_range=[-2, 2, 1],
                    x_length=8, y_length=5, tips=False)
        ejes.shift(RIGHT * 1.8)
        # La gráfica se dibuja hasta el instante actual
        grafica = always_redraw(lambda: ejes.plot(
            x, x_range=[0, max(t.get_value(), 0.01)], color=YELLOW))
        enlace = always_redraw(lambda: DashedLine(
            masa.get_right(), grafica.get_end(), color=GREY))
        rotulos = ejes.get_axis_labels("t", "x(t)")
        self.add(t, techo, ejes, rotulos, masa, muelle, grafica,
                 enlace)
        for _ in range(3):
            self.wait(2)
