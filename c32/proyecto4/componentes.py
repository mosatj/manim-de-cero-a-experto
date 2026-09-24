from manim import *

COLOR_SEN, COLOR_COS, COLOR_UNO = "#E0B04A", "#6FA3C0", "#B04A5A"


class CirculoUnitario(VGroup):
    """Circunferencia de radio 1 (dibujada con radio r en pantalla),
    un ángulo controlado por un ValueTracker y su triángulo."""

    def __init__(self, r=3.0, angulo=PI / 5, **kwargs):
        super().__init__(**kwargs)
        self.r = r
        self.theta = ValueTracker(angulo)
        self.circulo = Circle(r, color=GREY_B, stroke_width=3)
        self.ejes = VGroup(
            Line(LEFT * (r + 0.4), RIGHT * (r + 0.4)),
            Line(DOWN * (r + 0.4), UP * (r + 0.4)),
        ).set_stroke(GREY, 2)
        self.triangulo = always_redraw(self._triangulo)
        self.add(self.ejes, self.circulo, self.triangulo)

    def centro(self):
        return self.circulo.get_center()

    def punto(self):
        t = self.theta.get_value()
        return self.centro() + self.r * np.array(
            [np.cos(t), np.sin(t), 0]
        )

    def _triangulo(self):
        o, p = self.centro(), self.punto()
        pie = np.array([p[0], o[1], 0])
        return VGroup(
            Line(o, pie, color=COLOR_COS, stroke_width=9),
            Line(pie, p, color=COLOR_SEN, stroke_width=9),
            Line(o, p, color=COLOR_UNO, stroke_width=6),
            Dot(p, radius=0.1, color=WHITE),
        )
