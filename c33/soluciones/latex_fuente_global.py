from manim import *

# Una sola línea cambia la fuente de TODAS las fórmulas
config.tex_template = TexFontTemplates.libertine


class FormulasEnLibertine(Scene):
    def construct(self):
        formulas = VGroup(
            MathTex(r"e^{i\pi}+1=0"),
            MathTex(r"\sum_{n=1}^{\infty}\frac{1}{n^2}"
                    r"=\frac{\pi^2}{6}"),
            Tex(r"Teorema. Si $f$ es derivable, es continua."),
        ).arrange(DOWN, buff=0.7)
        self.play(Write(formulas, run_time=3))
