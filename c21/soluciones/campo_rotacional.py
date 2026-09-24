from manim import *


class CampoRotacional(Scene):
    def construct(self):
        # El color depende del ÁNGULO del vector, no de su tamaño
        campo = ArrowVectorField(
            lambda p: np.array([-p[1], p[0], 0]),
            x_range=[-6.5, 6.5, 1], y_range=[-3.5, 3.5, 1],
            color_scheme=lambda v: np.arctan2(v[1], v[0]) % TAU,
            min_color_scheme_value=0, max_color_scheme_value=TAU,
            colors=[RED, YELLOW, GREEN, BLUE, PURPLE, RED])
        self.play(Create(campo, lag_ratio=0.01), run_time=2)
