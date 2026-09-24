from manim import *


class HexagonoLadoALado(Scene):
    def construct(self):
        hexagono = RegularPolygon(n=6, radius=2.6)
        vertices = hexagono.get_vertices()
        lados = VGroup(*[
            Line(vertices[i], vertices[(i + 1) % 6], stroke_width=6,
                 color=interpolate_color(BLUE, RED, i / 5))
            for i in range(6)
        ])
        puntos = VGroup(*[Dot(v, radius=0.1) for v in vertices])
        centro = Dot(color=RED)
        radios = VGroup(*[DashedLine(ORIGIN, v, color=GRAY)
                          for v in vertices])

        self.play(LaggedStartMap(GrowFromCenter, puntos,
                                 lag_ratio=0.2))
        # Cada lado empieza cuando el anterior terminó
        self.play(Succession(*[Create(l) for l in lados],
                             run_time=3, rate_func=linear))
        # arg_creator: cada radio discontinuo se pasa entero
        self.play(GrowFromCenter(centro),
                  LaggedStartMap(Create, radios, lag_ratio=0.15,
                                 arg_creator=lambda m: (m,)))
