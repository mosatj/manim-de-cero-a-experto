from manim import *


class BezierAMano(Scene):
    def construct(self):
        self.add(NumberPlane(background_line_style={
            "stroke_opacity": 0.4}))
        # Dos cúbicas: [ancla, asa, asa, ancla] cada una
        curva = VMobject(color=GREEN, stroke_width=6)
        curva.set_points([
            [-4, -1, 0], [-5, 2, 0], [-1, 3, 0], [0, 1, 0],
            [0, 1, 0], [1, -1, 0], [5, 3, 0], [4, -2, 0],
        ])
        p = curva.points
        # Segmentos ancla-asa (índices 0-1, 2-3, 4-5, 6-7)
        palancas = VGroup(*[
            Line(p[i], p[i + 1], color=RED, stroke_width=2)
            for i in range(0, len(p), 2)])
        asas = VGroup(*[Dot(p[i], color=RED)
                        for i in (1, 2, 5, 6)])
        anclas = VGroup(*[Dot(p[i], color=YELLOW, radius=0.1)
                          for i in (0, 3, 7)])
        self.add(palancas, curva, asas, anclas)
        self.play(Create(curva), run_time=2)
        self.wait()
