from manim import *


class TrianguloConAltura(VGroup):
    """Triángulo ABC con su altura desde C hasta la recta AB."""

    def __init__(self, a, b, c, **kwargs):
        super().__init__(**kwargs)
        a, b, c = (np.array([p[0], p[1], 0.0]) for p in (a, b, c))
        ab = b - a
        t = np.dot(c - a, ab) / np.dot(ab, ab)
        pie = a + t * ab  # pie H de la perpendicular
        # u: dirección de la base que apunta hacia el segmento AB
        u = normalize(b - pie if t <= 0.5 else a - pie)
        v = normalize(c - pie)
        self.triangulo = Polygon(a, b, c, color=WHITE,
                                 fill_color=BLUE, fill_opacity=0.25)
        self.base = Line(a, b, color=BLUE, stroke_width=7)
        # Si el pie cae fuera de AB, la base se prolonga
        if t < 0 or t > 1:
            extremo = a if t < 0 else b
            self.prolongacion = DashedLine(
                extremo, pie - 0.4 * u, color=GRAY_B
            )
        else:
            self.prolongacion = VMobject()
        self.altura = Line(c, pie, color=RED, stroke_width=7)
        s = 0.22  # lado de la marca de ángulo recto
        self.marca = VMobject(color=RED, stroke_width=3)
        self.marca.set_points_as_corners(
            [pie + s * u, pie + s * (u + v), pie + s * v]
        )
        self.h = MathTex("h", color=RED, font_size=44)
        self.h.move_to((c + pie) / 2 - 0.32 * u)
        self.add(self.prolongacion, self.triangulo, self.base,
                 self.altura, self.marca, self.h)


class VariacionAltura(Scene):
    def construct(self):
        prototipo = [(-2, -1), (2, -1), (-0.5, 1.3)]
        girado = [
            0.8 * rotate_vector(np.array([x, y, 0]), 35 * DEGREES)
            for x, y in prototipo
        ]
        casos = [  # una sola variación por panel
            ("prototipo", prototipo),
            ("girado y escalado", girado),
            ("rectángulo", [(-2, -1), (2, -1), (-2, 1.3)]),
            ("obtuso", [(-2.2, -1), (0.4, -1), (2, 1.3)]),
        ]
        paneles = VGroup()
        for rotulo, vertices in casos:
            figura = TrianguloConAltura(*vertices)
            texto = Text(rotulo, font_size=32)
            texto.next_to(figura, DOWN, buff=0.3)
            paneles.add(VGroup(figura, texto))
        paneles.arrange_in_grid(rows=2, cols=2, buff=(1.4, 0.7))
        for figura, texto in paneles:
            self.play(Create(figura.triangulo), Create(figura.base),
                      Create(figura.prolongacion))
            self.play(Create(figura.altura), Create(figura.marca),
                      Write(figura.h), FadeIn(texto))
        # Lo que no cambia: la perpendicular a la recta de la base
        self.play(*[Indicate(f.marca, scale_factor=1.8)
                    for f, _ in paneles])
        self.wait()
