from manim import *


class AplicarCompleja(Scene):
    def construct(self):
        plano = NumberPlane(x_range=[-2, 2, 0.5],
                            y_range=[-2, 2, 0.5],
                            x_length=4, y_length=4)
        # Más puntos por línea: se curvarán sin quebrarse
        plano.prepare_for_nonlinear_transform()
        circulo = Circle(radius=1, color=YELLOW)
        grupo = VGroup(plano, circulo).shift(3.5 * LEFT)
        copia = grupo.copy().shift(7 * RIGHT)
        self.add(grupo, copia)

        # z -> z^2 alrededor del centro de la copia
        centro = complex(*copia.get_center()[:2])
        self.play(ApplyComplexFunction(
            lambda z: (z - centro) ** 2 + centro, copia),
            run_time=3)
