from manim import *


class FlujoDeCizalla(Scene):
    def construct(self):
        ys, xs = np.arange(-2, 2.1, 0.5), np.arange(-3, 3.1, 0.5)
        malla = VGroup(
            *[Line([-3, y, 0], [3, y, 0]) for y in ys],
            *[Line([x, -2, 0], [x, 2, 0]) for x in xs],
        ).set_stroke(BLUE, 2)
        mancha = Circle(radius=1, color=YELLOW, fill_opacity=0.5)
        fluido = VGroup(malla, mancha).shift(LEFT * 1.5)
        fondo = fluido.copy().set_opacity(0.15)

        # Velocidad v(x, y) = (0.8 y, 0): capas que se deslizan
        def velocidad(p):
            return np.array([0.8 * p[1], 0, 0])

        self.add(fondo)
        self.play(PhaseFlow(velocidad, fluido, virtual_time=2),
                  run_time=3)
