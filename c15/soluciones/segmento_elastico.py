from manim import *


class SegmentoElastico(Scene):
    def construct(self):
        a = Dot(LEFT * 3, color=YELLOW)
        b = Dot(RIGHT * 3, color=YELLOW)
        segmento = always_redraw(lambda: Line(
            a.get_center(), b.get_center(), color=BLUE))
        largo = always_redraw(lambda: DecimalNumber(
            segmento.get_length()).next_to(segmento, UP))
        self.add(segmento, largo, a, b)
        self.play(a.animate.shift(2 * UP), b.animate.shift(DL))
