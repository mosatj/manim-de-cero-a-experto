from manim import *


class TeselacionHexagonal(Scene):
    def construct(self):
        lado = 0.55
        colores = [BLUE_E, TEAL_E, GOLD_E]
        mosaico = VGroup()
        # Coordenadas axiales (i, j): los centros forman una red
        for i in range(-9, 10):
            for j in range(-10, 11):
                x = lado * 1.5 * i
                y = lado * np.sqrt(3) * (j + i / 2)
                if abs(x) > 7.6 or abs(y) > 4.5:
                    continue
                hexagono = RegularPolygon(6, radius=lado,
                                          stroke_width=2,
                                          stroke_color=WHITE)
                # (i - j) mod 3 garantiza que vecinos no se repiten
                hexagono.set_fill(colores[(i - j) % 3], opacity=0.9)
                mosaico.add(hexagono.move_to([x, y, 0]))
        aparicion = [FadeIn(h, scale=0.5) for h in mosaico]
        self.play(LaggedStart(*aparicion, lag_ratio=0.01),
                  run_time=3)
