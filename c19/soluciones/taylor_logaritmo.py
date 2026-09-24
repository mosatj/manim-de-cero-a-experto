from manim import *


def taylor_log(n):
    """Suma parcial de ln(1 + x) = x − x²/2 + x³/3 − ..."""
    return lambda x: sum((-1)**(k + 1) * x**k / k
                         for k in range(1, n + 1))


def hasta_donde(p, tope=1.8):
    """Mayor X <= 1.6 con |p(x)| <= tope en [0, X]."""
    for x in np.linspace(0, 1.6, 801):
        if abs(p(x)) > tope:
            return x
    return 1.6


class TaylorLogaritmo(Scene):
    def construct(self):
        ejes = Axes(x_range=[-1, 2, 0.5], y_range=[-3, 2, 1],
                    x_length=10, y_length=5.8, tips=False)
        ejes.add_coordinates(font_size=22).to_edge(DOWN, buff=0.3)
        log = ejes.plot(lambda x: np.log(1 + x), x_range=[-0.95, 2],
                        color=BLUE)
        # Borde del disco de convergencia: |x| = 1
        borde = DashedLine(ejes.c2p(1, -3), ejes.c2p(1, 2),
                           color=RED)
        colores = color_gradient([YELLOW, ORANGE], 4)
        sumas = VGroup(*[
            ejes.plot(taylor_log(n), color=c, stroke_width=2,
                      x_range=[-0.95, hasta_donde(taylor_log(n))])
            for n, c in zip([2, 5, 10, 20], colores)])
        texto = MathTex(
            r"\ln(1+x)=\sum_{k\ge1}\frac{(-1)^{k+1}x^k}{k}",
            r"\quad(-1<x\le 1)", font_size=36).to_edge(UP)
        self.add(ejes, borde, sumas, log, texto)
