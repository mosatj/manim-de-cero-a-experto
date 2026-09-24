from manim import *


def es_primo(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


class PrimosGemelos(Scene):
    def construct(self):
        celdas = VGroup(*[
            VGroup(Square(0.9, stroke_width=1.5),
                   Text(str(n), font_size=26)) for n in range(1, 51)
        ]).arrange_in_grid(5, 10, buff=0)
        for c in celdas:
            c[1].move_to(c[0])
        self.add(celdas)
        primos = [n for n in range(1, 51) if es_primo(n)]
        gemelos = {p for p in primos
                   if es_primo(p + 2) or es_primo(p - 2)}
        self.play(*[celdas[p - 1][0].animate.set_fill(
            RED_D if p in gemelos else YELLOW_E, 0.8)
            for p in primos])
        leyenda = Tex(r"rojo: primos gemelos ($p$ y $p+2$ primos)",
                      font_size=36).next_to(celdas, DOWN)
        self.play(Write(leyenda))
        self.wait()
