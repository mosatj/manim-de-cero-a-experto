from manim import *

PASOS = [("2x+3", "11"), ("2x", "8"), ("x", "4")]


def ecuacion(izquierda, derecha):
    return MathTex(izquierda, "=", derecha, font_size=64)


class TransitoriaAntes(Scene):
    def construct(self):
        # Cada paso borra al anterior: hay que recordarlo todo
        actual = ecuacion(*PASOS[0])
        self.play(Write(actual))
        for paso in PASOS[1:]:
            nuevo = ecuacion(*paso)
            self.play(ReplacementTransform(actual, nuevo))
            actual = nuevo


class TransitoriaDespues(Scene):
    def construct(self):
        # Los pasos quedan a la vista: la pantalla es memoria externa
        filas = VGroup(*[ecuacion(*p) for p in PASOS])
        filas.arrange(DOWN, buff=0.5)
        for fila in filas[1:]:  # alinear todos los signos «=»
            fila.shift((filas[0][1].get_x() - fila[1].get_x()) * RIGHT)
        notas = VGroup(*[Text(t, font_size=30, color=GREY_A)
                         for t in ("restar 3", "dividir entre 2")])
        for nota, fila in zip(notas, filas[1:]):
            nota.next_to(fila, RIGHT, buff=0.8).set_x(3.2, LEFT)
        self.play(Write(filas[0]))
        for anterior, fila, nota in zip(filas, filas[1:], notas):
            self.play(TransformFromCopy(anterior, fila),
                      FadeIn(nota, shift=LEFT))
        self.play(Create(SurroundingRectangle(filas[-1], color=YELLOW)))
