from manim import *


class CopiaTermino(Scene):
    def construct(self):
        suma = MathTex("a", "+", "b", font_size=96).shift(UP)
        conmutada = MathTex("b", "+", "a", font_size=96)
        conmutada.shift(1.5 * DOWN)
        self.add(suma)
        # Las copias viajan; el original de arriba no se toca
        self.play(
            TransformFromCopy(suma[0], conmutada[2],
                              path_arc=PI / 2),
            TransformFromCopy(suma[2], conmutada[0],
                              path_arc=PI / 2),
            TransformFromCopy(suma[1], conmutada[1]),
            run_time=2,
        )
        self.wait()
