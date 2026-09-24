from manim import *


class Carrera(Scene):
    def construct(self):
        ritmos = [linear, smooth, rush_into,
                  rate_functions.ease_out_elastic]
        animaciones = []
        for k, funcion in enumerate(ritmos):
            y = 2.4 - 1.6 * k
            carril = Line([-4, y, 0], [5, y, 0], color=GRAY_D)
            nombre = Text(funcion.__name__, font_size=24)
            nombre.next_to(carril, LEFT)
            punto = Dot([-4, y, 0], radius=0.15, color=YELLOW)
            self.add(carril, nombre, punto)
            # Cada punto recibe su propio ritmo
            animaciones.append(
                punto.animate(rate_func=funcion).shift(9 * RIGHT))
        self.play(*animaciones, run_time=4)
