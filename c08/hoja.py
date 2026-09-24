from manim import *


class Hoja(Scene):
    def construct(self):
        hoja = VMobject(color=GREEN, fill_opacity=0.5)
        base, punta = DOWN * 3, UP * 3 + RIGHT
        hoja.start_new_path(base)             # ancla inicial
        hoja.add_cubic_bezier_curve_to(       # lado derecho
            RIGHT * 3 + DOWN, RIGHT * 2 + UP * 2, punta)
        hoja.add_cubic_bezier_curve_to(       # lado izquierdo
            LEFT + UP * 3, LEFT * 3 + DOWN, base)
        nervio = ArcBetweenPoints(base, punta,
                                  angle=-PI / 6, color=YELLOW)

        self.play(DrawBorderThenFill(hoja), run_time=2)
        self.play(Create(nervio))
        n = hoja.get_num_curves()
        info = Text(f"{n} curvas, {len(hoja.points)} puntos",
                    font_size=30).to_corner(UL)
        self.play(Write(info))
        self.wait()
