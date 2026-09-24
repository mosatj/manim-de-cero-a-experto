from manim import *


class Vectores(Scene):
    def construct(self):
        self.add(NumberPlane())
        u, v = np.array([3, 1, 0]), np.array([1, 2, 0])
        fu = Vector(u, color=BLUE)
        fv = Vector(v, color=GREEN)
        suma = Vector(u + v, color=YELLOW)
        # Las copias trasladadas cierran el paralelogramo
        fv2 = DashedLine(u, u + v, color=GREEN)
        fu2 = DashedLine(v, u + v, color=BLUE)
        self.add(fu, fv, fu2, fv2, suma)
        self.add(MathTex(r"\vec u + \vec v", color=YELLOW)
                 .next_to(suma.get_end(), UR, buff=0.1))
