from manim import *


class PerimetroCuadrado(Scene):
    def construct(self):
        titulo = Text("Perímetro", font_size=48).to_edge(UP)
        cuadrado = Square(4, color=BLUE)
        viajero = Dot(cuadrado.get_start(), color=YELLOW)
        self.add(titulo)
        # El punto recorre el borde mientras este se dibuja
        self.play(Create(cuadrado),
                  MoveAlongPath(viajero, cuadrado),
                  run_time=4, rate_func=linear)
