from manim import *


class TangenteUnitaria(Scene):
    def construct(self):
        R, t = 2.5, 50 * DEGREES
        O = ORIGIN
        P = R * np.array([np.cos(t), np.sin(t), 0])
        T = R * np.array([1, np.tan(t), 0])   # corte con x = 1
        self.add(Circle(R, color=GRAY),
                 Line(2.8 * LEFT, 3.5 * RIGHT),
                 Line(2.8 * DOWN, 3.8 * UP))
        tangente = Line(R * RIGHT, T, color=YELLOW, stroke_width=6)
        self.play(Create(Line(O, T, color=WHITE)), Create(tangente),
                  Create(Line([P[0], 0, 0], P, color=RED)),
                  Create(Line(O, [P[0], 0, 0], color=BLUE)))
        self.add(Dot(P), Dot(T, color=YELLOW),
                 MathTex(r"\tan\theta", color=YELLOW)
                 .next_to(tangente, RIGHT),
                 Angle(Line(O, RIGHT), Line(O, P), radius=0.6))
