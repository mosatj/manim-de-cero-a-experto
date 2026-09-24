from manim import *


class Superposicion(Scene):
    def construct(self):
        alturas = [1.2, 2.5, 1.8, 3.4, 2.9, 4.1, 3.6]
        barras = VGroup(*[
            Rectangle(width=0.8, height=h, fill_opacity=0.9,
                      color=interpolate_color(BLUE, TEAL, k / 6))
            for k, h in enumerate(alturas)
        ]).arrange(RIGHT, buff=0.3, aligned_edge=DOWN).shift(DOWN)
        suelo = Line(5 * LEFT, 5 * RIGHT, color=GREY_B)
        suelo.next_to(barras, DOWN, buff=0)
        self.add(suelo)
        # lag_ratio < 1: cada barra arranca antes de que acabe la previa
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in barras],
                              lag_ratio=0.25, run_time=2.5))
        self.play(LaggedStart(*[b.animate.set_color(YELLOW)
                                for b in barras[3::2]], lag_ratio=0.4))
        self.play(barras[-2].animate.set_color(RED))
