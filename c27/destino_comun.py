from manim import *


class DestinoComun(Scene):
    def construct(self):
        # Doce puntos idénticos: nada los agrupa... hasta que se mueven
        puntos = VGroup(*[Dot(radius=0.15, color=GREY)
                          for _ in range(12)])
        puntos.arrange_in_grid(rows=3, cols=4, buff=0.9)
        elegidos = VGroup(puntos[1], puntos[4], puntos[6], puntos[11])
        self.add(puntos)
        self.wait()
        # Moverse juntos (destino común) crea el grupo, sin color
        self.play(elegidos.animate.shift(0.6 * UP), run_time=0.8)
        # Al volver, ya se puede nombrar lo que el ojo agrupó
        self.play(elegidos.animate.shift(0.6 * DOWN).set_color(ORANGE))
