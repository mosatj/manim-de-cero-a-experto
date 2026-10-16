from manim import *

# XeLaTeX: fuentes del sistema con fontspec; la salida es .xdv
stix = TexTemplate(tex_compiler="xelatex", output_format=".xdv")
stix.add_to_preamble(
    r"\usepackage{fontspec}\setmainfont{STIX Two Text}"
    r"\usepackage{unicode-math}\setmathfont{STIX Two Math}"
)

# LuaLaTeX también sirve; aquí pide salida .dvi (no .pdf)
fira = TexTemplate(tex_compiler="lualatex", output_format=".dvi")
fira.add_to_preamble(
    r"\usepackage{fontspec}\setmainfont{Fira Sans}")


class TextoUnicode(Scene):
    def construct(self):
        frase = "Función, año y ñandú: Unicode tal cual"
        a = Tex(frase, tex_template=stix)
        b = Tex(frase, tex_template=fira, color="#E0B04A")
        c = Tex(r"$\mathbb{E}[X]=\int_{-\infty}^{\infty} x\,"
                r"f(x)\,\mathrm{d}x$", tex_template=stix)
        grupo = VGroup(a, b, c).arrange(DOWN, buff=0.7)
        self.play(Write(grupo, run_time=3))
