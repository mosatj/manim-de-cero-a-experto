from manim import *


class Corazon(Scene):
    def construct(self):
        # Dos Bézier cúbicas simétricas, unidas por sus extremos
        arriba = np.array([0, 1.5, 0])
        abajo = np.array([0, -2.5, 0])
        izq = CubicBezier(abajo, [-3.5, 0, 0], [-2.5, 3.5, 0],
                          arriba)
        der = CubicBezier(arriba, [2.5, 3.5, 0], [3.5, 0, 0],
                          abajo)
        corazon = VMobject(color=RED, fill_opacity=0.8)
        corazon.append_points(izq.points)
        corazon.append_points(der.points)
        self.add(corazon)
