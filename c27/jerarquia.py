from manim import *


def contenidos(tamanos, colores):
    titulo = Text("Teorema de Pitágoras", font_size=tamanos[0],
                  color=colores[0])
    formula = MathTex(r"a^2+b^2=c^2", font_size=tamanos[1],
                      color=colores[1])
    nota = Text("solo en triángulos rectángulos",
                font_size=tamanos[2], color=colores[2])
    return titulo, formula, nota


class JerarquiaAntes(Scene):
    def construct(self):
        # Mismo tamaño y color: nada dice «empieza por aquí»
        titulo, formula, nota = contenidos([40, 40, 40], [WHITE] * 3)
        VGroup(titulo, nota, formula).arrange(DOWN, buff=0.6)
        self.play(FadeIn(titulo), FadeIn(formula), FadeIn(nota))


class JerarquiaDespues(Scene):
    def construct(self):
        # Tres niveles: fórmula que manda, título que orienta, nota
        titulo, formula, nota = contenidos([36, 110, 30],
                                           [GREY_B, WHITE, YELLOW])
        titulo.to_edge(UP, buff=0.8)
        nota.next_to(formula, DOWN, buff=0.6)
        self.play(FadeIn(titulo))
        self.play(Write(formula))
        self.play(FadeIn(nota, shift=UP * 0.3))
