from manim import *


class PuntosEnCirculo(Scene):
    def construct(self):
        rng = np.random.default_rng(3)
        n = 16
        puntos = VGroup(*[
            Dot([rng.uniform(-6, 6), rng.uniform(-3, 3), 0])
            for _ in range(n)
        ]).set_color_by_gradient(BLUE, RED)
        self.add(puntos)
        puntos.generate_target()
        for k, punto in enumerate(puntos.target):
            angulo = k * TAU / n
            punto.move_to(2.5 * np.array([np.cos(angulo),
                                          np.sin(angulo), 0]))
        self.play(MoveToTarget(puntos, run_time=2))
