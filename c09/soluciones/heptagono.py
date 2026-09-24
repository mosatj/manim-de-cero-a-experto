from manim import *


class Heptagono(Scene):
    def construct(self):
        n = 7
        inicial = 3 * UP
        # Vértice k: el inicial girado k/n de vuelta
        vertices = [rotate_vector(inicial, k * TAU / n)
                    for k in range(n)]
        self.add(Circle(3, color=GRAY))
        self.add(Polygon(*vertices, color=BLUE,
                         fill_opacity=0.3))
        self.add(*[Dot(v, color=YELLOW) for v in vertices])
