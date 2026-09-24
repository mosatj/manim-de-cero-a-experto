from manim import *

AZUL, VERDE, ROJO = BLUE, GREEN, RED


class PitagorasColores(Scene):
    def construct(self):
        # Triángulo rectángulo de catetos 3 y 4 (escala 0.8)
        A, B, C = ORIGIN, 3.2 * RIGHT, 2.4 * UP
        cat_a = Line(A, C, color=AZUL, stroke_width=6)
        cat_b = Line(A, B, color=VERDE, stroke_width=6)
        hipo = Line(B, C, color=ROJO, stroke_width=6)
        recto = RightAngle(cat_b, cat_a, length=0.3, color=GRAY)
        la = MathTex("a", color=AZUL).next_to(cat_a, LEFT)
        lb = MathTex("b", color=VERDE).next_to(cat_b, DOWN)
        lc = MathTex("c", color=ROJO).move_to(hipo).shift(0.35 * UR)
        triangulo = VGroup(cat_a, cat_b, hipo, recto, la, lb, lc)
        # Fórmula y versión numérica, con los mismos colores
        mapa = {"a^2": AZUL, "b^2": VERDE, "c^2": ROJO}
        simbolica = MathTex("a^2", "+", "b^2", "=", "c^2",
                            font_size=80, tex_to_color_map=mapa)
        numeros = MathTex("3^2", "+", "4^2", "=", "5^2",
                          font_size=64)
        for k, color in zip([0, 2, 4], [AZUL, VERDE, ROJO]):
            numeros[k].set_color(color)
        derecha = VGroup(simbolica, numeros).arrange(DOWN, buff=0.8)
        VGroup(triangulo, derecha).arrange(RIGHT, buff=1.8)
        self.play(Create(triangulo))
        self.play(Write(simbolica))
        self.play(TransformFromCopy(simbolica, numeros))
        self.wait()
