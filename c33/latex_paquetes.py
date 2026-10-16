from manim import *

fisica = TexTemplate()
fisica.add_to_preamble(
    r"\usepackage{siunitx}\usepackage{physics}"
    r"\usepackage{amsthm}\newtheorem{teorema}{Teorema}"
)


class PaquetesEnPantalla(Scene):
    def construct(self):
        # siunitx: números y unidades con el espaciado correcto
        g = MathTex(r"g = \SI{9.81}{\metre\per\second\squared},"
                    r"\quad N_A = \num{6.022e23}",
                    tex_template=fisica)
        # physics: derivadas con \dv y \pdv
        ley = MathTex(r"F = m\,\dv[2]{x}{t} \qquad "
                      r"\pdv{u}{t} = \alpha\,\pdv[2]{u}{x}",
                      tex_template=fisica)
        # align*: varias líneas alineadas en el signo =
        pasos = MathTex(r"(a+b)^2 &= (a+b)(a+b) \\"
                        r"&= a^2 + 2ab + b^2",
                        tex_environment="align*")
        # Texto largo: un párrafo de 9 cm dentro de \parbox
        teorema = Tex(r"\parbox{9cm}{\begin{teorema}[Pitágoras]"
                      r"En todo triángulo rectángulo, el cuadrado"
                      r" de la hipotenusa es la suma de los"
                      r" cuadrados de los catetos: $a^2+b^2=c^2$."
                      r"\end{teorema}}", tex_template=fisica)
        grupo = VGroup(g, ley, pasos, teorema)
        grupo.arrange(DOWN, buff=0.5)
        for parte in grupo:
            self.play(FadeIn(parte, shift=0.3 * UP), run_time=0.8)
        self.wait(0.5)
