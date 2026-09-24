from manim import *


class SubirYAparecer(Animation):
    """Cada pieza sube un poco y se vuelve opaca, una tras otra."""

    def __init__(self, mob, altura=0.4, lag_ratio=0.08, **kwargs):
        super().__init__(mob, lag_ratio=lag_ratio,
                         introducer=True, **kwargs)
        self.altura = altura

    def interpolate_submobject(self, sub, ini, alpha):
        # alpha ya viene con la rate_func y el retraso de esta pieza
        bajada = (1 - alpha) * self.altura * DOWN
        sub.points = ini.points + bajada
        sub.set_fill(opacity=alpha * ini.get_fill_opacity())
        sub.set_stroke(opacity=alpha * ini.get_stroke_opacity())


class EscenaSubir(Scene):
    def construct(self):
        titulo = Text("Series de Fourier", font_size=64)
        subtitulo = Text("toda onda es una suma de senos",
                         font_size=34, color=GRAY_A)
        formula = MathTex(r"f(t)=\sum_{n=1}^{\infty} b_n \sin(n t)",
                          font_size=60, color=YELLOW)
        VGroup(titulo, subtitulo, formula).arrange(DOWN, buff=0.6)
        self.play(SubirYAparecer(titulo))
        self.play(SubirYAparecer(subtitulo, lag_ratio=0.03))
        self.play(SubirYAparecer(formula, altura=0.8), run_time=1.5)
        self.wait()
