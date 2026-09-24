from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class FilaYColumna(Scene):
    def construct(self):
        formas = [Circle, Square, Triangle, RegularPolygon, Star]
        colores = [BLUE, GREEN, YELLOW, RED, PURPLE]
        # Fila: cada uno a la derecha del anterior
        fila = VGroup(*[f(color=c).scale(0.6)
                        for f, c in zip(formas, colores)])
        fila.arrange(RIGHT, buff=0.4).to_edge(UP, buff=0.8)
        self.add(fila, Text("arrange(RIGHT, buff=0.4)",
                            font_size=28).next_to(fila, DOWN))
        # Columnas de rótulos de largo distinto
        palabras = ["círculo", "cuadrado", "triángulo"]
        rotulos = VGroup(*[Text(t, font_size=30)
                           for t in palabras])
        izq = rotulos.copy().arrange(DOWN, aligned_edge=LEFT)
        cen = rotulos.copy().arrange(DOWN)
        der = rotulos.copy().arrange(DOWN, aligned_edge=RIGHT)
        columnas = VGroup(izq, cen, der).arrange(RIGHT, buff=1.5)
        columnas.to_edge(DOWN, buff=1.3)
        self.add(columnas)
        notas = ["aligned_edge=LEFT", "(centrado)",
                 "aligned_edge=RIGHT"]
        for col, t in zip(columnas, notas):
            self.add(SurroundingRectangle(col, color=GRAY))
            self.add(Text(t, font_size=24, color=YELLOW)
                     .next_to(col, DOWN, buff=0.3))
