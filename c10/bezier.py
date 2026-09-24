from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class Bezier(Scene):
    def construct(self):
        p0, p1 = np.array([-5, -2, 0]), np.array([-3, 2.5, 0])
        p2, p3 = np.array([3, -3, 0]), np.array([5, 1.5, 0])
        curva = CubicBezier(p0, p1, p2, p3, color=YELLOW,
                            stroke_width=8)
        # Asideros: cada ancla unida a su punto de control
        asas = VGroup(DashedLine(p0, p1), DashedLine(p3, p2))
        asas.set_color(GRAY)
        puntos = VGroup(Dot(p0, color=BLUE), Dot(p1, color=RED),
                        Dot(p2, color=RED), Dot(p3, color=BLUE))
        nombres = ["ancla inicial", "control 1", "control 2",
                   "ancla final"]
        lados = [DOWN, RIGHT, DOWN, UP]
        for p, t, lado in zip(puntos, nombres, lados):
            self.add(Text(t, font_size=24).next_to(p, lado))
        self.add(asas, curva, puntos)
        self.add(MathTex(r"B(t)=(1-t)^3P_0+3(1-t)^2tP_1"
                         r"+3(1-t)t^2P_2+t^3P_3",
                         font_size=36).to_edge(UP))
