from manim import *


def collatz(n):
    """Sucesión de Collatz desde n hasta llegar a 1."""
    valores = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        valores.append(n)
    return valores


class PuntoCollatz(LabeledDot):
    """Un punto que conoce su número y el color de su paridad."""

    def __init__(self, n, **kwargs):
        rotulo = MathTex(str(n), color=BLACK, font_size=26)
        super().__init__(rotulo, radius=0.27, **kwargs)
        self.n = n
        self.color_paridad = BLUE_C if n % 2 == 0 else RED_C


class Collatz(Scene):
    def construct(self):
        valores = collatz(12)     # 12, 6, 3, 10, 5, 16, 8, 4, 2, 1
        ejes = Axes(x_range=[0, len(valores), 1],
                    y_range=[0, 18, 2], x_length=11.5, y_length=6.2,
                    tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24})
        ejes.to_edge(DOWN, buff=0.4)
        puntos = [PuntoCollatz(v).move_to(ejes.c2p(i + 1, v))
                  for i, v in enumerate(valores)]
        self.add(ejes)
        self.play(GrowFromCenter(puntos[0]))
        for previo, siguiente in zip(puntos, puntos[1:]):
            par = previo.n % 2 == 0
            regla = r"\div 2" if par else r"\times 3 + 1"
            color = previo.color_paridad
            flecha = Arrow(previo.get_center(),
                           siguiente.get_center(), buff=0.3,
                           color=color, stroke_width=4)
            texto = MathTex(regla, font_size=28, color=color)
            texto.next_to(flecha.get_center(), UR, buff=0.05)
            # family=False: se colorea el disco, no el número
            self.play(previo.animate.set_color(color, family=False),
                      GrowArrow(flecha), FadeIn(texto),
                      GrowFromCenter(siguiente), run_time=0.8)
        final = puntos[-1].animate.set_color(YELLOW, family=False)
        self.play(final)
        self.wait()
