from manim import *


class GaleriaGeometria(Scene):
    def construct(self):
        # Triángulo rectángulo 3-4-5 con un cuadrado sobre cada lado
        a, b, c = [0, 0, 0], [2.4, 0, 0], [0, 1.8, 0]
        triangulo = Polygon(a, b, c, color=WHITE, fill_opacity=0.2)

        def cuadrado_sobre(p, q, color):
            p, q = np.array(p), np.array(q)
            normal = rotate_vector(q - p, -PI / 2)
            return Polygon(p, q, q + normal, p + normal, color=color,
                           fill_opacity=0.5)

        cuadrados = VGroup(cuadrado_sobre(a, b, BLUE),
                           cuadrado_sobre(c, a, GREEN),
                           cuadrado_sobre(b, c, RED))
        figura = VGroup(triangulo, cuadrados).move_to(1.8 * LEFT)
        formula = MathTex(r"a^2 + b^2 = c^2", font_size=64)
        formula.to_edge(RIGHT, buff=1)
        self.add(figura, formula)
