from manim import *


class TresEntradas(Scene):
    def construct(self):
        rect = RoundedRectangle(corner_radius=0.2, color=RED,
                                fill_opacity=0.4)
        r1 = rect.copy().shift(LEFT * 4.5)
        r2 = rect.copy()
        r3 = rect.copy().shift(RIGHT * 4.5)

        self.play(Write(r1))                # 1: a mano
        self.play(DrawBorderThenFill(r2))   # 2: borde y fondo
        self.play(FadeIn(r3))               # 3: fundido
        nombres = ["Write", "DrawBorderThenFill", "FadeIn"]
        for r, nombre in zip([r1, r2, r3], nombres):
            etiqueta = Text(nombre, font_size=28)
            etiqueta.next_to(r, DOWN)
            self.add(etiqueta)
        self.wait()
