from manim import *


class TipografiaAntes(Scene):
    def construct(self):
        bloque = Paragraph(
            "LOS CEROS DE UNA FUNCIÓN F SON LOS VALORES DE X EN",
            "LOS QUE SU GRÁFICA CORTA AL EJE HORIZONTAL. POR",
            "EJEMPLO, SI F(X) = X^2 - 4X + 3, LOS CEROS SON",
            "X = 1 Y X = 3.", font_size=32, line_spacing=0.6,
            alignment="center")
        self.add(bloque)


class TipografiaDespues(Scene):
    def construct(self):
        tema = Text("Ceros de una función", font_size=40,
                    color=GRAY_B)
        formula = MathTex(r"f(x)=x^2-4x+3", font_size=64)
        idea = Tex(r"Valores de $x$ donde\\la gráfica corta\\"
                   r"el eje horizontal", font_size=44,
                   tex_environment="flushleft")
        ceros = MathTex(r"x=1,\quad x=3", font_size=56, color=RED)
        texto = VGroup(tema, formula, idea, ceros)
        texto.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        texto.to_edge(LEFT, buff=0.9)

        ejes = Axes(x_range=[0, 4.5, 1], y_range=[-1.5, 3.5, 1],
                    x_length=5, y_length=4.5, tips=False)
        ejes.to_edge(RIGHT, buff=0.7)
        curva = ejes.plot(lambda x: x**2 - 4 * x + 3,
                          x_range=[0.2, 3.8], color=BLUE)
        puntos = VGroup(*[Dot(ejes.c2p(x, 0), radius=0.12, color=RED)
                          for x in (1, 3)])
        self.add(texto, ejes, curva, puntos)
