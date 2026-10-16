from manim import *
from asy_puente import importar_asy
from asy_utiles import Registro, flechas, por_color

AZUL, GRANATE, OCRE = "#6FA3C0", "#B04A5A", "#E0B04A"


class GradienteAsy(Scene):
    """contour y vectorfield de Asymptote; el descenso, de Manim."""

    def construct(self):
        fig = importar_asy("asy_gradiente.asy", height=6.6)
        fig.to_edge(LEFT, buff=0.4)
        a_escena = Registro(fig, (-3, -2), (3, 2))
        niveles = por_color(fig, AZUL)
        campo = flechas(por_color(fig, GRANATE))

        self.play(LaggedStart(*[Create(c) for c in niveles],
                              lag_ratio=0.3), run_time=2)
        self.play(LaggedStart(*[FadeIn(f) for f in campo],
                              lag_ratio=0.04), run_time=3)
        # Descenso más rápido desde (x0, y0): y = y0 (x/x0)^4
        x0, y0 = 2.8, 1.5
        xs = np.linspace(x0, 0.05, 60)
        camino = VMobject(color=OCRE, stroke_width=7)
        camino.set_points_smoothly(
            [a_escena(x, y0 * (x / x0) ** 4) for x in xs])
        bola = Dot(camino.get_start(), radius=0.12, color=OCRE)
        self.play(campo.animate.set_opacity(0.45), FadeIn(bola))
        self.play(Create(camino), MoveAlongPath(bola, camino),
                  run_time=3)
        texto = VGroup(
            MathTex(r"\dot{\mathbf{x}} = -\nabla f", font_size=48,
                    color=OCRE),
            Text("perpendicular a las", font_size=32),
            Text("curvas de nivel", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT)
        texto.to_edge(RIGHT, buff=0.5)
        self.play(Write(texto))
        self.wait()
