from manim import *

# Configuración global: vale para todas las escenas
# de este archivo (va fuera de la clase).
config.background_color = "#F4F1EA"


class FondoClaro(Scene):
    def construct(self):
        titulo = Text("Fondo claro", color="#0B2A3C")
        titulo.to_edge(UP)
        triangulo = Triangle(color="#B3174A",
                             fill_opacity=0.6).scale(2)
        self.play(Write(titulo), Create(triangulo))
        self.wait()
