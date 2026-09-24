from manim import *


class FotogramasSuaves(Scene):
    def construct(self):
        cuadrado = Square(side_length=2, color=BLUE)
        circulo = Circle(radius=1, color=RED, fill_opacity=0.5)
        cuadrado.align_points(circulo)
        fotos = VGroup()
        for t in [0, 0.25, 0.5, 0.75, 1]:
            alfa = smooth(t)  # el ritmo por defecto de Manim
            forma = cuadrado.copy()
            forma.interpolate(cuadrado, circulo, alfa)
            etiqueta = VGroup(
                MathTex(rf"t = {t}", font_size=32),
                MathTex(rf"\alpha = {alfa:.2f}", font_size=32),
            ).arrange(DOWN, buff=0.15)
            etiqueta.next_to(forma, DOWN, buff=0.35)
            fotos.add(VGroup(forma, etiqueta))
        fotos.arrange(RIGHT, buff=0.45).scale(0.95)
        self.add(fotos)
