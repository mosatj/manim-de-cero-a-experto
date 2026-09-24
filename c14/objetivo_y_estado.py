from manim import *


class ObjetivoYEstado(Scene):
    def construct(self):
        rng = np.random.default_rng(7)
        puntos = VGroup(*[
            Dot([rng.uniform(-6, 6), rng.uniform(-3, 3), 0],
                radius=0.14)
            for _ in range(24)
        ]).set_color_by_gradient(BLUE, YELLOW)
        self.play(FadeIn(puntos, lag_ratio=0.1))

        # 1) Preparar un objetivo y moverse hacia él
        puntos.generate_target()
        puntos.target.arrange_in_grid(rows=4, buff=0.6)
        self.play(MoveToTarget(puntos))

        # 2) Guardar este estado, cambiar y volver
        puntos.save_state()
        self.play(puntos.animate.scale(0.4).set_color(RED)
                  .to_edge(LEFT))
        self.play(Restore(puntos))
