from manim import *


class BusquedaLineal(Scene):
    def construct(self):
        a, x = [14, 3, 9, 27, 5, 18, 11, 6], 18
        celdas = VGroup(*[VGroup(Square(0.9), MathTex(str(v)))
                          for v in a]).arrange(RIGHT, buff=0)
        for c in celdas:
            c[1].move_to(c[0])
        flecha = Arrow(DOWN, UP, color=YELLOW)
        flecha.next_to(celdas[0], DOWN)
        self.add(celdas, MathTex(rf"x = {x}").to_edge(UP), flecha)
        for k, v in enumerate(a):
            self.play(flecha.animate.next_to(celdas[k], DOWN),
                      run_time=0.4)
            # encontrado
            if v == x:
                verde = celdas[k][0].animate.set_fill(GREEN_D, 0.8)
                self.play(verde)
                break
            self.play(celdas[k].animate.set_opacity(0.3),
                      run_time=0.3)
        self.wait()
