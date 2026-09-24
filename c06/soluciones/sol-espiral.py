from manim import *


class EspiralArquimedes(Scene):
    def construct(self):
        theta = np.linspace(0, 6 * PI, 600)      # tres vueltas
        r = 0.18 * theta                         # r = a θ
        x, y = r * np.cos(theta), r * np.sin(theta)
        puntos = np.column_stack([x, y, np.zeros_like(theta)])
        espiral = VMobject().set_points_smoothly(puntos)
        espiral.set_color_by_gradient(BLUE, YELLOW, RED)
        # Un punto cada 100 muestras: rebanada con paso
        muestras = puntos[::100]
        marcas = VGroup(*[Dot(p, radius=0.06) for p in muestras])
        self.play(Create(espiral), run_time=3)
        self.play(FadeIn(marcas))
