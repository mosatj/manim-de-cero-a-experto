from manim import *


class ConTituloBase(Scene):
    titulo = "Sin título"  # atributo de clase

    def setup(self):
        self.cabecera = Text(self.titulo, font_size=40)
        self.cabecera.to_edge(UP)
        linea = Line(LEFT * 6, RIGHT * 6, color=BLUE)
        linea.next_to(self.cabecera, DOWN)
        self.add(self.cabecera, linea)


class Circulos(ConTituloBase):
    titulo = "Círculos"

    def construct(self):
        self.play(Create(Circle(radius=2, color=YELLOW)))
        self.wait()


class Cuadrados(ConTituloBase):
    titulo = "Cuadrados"

    def construct(self):
        self.play(Create(Square(side_length=3, color=RED)))
        self.wait()
