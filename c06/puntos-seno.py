from manim import *


class PuntosSeno(Scene):
    def construct(self):
        x = np.linspace(-6, 6, 61)      # 61 abscisas equiespaciadas
        y = 2 * np.sin(x)                 # 61 ordenadas de una vez
        puntos = VGroup(*[
            Dot([xi, yi, 0], radius=0.06,
                color=interpolate_color(BLUE, YELLOW, (yi + 2) / 4))
            for xi, yi in zip(x, y)
        ])
        eje = Line(6.5 * LEFT, 6.5 * RIGHT, color=GREY)
        self.add(eje)
        self.play(LaggedStart(*[FadeIn(p, scale=3) for p in puntos],
                              lag_ratio=0.05))
