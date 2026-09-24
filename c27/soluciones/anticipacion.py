from manim import *

FACTORES = [-0.2, -0.5, -1.0]


class Anticipacion(Scene):
    def construct(self):
        for i, factor in enumerate(FACTORES):
            y = 2 - 2 * i
            inicio, fin = np.array([-1, y, 0]), np.array([5.5, y, 0])
            puntos = VGroup(*[
                Dot(inicio + running_start(k / 12, pull_factor=factor)
                    * (fin - inicio), radius=0.09, color=BLUE)
                for k in range(13)])
            rotulo = Text(f"pull_factor={factor}", font="Monospace",
                          font_size=24)
            rotulo.next_to([-4.1, y, 0], LEFT, buff=0)
            self.add(Line(inicio, fin, stroke_width=1, color=GREY_D),
                     puntos, rotulo)
        cuadrado = Square(0.6, color=ORANGE, fill_opacity=1)
        cuadrado.move_to([-1, -3.2, 0])
        ritmo = lambda t: running_start(t, pull_factor=-0.5)
        self.play(cuadrado.animate.shift(6.5 * RIGHT), run_time=1.5,
                  rate_func=ritmo)
