from manim import *

from componentes import CuadradoImpares, LeccionScene, Tarjeta


class Conclusion(LeccionScene):
    titulo = "Conclusión"

    def construct(self):
        cuadro = CuadradoImpares(4, lado=0.4).shift(3.5 * LEFT)
        teorema = Tarjeta("Para todo n ≥ 1",
                          r"\sum_{k=1}^{n}(2k-1)=n^2")
        teorema.shift(1.5 * RIGHT)
        self.add(cuadro)
        self.play(FadeIn(teorema, scale=0.9))
        self.play(teorema.resaltar())
