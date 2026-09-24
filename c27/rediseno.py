from manim import *

B, PEQ, H = 5.0, 2.6, 2.4  # base mayor, base menor y altura


def trapecio():
    return Polygon([-B / 2, 0, 0], [B / 2, 0, 0], [PEQ / 2, H, 0],
                   [-PEQ / 2, H, 0])


class RedisenoAntes(Scene):
    def construct(self):
        titulo = Text("ÁREA DEL TRAPECIO", font_size=44, weight=BOLD)
        titulo.set_color_by_gradient(PINK, YELLOW).to_edge(UP)
        subrayado = Underline(titulo, color=GREEN)
        t = trapecio().set_color(PURPLE).shift(3.2 * LEFT + 1.6 * DOWN)
        numeros = VGroup(Text("1").next_to(t, DOWN),
                         Text("2").next_to(t, UP),
                         Text("3").move_to(t.get_center()))
        texto = Paragraph("El área del trapecio es igual a",
                          "la semisuma de las bases (1 y 2)",
                          "multiplicada por la altura (3).",
                          font_size=24).shift(3 * RIGHT + UP)
        formula = MathTex(r"A=\frac{(B+b)\,h}{2}", color=GREEN)
        formula.next_to(texto, DOWN, buff=0.6)
        self.add(titulo, subrayado, t, numeros, texto)
        self.play(Write(formula), *[Indicate(n) for n in numeros])


class RedisenoDespues(Scene):
    def construct(self):
        t = trapecio().set_stroke(GREY_B).shift(3.2 * LEFT + 1.6 * DOWN)
        vertices = t.get_vertices()
        base_mayor = Line(vertices[0], vertices[1], color=BLUE)
        base_menor = Line(vertices[3], vertices[2], color=TEAL)
        pie = np.array([vertices[3][0], vertices[0][1], 0])
        altura = DashedLine(vertices[3], pie, color=YELLOW)
        rotulos = VGroup(
            MathTex("B", color=BLUE).next_to(base_mayor, DOWN),
            MathTex("b", color=TEAL).next_to(base_menor, UP),
            MathTex("h", color=YELLOW).next_to(altura, LEFT, buff=0.15),
        )
        formula = MathTex(r"A=", r"{(B", "+", "b)", r"\,h", r"\over 2}",
                          font_size=80).shift(3.2 * RIGHT)
        for indice, color in ((1, BLUE), (3, TEAL), (4, YELLOW)):
            formula[indice].set_color(color)
        self.add(t)
        self.play(Create(VGroup(base_mayor, base_menor, altura)),
                  Write(rotulos))
        self.play(Write(formula))
