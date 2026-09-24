from manim import *


class Determinante(Scene):
    def construct(self):
        plano = NumberPlane()
        cuadrado = Square(side_length=1, color=YELLOW,
                          fill_opacity=0.6)
        cuadrado.move_to([0.5, 0.5, 0])
        matriz = [[3, 1], [1, 1]]            # det = 3·1 - 1·1 = 2
        self.add(plano, cuadrado)
        self.play(ApplyMatrix(matriz, VGroup(plano, cuadrado)),
                  run_time=2)
        area = MathTex(r"\text{área} = |\det A| = 2", font_size=48)
        area.to_corner(UL).add_background_rectangle()
        self.play(Write(area))
