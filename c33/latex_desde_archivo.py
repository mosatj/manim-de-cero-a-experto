from manim import *

# La plantilla vive en un archivo .tex normal, junto al script;
# así la comparte el proyecto entero (y tus apuntes en LaTeX).
mia = TexTemplate.from_file("latex_plantilla.tex")
config.tex_template = mia     # para todas las fórmulas


class PlantillaDeArchivo(Scene):
    def construct(self):
        f = MathTex(r"f:\R\to\R,\qquad f(x)=\destacar{x^2}")
        integral = MathTex(r"\int_0^1 \destacar{x^2}\dd x=\tfrac13")
        grupo = VGroup(f, integral).arrange(DOWN, buff=0.8)
        self.play(Write(f))
        self.play(TransformFromCopy(f[0][-3:], integral[0][4:7]),
                  FadeIn(integral), run_time=1.5)
        self.wait(0.5)
