from manim import *


class PlantillaTex(Scene):
    def construct(self):
        # Una plantilla propia: la de siempre más tres paquetes
        mia = TexTemplate()
        mia.add_to_preamble(r"\usepackage{mathrsfs}")   # \mathscr
        mia.add_to_preamble(r"\usepackage{cancel}")     # \cancel
        mia.add_to_preamble(r"\newcommand{\R}{\mathbb{R}}")
        letra = MathTex(r"\mathscr{L}\{f\}(s)", tex_template=mia)
        tachado = MathTex(r"\frac{\cancel{3}\,x}{\cancel{3}} = x",
                          tex_template=mia)
        macro = MathTex(r"f:\R\to\R", tex_template=mia)
        # Plantillas de fuentes ya preparadas por Manim
        palatino = MathTex(r"\int_0^\pi \sin t\,dt = 2",
                           tex_template=TexFontTemplates.palatino)
        grupo = VGroup(letra, tachado, macro, palatino)
        grupo.arrange_in_grid(rows=2, cols=2, buff=(1.5, 1))
        self.add(grupo.scale(1.3))
