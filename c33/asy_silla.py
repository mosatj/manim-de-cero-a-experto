from manim import *
from asy_puente import importar_asy, importar_asy_png


class SillaAsy(Scene):
    """Lámina sombreada (PNG) y curvas vectoriales (SVG) encima:
    misma vista y misma caja en los dos archivos."""

    def construct(self):
        lamina = importar_asy_png("asy_silla.asy", dpi=300,
                                  height=6.4)
        lamina.to_edge(LEFT, buff=0.4)
        curvas = importar_asy("asy_silla_curvas.asy", height=6.4)
        curvas.move_to(lamina)          # misma caja: encajan solas
        borde, rectas, circulo = curvas[0:4], curvas[4:6], curvas[6]

        self.play(FadeIn(lamina), Create(borde), run_time=1.5)
        formula = MathTex(r"z=\tfrac12\,(x^2-y^2)", font_size=48)
        formula.to_corner(UR, buff=0.6)
        self.play(Write(formula))
        texto = Text("Rectas y = ±x en z = 0", font_size=32,
                     color="#B04A5A")
        texto.next_to(formula, DOWN, buff=0.6)
        texto.align_to(formula, RIGHT)
        self.play(Create(rectas), FadeIn(texto), run_time=1.5)
        punto = Dot(circulo.get_start(), radius=0.11,
                    color="#E0B04A")
        self.play(Create(circulo), MoveAlongPath(punto, circulo),
                  run_time=3)
        self.wait()
