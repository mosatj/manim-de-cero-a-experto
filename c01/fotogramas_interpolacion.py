from manim import *


class FotogramasInterpolacion(Scene):
    def construct(self):
        # Cinco "fotos" de Transform(cuadrado, circulo) en distintos instantes
        cuadrado = Square(side_length=2, color=BLUE)
        circulo = Circle(radius=1, color=RED, fill_opacity=0.5)
        cuadrado.align_points(circulo)  # mismo número de puntos en ambas
        fotos = VGroup()
        for alfa in [0, 0.25, 0.5, 0.75, 1]:
            forma = cuadrado.copy()
            forma.interpolate(cuadrado, circulo, alfa)  # mezcla al alfa %
            etiqueta = MathTex(rf"\alpha = {alfa}", font_size=34)
            etiqueta.next_to(forma, DOWN, buff=0.35)
            fotos.add(VGroup(forma, etiqueta))
        fotos.arrange(RIGHT, buff=0.45).scale(0.95)
        flecha = Arrow(fotos.get_left(), fotos.get_right(), buff=0)
        flecha.next_to(fotos, DOWN, buff=0.5)
        tiempo = Text("tiempo", font_size=28).next_to(flecha, DOWN)
        self.add(fotos, flecha, tiempo)
