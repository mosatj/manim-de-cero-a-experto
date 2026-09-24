from manim import *


class Gota(Scene):
    def construct(self):
        gota = VMobject(color=BLUE, fill_opacity=0.6)
        punta, fondo = UP * 3, DOWN * 2.5
        gota.start_new_path(punta)
        gota.add_cubic_bezier_curve_to(      # lado derecho
            RIGHT * 0.5 + UP * 1.5, RIGHT * 2.5 + DOWN * 2,
            fondo)
        gota.add_cubic_bezier_curve_to(      # lado izquierdo
            LEFT * 2.5 + DOWN * 2, LEFT * 0.5 + UP * 1.5,
            punta)
        self.play(DrawBorderThenFill(gota), run_time=2)
        self.wait()
