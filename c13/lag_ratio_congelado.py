from manim import *
from congelar import congelar


class LagRatioCongelado(Scene):
    def construct(self):
        casos = [(0, "AnimationGroup (lag_ratio=0)"),
                 (0.25, "LaggedStart(lag_ratio=0.25)"),
                 (0.5, "LaggedStart(lag_ratio=0.5)"),
                 (1, "Succession (lag_ratio=1)")]
        for k, (lag, nombre) in enumerate(casos):
            fila = VGroup(*[
                Square(side_length=0.8, color=TEAL,
                       fill_opacity=0.8)
                for _ in range(6)
            ]).arrange(RIGHT, buff=0.25)
            fila.move_to([2.2, 2.7 - 1.8 * k, 0])
            grupo = AnimationGroup(
                *[GrowFromCenter(c) for c in fila], lag_ratio=lag)
            # Siluetas del estado final, como referencia
            self.add(fila.copy().set_fill(opacity=0).set_stroke(
                GRAY_D, 1.5))
            congelar(self, grupo, 0.5)   # a mitad del tiempo total
            rotulo = Text(nombre, font="Monospace", font_size=20)
            rotulo.next_to(fila, LEFT, buff=0.5)
            self.add(rotulo)
