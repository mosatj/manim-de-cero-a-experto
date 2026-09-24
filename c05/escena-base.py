from manim import *


class EscenaLibroBase(Scene):
    """Escena base del proyecto: título y filete comunes."""
    titulo = "Sin título"                # las hijas lo cambian

    def setup(self):                     # Manim lo llama antes de
        rotulo = Text(self.titulo, font_size=40)   # construct()
        rotulo.to_edge(UP, buff=0.5)
        filete = Line(6 * LEFT, 6 * RIGHT, color=BLUE)
        filete.next_to(rotulo, DOWN, buff=0.25)
        self.add(rotulo, filete)


class Pitagoras(EscenaLibroBase):
    titulo = "Teorema de Pitágoras"

    def construct(self):
        formula = MathTex(r"a^2 + b^2 = c^2", font_size=80)
        self.play(Write(formula))

