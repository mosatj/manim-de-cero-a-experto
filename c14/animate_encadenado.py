from manim import *


class AnimateEncadenado(Scene):
    def construct(self):
        cuadrado = Square(side_length=1.5, color=BLUE,
                          fill_opacity=0.6)
        cuadrado.shift(4 * LEFT)
        self.add(cuadrado)
        # Tres métodos encadenados: una sola animación
        self.play(cuadrado.animate.shift(2 * UP).scale(0.5)
                  .set_color(YELLOW))
        # Argumentos de la animación: antes del primer método
        self.play(cuadrado.animate(run_time=2, path_arc=-PI)
                  .shift(8 * RIGHT))
        self.play(cuadrado.animate(rate_func=there_and_back)
                  .scale(3), run_time=1.5)
