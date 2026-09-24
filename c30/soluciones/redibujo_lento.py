from manim import *


class RedibujoLento(Scene):
    def construct(self):
        t = ValueTracker(0)
        # En cada fotograma se construye otra cuadrícula entera
        plano = always_redraw(
            lambda: NumberPlane().rotate(t.get_value()))
        self.add(plano)
        self.play(t.animate.set_value(PI / 6), run_time=6)
