from manim import *


class HomotopiaCompleja(Scene):
    def construct(self):
        rango = [-2, 2, 0.5]
        malla = NumberPlane(x_range=rango, y_range=rango,
                            x_length=4, y_length=4)
        malla.prepare_for_nonlinear_transform()
        fondo = malla.copy().set_stroke(opacity=0.2)

        # Deformación continua de la identidad (t=0) a z²/2 (t=1)
        def deformar(z, t):
            return (1 - t) * z + t * z ** 2 / 2

        self.add(fondo)
        self.play(ComplexHomotopy(deformar, malla, run_time=3))
