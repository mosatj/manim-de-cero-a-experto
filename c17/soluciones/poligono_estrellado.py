from manim import *


class PoligonoEstrellado(VMobject):
    """Polígono {n/k}: une cada vértice con el k-ésimo siguiente."""

    def __init__(self, n=5, k=2, radio=1.5, **kwargs):
        self.n, self.k, self.radio = n, k, radio  # antes de super()
        super().__init__(**kwargs)

    def generate_points(self):
        angulos = [PI / 2 + TAU * self.k * j / self.n
                   for j in range(self.n + 1)]
        vertices = [self.radio * np.array([np.cos(a), np.sin(a), 0])
                    for a in angulos]
        self.set_points_as_corners(vertices)
        return self


class EscenaEstrellados(Scene):
    def construct(self):
        tipos = [(5, 2), (7, 2), (7, 3), (9, 4)]
        figuras = VGroup()
        for n, k in tipos:
            figura = PoligonoEstrellado(n, k, radio=1.3, color=BLUE)
            rotulo = MathTex(rf"\{{{n}/{k}\}}", font_size=40)
            rotulo.next_to(figura, DOWN)
            figuras.add(VGroup(figura, rotulo))
        figuras.arrange(RIGHT, buff=0.6)
        self.play(LaggedStart(*[Create(f[0]) for f in figuras],
                              lag_ratio=0.3), run_time=3)
        self.add(*[f[1] for f in figuras])
        self.wait()
