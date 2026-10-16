from manim import *
from asy_puente import importar_asy_png


class FiguraDeClase(Scene):
    """Una lámina sombreada de Asymptote (PNG) con anotaciones de
    Manim encima: el dibujo de siempre, sin redibujarlo."""

    def construct(self):
        lamina = importar_asy_png("asy_sombreado.asy", dpi=300,
                                  height=5.6)
        lamina.shift(LEFT * 1.3 + DOWN * 0.2)
        self.play(FadeIn(lamina, run_time=1.2))
        # Un PNG no tiene geometría: se apunta por proporciones
        ancho, alto = lamina.width, lamina.height
        esquina = lamina.get_corner(DL)
        disco = esquina + np.array([0.46 * ancho, 0.52 * alto, 0])
        flecha = Arrow(disco + UL * 1.7, disco, buff=0.05,
                       color="#E0B04A")
        formula = MathTex(r"dV=\pi\,f(x)^2\,dx", font_size=44)
        formula.next_to(flecha.get_start(), UP, buff=0.15)
        self.play(GrowArrow(flecha), Write(formula))
        total = MathTex(r"V=\pi\int_0^4 f(x)^2\,dx", font_size=40)
        total.to_corner(DR, buff=0.5)
        self.play(TransformFromCopy(formula, total))
        self.wait()
