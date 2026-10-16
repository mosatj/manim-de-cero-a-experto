from manim import *


class Reticula:
    """Retícula modular: columnas y filas dentro de un margen."""

    def __init__(self, columnas=6, filas=4, margen=0.6, medianil=0.3):
        self.columnas, self.filas = columnas, filas
        self.medianil = medianil
        ancho = config.frame_width - 2 * margen
        alto = config.frame_height - 2 * margen
        self.col = (ancho - (columnas - 1) * medianil) / columnas
        self.fil = (alto - (filas - 1) * medianil) / filas
        self.x0, self.y0 = -ancho / 2, alto / 2  # esquina sup. izq.

    def zona(self, c0, c1, f0, f1):
        """Rectángulo de las columnas c0..c1 y las filas f0..f1."""
        paso_x = self.col + self.medianil
        paso_y = self.fil + self.medianil
        izq = self.x0 + c0 * paso_x
        der = self.x0 + (c1 + 1) * paso_x - self.medianil
        sup = self.y0 - f0 * paso_y
        inf = self.y0 - (f1 + 1) * paso_y + self.medianil
        return Rectangle(width=der - izq, height=sup - inf).move_to(
            [(izq + der) / 2, (sup + inf) / 2, 0])

    def colocar(self, mob, c0, c1, f0, f1, borde=UL):
        zona = self.zona(c0, c1, f0, f1)
        return mob.move_to(zona.get_corner(borde), aligned_edge=borde)

    def guias(self):
        columnas = [self.zona(c, c, 0, self.filas - 1)
                    for c in range(self.columnas)]
        return VGroup(*columnas).set_stroke(GRAY, 1, opacity=0.6)


def piezas():
    titulo = Text("Teorema de Pitágoras", font_size=48)
    tri = Polygon(ORIGIN, 4.6 * RIGHT, 4.6 * RIGHT + 3.4 * UP,
                  color=BLUE, stroke_width=6)
    a = MathTex("a").next_to(tri, DOWN)
    b = MathTex("b").next_to(tri, RIGHT)
    normal = np.array([-3.4, 4.6, 0]) / 5.72  # perpendicular a c
    c = MathTex("c").move_to([2.3, 1.7, 0] + 0.45 * normal)
    formula = MathTex(r"a^2+b^2=c^2", font_size=80)
    nota = Text("solo si el ángulo es recto", font_size=40)
    return titulo, VGroup(tri, a, b, c), formula, nota


class ReticulaAntes(Scene):
    def construct(self):
        titulo, figura, formula, nota = piezas()
        titulo.move_to([-0.6, 3.3, 0])  # cada pieza «donde cupo»
        figura.move_to([-3.9, -0.3, 0])
        formula.move_to([3.1, 1.4, 0])
        nota.move_to([3.7, -2.9, 0])
        self.add(titulo, figura, formula, nota)


class ReticulaDespues(Scene):
    def construct(self):
        r = Reticula()
        titulo, figura, formula, nota = piezas()
        r.colocar(titulo, 0, 5, 0, 0)
        r.colocar(figura, 0, 2, 1, 3)
        r.colocar(formula, 3, 5, 1, 1)
        r.colocar(nota, 3, 5, 2, 2)
        self.add(r.guias(), titulo, figura, formula, nota)
