from manim import *

from componentes import CIAN, LeccionScene, Tarjeta


class Pregunta(LeccionScene):
    titulo = "La suma de los impares"

    def construct(self):
        sumas = VGroup()
        for n in range(1, 5):
            impares = "+".join(str(2*k-1) for k in range(1, n + 1))
            sumas.add(MathTex(impares, "=", str(n * n)))
        sumas.arrange(DOWN, aligned_edge=RIGHT).shift(2.5 * LEFT)
        for suma in sumas:
            suma[2].set_color(CIAN)
            self.play(Write(suma), run_time=0.8)
        pregunta = Tarjeta("¿Y en general?",
                           r"1+3+\cdots+(2n-1)=\,?")
        pregunta.next_to(sumas, RIGHT, buff=1)
        self.play(FadeIn(pregunta, shift=LEFT))
        self.play(pregunta.resaltar())
