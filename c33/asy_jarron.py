from manim import *
from asy_puente import importar_asy


class JarronAsy(Scene):
    """Alambre de Asymptote: cada curva es un camino animable."""

    def construct(self):
        alambre = importar_asy("asy_jarron.asy", height=5.6)
        alambre.shift(LEFT * 1.4 + DOWN * 0.3)
        ejes = VGroup(*alambre[0:3])
        generatrices = VGroup(*alambre[3:15])
        circulos = VGroup(*alambre[15:24])
        letra_x = alambre[24].set_fill(WHITE)
        formula = MathTex(r"V=\pi\int_0^4 f(x)^2\,dx",
                          font_size=40)
        formula.to_corner(UR, buff=0.6)

        self.play(Create(ejes), FadeIn(letra_x))
        self.play(Create(generatrices[0]), run_time=1)
        resto = [Create(g) for g in generatrices[1:]]
        self.play(LaggedStart(*resto, lag_ratio=0.1), run_time=2)
        aros = [Create(c) for c in circulos]
        self.play(LaggedStart(*aros, lag_ratio=0.1), run_time=2)
        # Un punto recorre la generatriz dibujada por Asymptote
        punto = Dot(color="#B04A5A", radius=0.1)
        punto.move_to(generatrices[0].get_start())
        self.add(punto)
        self.play(MoveAlongPath(punto, generatrices[0]),
                  Write(formula), run_time=3)
        self.wait()
