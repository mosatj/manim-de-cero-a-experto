from manim import *
from estilo import COLOR_A, COLOR_B, COLOR_C, COLOR_TRIANGULO


def triangulo(a, b):
    """Triángulo rectángulo con el ángulo recto en el origen."""
    return Polygon(
        ORIGIN,
        RIGHT * a,
        UP * b,
        color=WHITE,
        fill_color=COLOR_TRIANGULO,
        fill_opacity=0.9,
        stroke_width=3,
    )


class MarcoPitagoras(VGroup):
    """Cuadrado de lado a + b con cuatro triángulos, en dos
    disposiciones:

    1: un triángulo por esquina; el hueco es el cuadrado de lado c.
    2: dos rectángulos a x b; los huecos son los cuadrados a y b.
    """

    GIROS = [0, PI / 2, PI, 3 * PI / 2]

    def __init__(self, a=2.0, b=1.3, **kwargs):
        super().__init__(**kwargs)
        self.a, self.b, self.l = a, b, a + b
        self.marco = Square(self.l, color=WHITE).move_to(
            (RIGHT + UP) * self.l / 2
        )
        self.triangulos = VGroup(
            *[triangulo(a, b) for _ in range(4)]
        )
        self.add(self.marco, self.triangulos)
        for t, d in zip(self.triangulos, self.destinos(1)):
            t.become(d)

    def anclas(self, disposicion):
        """Dónde va el ángulo recto de cada triángulo."""
        a, b, l = self.a, self.b, self.l
        if disposicion == 1:
            return [ORIGIN, RIGHT * l, RIGHT * l + UP * l, UP * l]
        return [
            ORIGIN,
            RIGHT * l + UP * b,
            RIGHT * a + UP * b,
            RIGHT * a + UP * l,
        ]

    def destinos(self, disposicion):
        """Cuatro triángulos nuevos en la disposición pedida. De 1
        a 2 cada triángulo solo se traslada: no gira ni cambia."""
        o = self.marco.get_corner(DL)
        return VGroup(
            *[
                triangulo(self.a, self.b)
                .rotate(giro, about_point=ORIGIN)
                .shift(o + ancla)
                for giro, ancla in zip(
                    self.GIROS, self.anclas(disposicion)
                )
            ]
        )

    def hueco_c(self):
        # El vértice agudo (índice 1) toca el hueco
        puntos = [t.get_vertices()[1] for t in self.destinos(1)]
        return Polygon(*puntos, color=COLOR_C, fill_opacity=0.85)

    def huecos_ab(self):
        o, a, b = self.marco.get_corner(DL), self.a, self.b
        cuad_a = Square(
            a, color=COLOR_A, fill_opacity=0.85
        ).move_to(o + RIGHT * a / 2 + UP * (b + a / 2))
        cuad_b = Square(
            b, color=COLOR_B, fill_opacity=0.85
        ).move_to(o + RIGHT * (a + b / 2) + UP * b / 2)
        return VGroup(cuad_a, cuad_b)


def rotulo(tex, objeto):
    """Rótulo centrado sobre una región (c^2, a^2, b^2)."""
    return MathTex(tex, color=BLACK, font_size=40).move_to(objeto)


def par_de_marcos():
    """Los dos cuadrados de la demostración, uno junto al otro."""
    izquierda = MarcoPitagoras().move_to(LEFT * 3.4 + UP * 0.5)
    derecha = MarcoPitagoras().move_to(RIGHT * 3.4 + UP * 0.5)
    return izquierda, derecha
