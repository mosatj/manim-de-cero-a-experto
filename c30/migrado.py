from manim import *


class Migrado(Scene):
    def construct(self):
        # GraphScene + CONFIG  ->  un objeto Axes con parámetros
        ejes = Axes(x_range=[-3, 3, 1], y_range=[-1, 9, 2],
                    x_length=6, y_length=5).to_edge(LEFT)
        self.play(Create(ejes))                      # ShowCreation
        curva = ejes.plot(lambda x: x**2, color=BLUE)  # get_graph
        etiqueta = ejes.get_graph_label(curva, label="x^2")
        self.play(Create(curva), Write(etiqueta))
        punto = Dot(ejes.c2p(2, 4), color=YELLOW)  # coords_to_point
        texto = Tex("Antes: GraphScene").to_edge(RIGHT)
        self.play(punto.animate.shift(UP),           # ApplyMethod
                  FadeIn(texto, shift=RIGHT))         # FadeInFrom
        self.play(Rotating(punto, angle=PI,           # radians=PI
                           about_point=ejes.c2p(2, 4)), run_time=1)
        ahora = Tex("Ahora: Axes").to_edge(RIGHT)
        self.play(Transform(texto, ahora))
