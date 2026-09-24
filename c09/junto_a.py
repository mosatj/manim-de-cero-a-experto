from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class JuntoA(Scene):
    def construct(self):
        base = Square(2.4, color=BLUE, fill_opacity=0.3)
        self.add(base, Text("base", font_size=30))
        # Una etiqueta a cada lado, separada buff unidades
        for lado, nombre in [(UP, "UP"), (DOWN, "DOWN"),
                             (LEFT, "LEFT"), (RIGHT, "RIGHT")]:
            e = Text(nombre, font_size=32, color=YELLOW)
            e.next_to(base, lado)       # buff = 0.25 por defecto
            self.add(e)
        # En diagonal, con un buff mayor y con buff nulo
        lejos = Dot(color=RED).next_to(base, UR, buff=1)
        cerca = Dot(color=GREEN).next_to(base, DL, buff=0)
        self.add(lejos, cerca)
        self.add(Text("UR, buff=1", font_size=26, color=RED)
                 .next_to(lejos, RIGHT))
        self.add(Text("DL, buff=0", font_size=26, color=GREEN)
                 .next_to(cerca, LEFT))
