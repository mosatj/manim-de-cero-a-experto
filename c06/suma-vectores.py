from manim import *


class SumaVectores(Scene):
    def construct(self):
        estilo = {"stroke_opacity": 0.3}         # cuadrícula tenue
        plano = NumberPlane(background_line_style=estilo)
        a = np.array([3, 1, 0])
        b = np.array([1, 2, 0])
        flecha_a = Arrow(ORIGIN, a, buff=0, color=BLUE)
        flecha_b = Arrow(ORIGIN, b, buff=0, color=GREEN)
        flecha_s = Arrow(ORIGIN, a + b, buff=0, color=YELLOW)
        # Lados del paralelogramo: b desde la punta de a y viceversa
        lado1 = DashedLine(a, a + b, color=GREEN)
        lado2 = DashedLine(b, a + b, color=BLUE)
        etiquetas = VGroup(
            MathTex(r"\vec a").next_to(a, DOWN).set_color(BLUE),
            MathTex(r"\vec b").next_to(b, LEFT).set_color(GREEN),
            MathTex(r"\vec a+\vec b").next_to(a + b, UR, buff=0.1),
        )
        self.add(plano)
        self.play(GrowArrow(flecha_a), GrowArrow(flecha_b))
        self.play(Create(lado1), Create(lado2))
        self.play(GrowArrow(flecha_s), Write(etiquetas))
