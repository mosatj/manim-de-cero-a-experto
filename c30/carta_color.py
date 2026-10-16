from manim import *

# Colores de la paleta del curso (hexadecimal sRGB)
PALETA = ["#8E2130", "#4F7C99", "#6FA3C0", "#E9F2F7"]


class CartaColor(Scene):
    """Carta de ajuste: cuatro muestras planas de color."""

    def construct(self):
        for i, hexa in enumerate(PALETA):
            x = -5.1 + 3.4 * i
            muestra = Square(2.8, fill_color=hexa, fill_opacity=1,
                             stroke_width=0).move_to([x, 0.6, 0])
            codigo = Text(hexa, font_size=32).next_to(muestra, DOWN)
            self.add(muestra, codigo)
        self.wait(0.1)  # un fotograma basta para medir
