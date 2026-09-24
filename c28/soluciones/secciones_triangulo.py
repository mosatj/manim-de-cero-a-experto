from manim import *

# Guion: (bloque, segundos de voz)
GUION = [("gancho", 4), ("rectangulo", 6), ("mitad", 6), ("formula", 5)]


class AreaTriangulo(Scene):
    def construct(self):
        tiempos = dict(GUION)
        self.next_section("gancho")
        pregunta = Text("¿Por qué el área del triángulo lleva un 1/2?",
                        font_size=34).to_edge(UP)
        self.play(Write(pregunta))
        self.wait(tiempos["gancho"] - 1)

        self.next_section("rectangulo")
        rect = Rectangle(width=5, height=3, color=BLUE).shift(0.5 * DOWN)
        b = MathTex("b").next_to(rect, DOWN)
        h = MathTex("h").next_to(rect, LEFT)
        self.play(Create(rect), Write(b), Write(h))
        self.wait(tiempos["rectangulo"] - 1)

        self.next_section("mitad")
        esquinas = rect.get_vertices()  # UR, UL, DL, DR
        tri = Polygon(esquinas[2], esquinas[3], esquinas[0],
                      color=YELLOW, fill_opacity=0.5)
        self.play(DrawBorderThenFill(tri))
        self.wait(tiempos["mitad"] - 1)

        self.next_section("formula")
        formula = MathTex(r"A=\frac{b\,h}{2}", font_size=64)
        formula.next_to(rect, RIGHT, buff=0.8)
        self.play(Write(formula))
        self.wait(tiempos["formula"] - 1)
