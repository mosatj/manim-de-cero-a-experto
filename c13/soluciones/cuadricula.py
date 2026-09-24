from manim import *


class Cuadricula(Scene):
    def construct(self):
        puntos = VGroup(*[Dot(radius=0.12) for _ in range(12 * 7)])
        puntos.arrange_in_grid(rows=7, cols=12, buff=0.6)
        puntos.set_color_by_gradient(BLUE, TEAL, YELLOW)
        # 84 puntos: un lag_ratio pequeño acota la duración
        self.play(LaggedStartMap(FadeIn, puntos, shift=0.5 * DOWN,
                                 lag_ratio=0.03, run_time=3))
