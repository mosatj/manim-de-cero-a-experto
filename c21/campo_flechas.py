from manim import *


def espiral(p):
    x, y = p[0], p[1]
    # Sumidero en espiral: x' = -y - 0.25x,  y' = x - 0.25y
    return np.array([-y - 0.25 * x, x - 0.25 * y, 0])


class CampoFlechas(Scene):
    def construct(self):
        campo = ArrowVectorField(
            espiral,
            x_range=[-6.8, 6.8, 0.85], y_range=[-3.4, 3.4, 0.85],
            length_func=lambda n: 0.55 * np.tanh(n / 2),
            colors=[BLUE_E, TEAL, YELLOW, RED],
            min_color_scheme_value=0, max_color_scheme_value=6)
        self.play(Create(campo, lag_ratio=0.005), run_time=2)
        # Una partícula que sigue el campo (trayectoria exacta)
        orbita = ParametricFunction(
            lambda t: 3.4 * np.exp(-0.25 * t)
            * np.array([np.cos(t), np.sin(t), 0]),
            t_range=[0, 14], color=WHITE, stroke_width=5)
        self.play(Create(orbita), run_time=3)
        self.add(Dot(orbita.get_end(), color=WHITE))
