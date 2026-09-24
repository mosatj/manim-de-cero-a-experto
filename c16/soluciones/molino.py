from manim import *


class Molino(Scene):
    def construct(self):
        centro = UP * 0.8
        torre = Polygon(centro + LEFT * 0.3, centro + RIGHT * 0.3,
                        [0.7, -3, 0], [-0.7, -3, 0], color=GREY_B)
        aspa = Polygon(ORIGIN, [0.35, 2.2, 0], [-0.1, 2.2, 0],
                       color=BLUE, fill_opacity=0.7)
        aspas = VGroup(*[aspa.copy().rotate(k * PI / 2,
                                             about_point=ORIGIN)
                         for k in range(4)]).shift(centro)
        self.add(torre, aspas, Dot(centro))
        # Dos vueltas en sentido horario, a ritmo constante
        self.play(Rotating(aspas, -2 * TAU, about_point=centro,
                           run_time=4))
