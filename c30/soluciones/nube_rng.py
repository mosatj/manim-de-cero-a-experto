import numpy as np
from manim import *


class NubeRng(Scene):
    def construct(self):
        # --seed siembra np.random (el generador antiguo), pero
        # no los generadores nuevos: la semilla se da al crearlos
        rng = np.random.default_rng(2026)
        xy = rng.normal(0, 1.2, size=(300, 2))
        puntos = VGroup(*[Dot([x, y, 0], radius=0.04, color=BLUE_E)
                          for x, y in xy])
        self.add(puntos)
        media = xy.mean(axis=0)
        cruz = Cross(Square(0.3), color=RED_E).move_to([*media, 0])
        rotulo = Text(f"media: ({media[0]:.3f}, {media[1]:.3f})",
                      font_size=30).to_edge(DOWN)
        self.add(cruz, rotulo)
