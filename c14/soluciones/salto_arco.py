from manim import *


class SaltoArco(Scene):
    def construct(self):
        suelo = Line(6.5 * LEFT, 6.5 * RIGHT).shift(2 * DOWN)
        pelota = Dot(radius=0.3, color=RED)
        pelota.next_to(suelo, UP, buff=0).shift(6 * LEFT)
        self.add(suelo, pelota)
        for _ in range(3):
            # path_arc negativo: arco horario (por arriba)
            self.play(pelota.animate(path_arc=-0.8 * PI)
                      .shift(4 * RIGHT), run_time=0.9)
