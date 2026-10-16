from manim import *

# Un preámbulo nuevo (no añadido): el de serie ya carga babel
# en inglés y un segundo babel en español daría «Option clash».
plantilla = TexTemplate(preamble=(
    r"\usepackage[spanish,es-noshorthands]{babel}"
    r"\usepackage{amsmath,amssymb,amsthm}"
    r"\newtheorem{teorema}{Teorema}\newtheorem*{dem}{Demostración}"
))


class TeoremaEnPantalla(Scene):
    def construct(self):
        enunciado = Tex(
            r"\parbox{10cm}{\begin{teorema}[Valor medio]"
            r"Si $f$ es continua en $[a,b]$ y derivable en $(a,b)$,"
            r" existe $c\in(a,b)$ con"
            r" $f'(c)=\dfrac{f(b)-f(a)}{b-a}$."
            r"\end{teorema}}", tex_template=plantilla)
        idea = Tex(
            r"\parbox{10cm}{\begin{dem}Aplica el teorema de Rolle"
            r" a $g(x)=f(x)-\dfrac{f(b)-f(a)}{b-a}(x-a)$."
            r"\end{dem}}",
            tex_template=plantilla, color="#6FA3C0")
        grupo = VGroup(enunciado, idea).arrange(DOWN, buff=0.8)
        self.play(Write(enunciado, run_time=3))
        self.play(FadeIn(idea, shift=0.3 * UP))
        self.wait()
