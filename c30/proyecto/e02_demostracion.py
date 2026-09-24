from manim import *

from componentes import CIAN, CuadradoImpares, LeccionScene


class Demostracion(LeccionScene):
    titulo = "Una prueba sin palabras"

    def construct(self):
        n = 5
        cuadro = CuadradoImpares(n).shift(2.5 * LEFT + 0.3 * DOWN)
        terminos = []
        for k in range(1, n + 1):
            self.next_section(f"capa-{k}")   # un vídeo por capa
            self.play(LaggedStart(*[FadeIn(c, scale=0.5)
                                    for c in cuadro.capa(k)],
                                  lag_ratio=0.1), run_time=0.8)
            terminos.append(str(2 * k - 1))
        self.next_section("cierre")
        suma = MathTex("+".join(terminos), "=", f"{n}^2")
        suma.next_to(cuadro, RIGHT, buff=1)
        suma[2].set_color(CIAN)
        self.play(Write(suma))
        self.play(Circumscribe(cuadro, color=CIAN))
