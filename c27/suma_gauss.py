from manim import *

N, LADO = 5, 0.6


def escalera(color):
    """Columnas de 1, 2, ..., N cuadrados: la suma 1 + 2 + ... + N."""
    columnas = VGroup(*[
        VGroup(*[Square(LADO) for _ in range(k)]).arrange(UP, buff=0)
        for k in range(1, N + 1)])
    columnas.arrange(RIGHT, buff=0, aligned_edge=DOWN)
    return columnas.set_style(fill_color=color, fill_opacity=0.8,
                              stroke_color=WHITE, stroke_width=2)


class SumaGauss(Scene):
    def construct(self):
        # 1. La pregunta, antes que cualquier fórmula
        pregunta = MathTex(r"1+2+3+\cdots+100", "=", "?", font_size=56)
        pregunta.to_edge(UP)
        self.play(Write(pregunta))
        # 2. Un caso concreto y pequeño: N = 5
        azul = escalera(BLUE).move_to([-3.6, -0.9, 0],
                                      aligned_edge=DOWN)
        self.play(LaggedStart(*[FadeIn(c, shift=UP) for c in azul],
                              lag_ratio=0.3))
        # 3. La idea: una copia girada completa un rectángulo
        naranja = escalera(ORANGE).rotate(PI)
        naranja.align_to(azul, LEFT).align_to(
            azul.get_bottom() + (N + 1) * LADO * UP, UP)
        self.play(TransformFromCopy(azul, naranja, path_arc=PI))
        bloque = VGroup(azul, naranja)
        llaves = VGroup(Brace(bloque, DOWN), Brace(bloque, LEFT))
        medidas = VGroup(llaves[0].get_tex("5"),
                         llaves[1].get_tex("6"))
        self.play(FadeIn(llaves), FadeIn(medidas))
        # 4. Lo que se ve, escrito; luego, el caso general
        caso = MathTex(r"1+2+3+4+5=\frac{5\cdot 6}{2}=15")
        general = MathTex(r"1+2+\cdots+n=\frac{n\,(n+1)}{2}")
        VGroup(caso, general).arrange(DOWN, aligned_edge=LEFT,
                                      buff=0.8).move_to([2.6, -0.3, 0])
        self.play(Write(caso))
        self.wait()
        self.play(Write(general))
        # 5. La respuesta a la pregunta del principio
        respuesta = MathTex("5050", font_size=56, color=ORANGE)
        respuesta.next_to(pregunta[1], RIGHT, buff=0.25)
        self.play(Transform(pregunta[2], respuesta))
