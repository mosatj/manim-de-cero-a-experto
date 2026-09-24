from manim import *


class CreateVsRelleno(Scene):
    def construct(self):
        izquierdo = Square(side_length=3, color=BLUE,
                           fill_opacity=0.7)
        derecho = izquierdo.copy()
        VGroup(izquierdo, derecho).arrange(RIGHT, buff=2)
        nombres = VGroup(
            Text("Create").next_to(izquierdo, DOWN),
            Text("DrawBorderThenFill").next_to(derecho, DOWN),
        )
        self.add(nombres)
        # Misma duración para comparar con justicia
        self.play(Create(izquierdo), DrawBorderThenFill(derecho),
                  run_time=2)
