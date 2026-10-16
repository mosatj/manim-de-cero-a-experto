from manim import *


class CuatroFuentes(Scene):
    """La misma fórmula con la fuente por defecto (Computer Modern)
    y tres plantillas de TexFontTemplates."""

    def construct(self):
        formula = r"\int_0^\infty e^{-x^2}\,dx=\frac{\sqrt{\pi}}{2}"
        plantillas = [
            ("Computer Modern", None),
            ("Palatino", TexFontTemplates.palatino),
            ("Libertine", TexFontTemplates.libertine),
            ("Fourier Utopia", TexFontTemplates.fourier_utopia),
        ]
        filas = VGroup()
        for nombre, plantilla in plantillas:
            opciones = {} if plantilla is None else {
                "tex_template": plantilla}
            rotulo = Text(nombre, font_size=24, color="#6FA3C0")
            fila = VGroup(rotulo, MathTex(formula, **opciones))
            fila.arrange(RIGHT, buff=0.8, aligned_edge=DOWN)
            filas.add(fila)
        filas.arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        for fila in filas:
            fila[1].align_to(filas[0][1], LEFT)
        self.play(LaggedStart(*[FadeIn(f) for f in filas],
                              lag_ratio=0.4, run_time=3))
