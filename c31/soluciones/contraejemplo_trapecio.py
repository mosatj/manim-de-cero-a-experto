from manim import *


class ContraejemploTrapecio(Scene):
    """Diagonales iguales no bastan: el trapecio isósceles."""

    def construct(self):
        a, b, c, d = (
            LEFT * 3 + DOWN * 1.5,
            RIGHT * 3 + DOWN * 1.5,
            RIGHT * 1.5 + UP * 1.5,
            LEFT * 1.5 + UP * 1.5,
        )
        trapecio = Polygon(a, b, c, d, color=BLUE, fill_opacity=0.3)
        diagonales = VGroup(
            Line(a, c, color=YELLOW), Line(b, d, color=YELLOW)
        )
        self.play(Create(trapecio))
        self.play(Create(diagonales))
        medidas = VGroup()
        for k, diag in enumerate(diagonales):
            rotulo = MathTex(
                f"{diag.get_length():.2f}",
                color=YELLOW,
                font_size=40,
            )
            punto = diag.point_from_proportion(0.3)
            medidas.add(
                rotulo.next_to(punto, UP if k == 0 else DOWN)
            )
        conclusion = Text(
            "Diagonales iguales, pero no es un rectángulo",
            font_size=30,
        ).to_edge(UP)
        self.play(Write(medidas), Write(conclusion))
