from manim import *


class SenoYCoseno(Scene):
    def construct(self):
        circulo = Circle(radius=2.5, color=GREY_B)
        theta = ValueTracker(0.4)

        def P():  # todo depende del tracker, no de otro objeto
            return circulo.point_at_angle(theta.get_value())

        radio = always_redraw(lambda: Line(ORIGIN, P()))
        seno = always_redraw(lambda: Line(
            [P()[0], 0, 0], P(), color=RED, stroke_width=6))
        coseno = always_redraw(lambda: Line(
            ORIGIN, [P()[0], 0, 0], color=BLUE, stroke_width=6))
        punto = always_redraw(lambda: Dot(P(), color=YELLOW))
        ejes = VGroup(Line(3 * LEFT, 3 * RIGHT),
                      Line(3 * DOWN, 3 * UP))
        ejes.set_stroke(GREY, 1)
        self.add(ejes, circulo, radio, seno, coseno, punto)
        self.play(theta.animate.set_value(2.4), run_time=3)
