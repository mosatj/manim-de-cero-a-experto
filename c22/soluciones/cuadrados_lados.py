from manim import *


def cuadrado_exterior(P, Q, interior):
    """Cuadrado sobre PQ, del lado opuesto al punto interior."""
    v = Q - P
    n = np.array([-v[1], v[0], 0])           # PQ girado 90 grados
    if np.dot(n, interior - P) > 0:          # apunta hacia dentro:
        n = -n                               # le damos la vuelta
    return Polygon(P, Q, Q + n, P + n)


class CuadradosLados(Scene):
    def construct(self):
        s = 0.25                             # escala: 5-12-13
        C = np.array([-1.5, -0.4, 0])        # ángulo recto en C
        A, B = C + 12 * s * RIGHT, C + 5 * s * UP
        tri = Polygon(A, B, C, color=WHITE)
        G = (A + B + C) / 3                  # un punto interior
        datos = ((C, A, "b^2 = 144", GREEN),
                 (C, B, "a^2 = 25", RED),
                 (A, B, "c^2 = 169", YELLOW))
        grupo = VGroup(tri)
        for P, Q, texto, color in datos:
            cuad = cuadrado_exterior(P, Q, G).set_fill(color, 0.3)
            cuad.set_stroke(color)
            grupo.add(cuad, MathTex(texto, font_size=30)
                      .move_to(cuad))
        self.play(Create(grupo, lag_ratio=0.3), run_time=3)
