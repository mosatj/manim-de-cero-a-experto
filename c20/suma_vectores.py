from manim import *


class SumaVectores(Scene):
    def construct(self):
        plano = NumberPlane(x_range=[-2, 7, 1], y_range=[-1, 4, 1],
                            x_length=12.6, y_length=7)
        plano.add_coordinates(font_size=20)
        o = plano.c2p(0, 0)
        # Vector(...) nace en ORIGIN: usamos Arrow entre dos puntos
        flecha = lambda a, b, c: Arrow(plano.c2p(*a), plano.c2p(*b),
                                       buff=0, color=c)
        v = flecha((0, 0), (3, 1), YELLOW)
        w = flecha((0, 0), (1, 2), BLUE)
        nom_v = MathTex(r"\vec v", color=YELLOW).next_to(v, DOWN)
        nom_w = MathTex(r"\vec w", color=BLUE).next_to(w, LEFT)
        # Paralelogramo: w trasladado al extremo de v y viceversa
        w_tras = DashedVMobject(flecha((3, 1), (4, 3), BLUE))
        v_tras = DashedVMobject(flecha((1, 2), (4, 3), YELLOW))
        suma = flecha((0, 0), (4, 3), GREEN)
        nom_s = MathTex(r"\vec v+\vec w=(4,3)", color=GREEN)
        nom_s.next_to(plano.c2p(4, 3), RIGHT)

        self.add(plano)
        self.play(GrowArrow(v), Write(nom_v))
        self.play(GrowArrow(w), Write(nom_w))
        self.play(TransformFromCopy(w, w_tras))
        self.play(TransformFromCopy(v, v_tras))
        self.play(GrowArrow(suma), Write(nom_s))
