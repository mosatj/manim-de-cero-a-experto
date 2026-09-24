from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class Resaltar(Scene):
    def construct(self):
        self.add(NumberPlane())
        f1 = MathTex(r"(a+b)^2 = a^2 + 2ab + b^2", font_size=60)
        f2 = MathTex(r"(a+b)^2 = a^2 + b^2", font_size=60)
        VGroup(f1, f2).arrange(DOWN, buff=1.4).shift(0.4 * UP)
        # Un fondo que tapa la cuadrícula para que se lea el texto
        fondo1 = BackgroundRectangle(f1, buff=0.15)
        fondo2 = BackgroundRectangle(f2, buff=0.15)
        marco = SurroundingRectangle(f1[0][10:13], color=YELLOW,
                                     buff=0.08)
        raya = Underline(f1, color=GREEN)
        aspa = Cross(f2, stroke_width=8)
        self.add(fondo1, fondo2, f1, f2, marco, raya, aspa)
        rotulos = VGroup(
            Text("BackgroundRectangle", font_size=24),
            Text("SurroundingRectangle", font_size=24,
                 color=YELLOW),
            Text("Underline", font_size=24, color=GREEN),
            Text("Cross", font_size=24, color=RED),
        ).arrange(RIGHT, buff=0.5).to_edge(DOWN)
        self.add(BackgroundRectangle(rotulos), rotulos)
