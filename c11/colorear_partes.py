from manim import *


def rotulo(texto):
    return Text(texto, font_size=22, color=GRAY_B)


class ColorearPartes(Scene):
    def construct(self):
        # 1. Por argumentos: cada cadena es una parte (f[0]...)
        f1 = MathTex("a^2", "+", "b^2", "=", "c^2")
        f1[0].set_color(BLUE)
        f1[2].set_color(GREEN)
        f1[4].set_color(RED)
        # 2. Llaves dobles: el mismo troceo en una sola cadena
        f2 = MathTex(r"{{a^2}} + {{b^2}} = {{c^2}}")
        f2.set_color_by_tex("b^2", GREEN)
        # 3. Aislar una subcadena en todas sus apariciones
        f3 = MathTex(r"e^{x} = 1 + x + \frac{x^2}{2!} + \cdots",
                     substrings_to_isolate="x")
        f3.set_color_by_tex("x", YELLOW)
        # 4. Diccionario de colores (aísla y colorea a la vez)
        f4 = MathTex(r"F = m\,a", tex_to_color_map={
            "F": RED, "m": BLUE, "a": GREEN})
        # 5. Rebanada de glifos del primer (y único) trozo
        f5 = MathTex(r"\sqrt{x^2+y^2}")
        f5[0][2:4].set_color(ORANGE)   # los glifos de x^2
        # 6. Color escrito en el propio LaTeX (requiere xcolor)
        plantilla = TexTemplate()
        plantilla.add_to_preamble(r"\usepackage{xcolor}")
        f6 = MathTex(r"\sin^2 x + \textcolor{pink}{\cos^2 x} = 1",
                     tex_template=plantilla)
        casillas = VGroup()
        nombres = [
            "1. argumentos", "2. {{ }}", "3. substrings_to_isolate",
            "4. tex_to_color_map", "5. f[0][2:4]", "6. \\textcolor"]
        for f, n in zip([f1, f2, f3, f4, f5, f6], nombres):
            f.scale(0.9)
            casillas.add(VGroup(f, rotulo(n).next_to(f, DOWN)))
        casillas.arrange_in_grid(rows=3, cols=2, buff=(1.2, 0.7))
        self.add(casillas)
