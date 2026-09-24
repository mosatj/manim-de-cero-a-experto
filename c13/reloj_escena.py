from manim import *


class RelojEscena(Scene):
    def construct(self):
        punto = Dot(radius=0.2, color=YELLOW)
        punto.move_to(5 * LEFT + 1.5 * DOWN)
        self.add(punto)

        def anotar(fila, texto):
            # self.time: segundos transcurridos desde el inicio
            nota = Text(f"{texto}   →   t = {self.time:.1f} s",
                        font_size=44)
            nota.move_to([0, 3.2 - 1.05 * fila, 0])
            self.add(nota)

        self.play(punto.animate.shift(2.5 * RIGHT), run_time=0.5)
        anotar(0, "play(..., run_time=0.5)")
        self.play(punto.animate.shift(2.5 * RIGHT), run_time=2)
        anotar(1, "play(..., run_time=2)")
        self.wait(1.5)
        anotar(2, "wait(1.5)")
        self.play(punto.animate.shift(2.5 * RIGHT))
        anotar(3, "play(...)   sin run_time: 1 s")
