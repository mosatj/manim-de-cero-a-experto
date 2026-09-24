from manim import *


def pausa_en_medio(t):
    """Va a la mitad, se detiene y termina el recorrido."""
    if t < 0.4:
        return 0.5 * smooth(t / 0.4)
    if t < 0.6:
        return 0.5
    return 0.5 + 0.5 * smooth((t - 0.6) / 0.4)


class PausaEnMedio(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 1, 0.2], y_range=[0, 1, 0.5],
                    x_length=6, y_length=4, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24}).to_edge(LEFT)
        curva = ejes.plot(pausa_en_medio, x_range=[0, 1, 0.005],
                          color=YELLOW)
        punto = Dot(color=BLUE).move_to(RIGHT * 1.5 + DOWN * 2)
        self.add(ejes, curva, punto)
        self.play(punto.animate(rate_func=pausa_en_medio)
                  .shift(UP * 4), run_time=3)
        self.wait()
