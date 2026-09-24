from manim import *


class RestaVectores(Scene):
    def construct(self):
        plano = NumberPlane(x_range=[-1, 5], y_range=[-2, 3],
                            x_length=8.4, y_length=7)
        p = plano.c2p
        v = Arrow(p(0, 0), p(3, 1), buff=0, color=YELLOW)
        w = Arrow(p(0, 0), p(1, 2), buff=0, color=BLUE)
        # v − w va del extremo de w al extremo de v: w + (v − w) = v
        dif = Arrow(p(1, 2), p(3, 1), buff=0, color=RED)
        dif_origen = Arrow(p(0, 0), p(2, -1), buff=0, color=RED)
        nombres = VGroup(
            MathTex(r"\vec v", color=YELLOW).next_to(v, DOWN),
            MathTex(r"\vec w", color=BLUE).next_to(w, LEFT),
            MathTex(r"\vec v-\vec w=(2,-1)", color=RED)
            .next_to(dif, UR, buff=0.1))
        self.add(plano, v, w, nombres)
        self.play(GrowArrow(dif))
        self.play(TransformFromCopy(dif, dif_origen))
