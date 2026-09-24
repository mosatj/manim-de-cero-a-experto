from manim import *


def pasos_collatz(n):
    """Número de pasos hasta llegar a 1 (tiempo de vuelo)."""
    pasos = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        pasos += 1
    return pasos


class TiemposCollatz(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 60, 10], y_range=[0, 120, 20],
                    x_length=11, y_length=6, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24})
        puntos = VGroup(*[
            Dot(ejes.c2p(n, pasos_collatz(n)), radius=0.06,
                color=RED_C if n == 27 else TEAL_B)
            for n in range(1, 61)])
        nota = MathTex(r"n=27:\ 111\text{ pasos}", color=RED_C,
                       font_size=36).next_to(puntos[26], UP)
        self.add(ejes)
        self.play(LaggedStart(*[GrowFromCenter(p) for p in puntos],
                              lag_ratio=0.05), run_time=3)
        self.play(Write(nota))
        self.wait()
