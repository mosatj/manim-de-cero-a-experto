from manim import *


class RelojASaltos(Scene):
    def construct(self):
        esfera = Circle(radius=2.5, color=GRAY_B)
        marcas = VGroup(*[
            Line(2.2 * UP, 2.5 * UP).rotate(-k * TAU / 12,
                                            about_point=ORIGIN)
            for k in range(12)
        ])
        aguja = Line(ORIGIN, 2 * UP, color=RED, stroke_width=8)
        self.add(esfera, marcas, aguja)
        # Ritmo escalonado: 12 saltos iguales, como un segundero
        saltos = lambda t: np.floor(12 * t) / 12
        self.play(Rotate(aguja, angle=-TAU * 11 / 12,
                         about_point=ORIGIN, rate_func=saltos),
                  run_time=6)
