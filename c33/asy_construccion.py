from manim import *
from asy_puente import importar_asy


class ConstruccionAsy(Scene):
    """Un dibujo de Asymptote, animado pieza a pieza en Manim."""

    def construct(self):
        figura = importar_asy("asy_construccion.asy", height=6)
        figura.shift(LEFT * 2.3)
        # Los índices siguen el orden de dibujo del archivo .asy
        circulo, punto_a, letra_a = figura[0], figura[1], figura[2]
        secantes = VGroup(*figura[3:11:2])   # 3, 5, 7, 9
        puntos_b = VGroup(*figura[4:12:2])   # 4, 6, 8, 10
        tangente = figura[11]
        # Las etiquetas llegan negras: su color no sobrevive al SVG
        letra_a.set_fill(WHITE)

        titulo = Text("De la secante a la tangente", font_size=34)
        titulo.to_edge(UP)
        rotulo = MathTex(r"B \rightarrow A", font_size=52)
        rotulo.shift(RIGHT * 3.6)

        self.play(Write(titulo), Create(circulo), run_time=1.5)
        self.play(FadeIn(punto_a, letra_a))
        for secante, b in zip(secantes, puntos_b):
            self.play(Create(secante), FadeIn(b), run_time=0.6)
        self.play(Write(rotulo))
        self.play(
            secantes.animate.set_stroke(opacity=0.3),
            Create(tangente),
            run_time=1.2,
        )
        self.play(Indicate(tangente, color=tangente.get_color()))
        self.wait()
