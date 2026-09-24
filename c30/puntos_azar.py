import random

from manim import *


class PuntosAzar(Scene):
    def construct(self):
        # Manim siembra random si se usa --seed o config.seed
        puntos = VGroup()
        for _ in range(150):
            x, y = random.uniform(-6, 6), random.uniform(-3.5, 3.5)
            color = random.choice([BLUE_E, TEAL_E, GOLD_E])
            puntos.add(Dot([x, y, 0], radius=0.07, color=color))
        self.play(LaggedStartMap(FadeIn, puntos, lag_ratio=0.01))
        primero = puntos[0].get_center()
        rotulo = Text(f"primer punto: ({primero[0]:.3f}, "
                      f"{primero[1]:.3f})", font_size=30)
        self.add(BackgroundRectangle(rotulo.to_edge(DOWN)), rotulo)
