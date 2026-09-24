from manim import *
from congelar import congelar


class PorPartes(Scene):
    def construct(self):
        def fila_de_puntos():
            return VGroup(*[
                Circle(radius=0.2, color=BLUE, fill_opacity=0.9)
                for _ in range(8)
            ]).arrange(RIGHT, buff=0.15)

        clases = [ShowIncreasingSubsets, ShowSubmobjectsOneByOne]
        for j, clase in enumerate(clases):
            titulo = Text(clase.__name__, font="Monospace",
                          font_size=26)
            titulo.move_to([0, 3.2 - 3.4 * j, 0])
            self.add(titulo)
            for i, alfa in enumerate([0.25, 0.5, 0.75]):
                fila = fila_de_puntos()
                fila.move_to([-4.6 + 4.6 * i, 2.2 - 3.4 * j, 0])
                # rate_func=linear: fracción visible = alfa
                congelar(self, clase(fila, rate_func=linear), alfa)
                rotulo = MathTex(rf"\alpha={alfa}", font_size=32)
                rotulo.next_to(fila, DOWN, buff=0.3)
                self.add(rotulo)
