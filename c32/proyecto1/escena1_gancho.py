from manim import *
from estilo import COLOR_A, COLOR_B, COLOR_C, TAM_TITULO
from componentes import triangulo
from narracion import GuionScene


class Gancho(GuionScene):
    def construct(self):
        formula = MathTex(
            "a^2",
            "+",
            "b^2",
            "=",
            "c^2",
            r"\;?",
            font_size=TAM_TITULO * 2,
        ).shift(UP * 1.2)
        self.decir("pregunta", Write(formula))

        a, b = 3.0, 2.0
        tri = triangulo(a, b).move_to(DOWN * 0.6)
        v = tri.get_vertices()
        lados = VGroup(
            Line(v[0], v[1], color=COLOR_A, stroke_width=7),
            Line(v[0], v[2], color=COLOR_B, stroke_width=7),
            Line(v[1], v[2], color=COLOR_C, stroke_width=7),
        )
        nombres = VGroup(
            MathTex("a", color=COLOR_A).next_to(lados[0], DOWN),
            MathTex("b", color=COLOR_B).next_to(lados[1], LEFT),
            MathTex("c", color=COLOR_C).move_to(
                lados[2].get_center() + 0.35 * (UP + RIGHT)
            ),
        )
        recto = RightAngle(lados[0], lados[1], length=0.3)
        # Los colores de la fórmula anticipan los de la figura
        self.decir(
            "triangulo",
            formula.animate.scale(0.5).to_edge(UP),
            FadeIn(tri),
            Create(lados),
            Create(recto),
            Write(nombres),
        )
        for i, color in ((0, COLOR_A), (2, COLOR_B), (4, COLOR_C)):
            formula[i].set_color(color)
