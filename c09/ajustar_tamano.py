from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class AjustarTamano(Scene):
    def construct(self):
        crudas = VGroup(
            Circle(0.3), Square(1.9, color=GREEN),
            Star(color=YELLOW).scale(0.4),
            Rectangle(width=3, height=0.6, color=BLUE),
        ).arrange(RIGHT, buff=0.5)
        # Misma altura, proporciones intactas
        iguales = crudas.copy()
        for f in iguales:
            f.scale_to_fit_height(1.2)
        iguales.arrange(RIGHT, buff=0.5)
        # Mismo ancho y alto a la fuerza: se deforman
        estiradas = crudas.copy()
        for f in estiradas:
            f.stretch_to_fit_width(1.6)
            f.stretch_to_fit_height(1.2)
        estiradas.arrange(RIGHT, buff=0.5)
        filas = VGroup(crudas, iguales, estiradas)
        filas.arrange(DOWN, buff=0.9).shift(0.3 * DOWN)
        self.add(filas)
        rotulos = ["tamaños originales",
                   "scale_to_fit_height(1.2)",
                   "stretch_to_fit_width/height"]
        for fila, t in zip(filas, rotulos):
            self.add(Text(t, font_size=26, color=GRAY_A)
                     .next_to(fila, UP, buff=0.15))
