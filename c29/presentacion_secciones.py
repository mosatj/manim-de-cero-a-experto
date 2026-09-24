from manim import *


class PresentacionSecciones(Scene):
    def construct(self):
        self.next_section("01-titulo")
        titulo = Text("Teorema de Pitágoras", font_size=48)
        titulo.to_edge(UP)
        self.play(Write(titulo))

        self.next_section("02-triangulo")
        tri = Polygon([-2, -1.5, 0], [2, -1.5, 0], [-2, 1.5, 0],
                      color=BLUE)
        self.play(Create(tri))

        self.next_section("03-formula")
        formula = MathTex(r"a^2+b^2=c^2", font_size=60)
        self.play(Write(formula.next_to(tri, RIGHT, buff=0.8)))

        # Una sección de apoyo que no queremos renderizar ahora
        self.next_section("04-borrador", skip_animations=True)
        self.play(Indicate(formula))
