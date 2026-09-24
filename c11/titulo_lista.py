from manim import *


class TituloLista(Scene):
    def construct(self):
        # Title se coloca solo arriba y trae su línea horizontal
        titulo = Title(r"Tres motores de texto")
        lista = BulletedList(
            r"\texttt{Text}: Pango, sin \LaTeX",
            r"\texttt{Tex}: texto compuesto con \LaTeX",
            r"\texttt{MathTex}: fórmulas en modo matemático",
            font_size=40,
        )
        lista.next_to(titulo, DOWN, buff=0.8)
        self.play(Write(titulo))
        self.play(FadeIn(lista, shift=UP))
        # Atenúa todo menos el elemento 1 (se cuenta desde 0)
        self.play(lista.animate.fade_all_but(1))
        self.wait()
