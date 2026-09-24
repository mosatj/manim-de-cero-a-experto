from manim import *


class Luna(Scene):
    def construct(self):
        disco = Circle(2, color=YELLOW_A)
        sombra = Circle(1.8).shift(0.9 * RIGHT + 0.3 * UP)
        luna = Difference(disco, sombra, color=YELLOW_A,
                          fill_opacity=1, stroke_width=0)
        luna.shift(2 * LEFT)
        rng = np.random.default_rng(7)     # cielo reproducible
        estrellas = VGroup(*[
            Star(5, outer_radius=r, color=WHITE, fill_opacity=1)
            .move_to([x, y, 0])
            for x, y, r in zip(rng.uniform(0, 6.5, 14),
                               rng.uniform(-3.5, 3.5, 14),
                               rng.uniform(0.05, 0.2, 14))
        ])
        self.add(luna, estrellas)
