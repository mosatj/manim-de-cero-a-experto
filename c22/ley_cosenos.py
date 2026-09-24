from manim import *


def angulo(u, v):
    """Ángulo orientado (radianes) que lleva el vector u al v."""
    return np.arctan2(u[0] * v[1] - u[1] * v[0], np.dot(u, v))


class LeyCosenos(Scene):
    def construct(self):
        # Triángulo con c = AB = 3, a = BC = 6 y B = 50 grados
        B = np.array([-5.8, -2.8, 0])
        C = B + 6 * RIGHT
        A = B + 3 * np.array([np.cos(50 * DEGREES),
                              np.sin(50 * DEGREES), 0])
        c = np.linalg.norm(A - B)
        u_ca = (A - C) / np.linalg.norm(A - C)
        D, G = A - c * u_ca, A + c * u_ca   # CA corta el círculo
        E = 2 * A - B                       # BE es un diámetro
        F = B + 2 * c * np.cos(50 * DEGREES) * RIGHT   # pie en BC
        tri = Polygon(A, B, C, color=WHITE)
        nombres = VGroup(*[
            MathTex(n, font_size=36).next_to(p, d, 0.1)
            for n, p, d in (("A", A, UP), ("B", B, DL),
                            ("C", C, DR))])
        self.add(tri, nombres)
        # 1) Circunferencia de centro A y radio c; AB gira hasta AD
        circ = Circle(radius=c, color=BLUE).move_to(A)
        radio = Line(A, B, color=YELLOW, stroke_width=6)
        self.play(Create(circ))
        self.play(Rotate(radio, angle=angulo(B - A, D - A),
                         about_point=A))
        # 2) Diámetro BE y ángulo recto en F (ángulo inscrito)
        diam = DashedLine(B, E, color=BLUE)
        recto = RightAngle(Line(F, B), Line(F, E), length=0.25)
        self.play(Create(diam), Create(Line(F, E, color=BLUE)),
                  Create(recto))
        # 3) La secante C-D-G completa la figura
        self.play(Create(Line(D, G, color=GREEN)))
        for n, p, d in (("D", D, UR), ("E", E, UP), ("F", F, DOWN),
                        ("G", G, UL)):
            self.add(Dot(p, radius=0.05), MathTex(n, font_size=32)
                     .next_to(p, d, 0.1))
        # 4) Potencia del punto C respecto de la circunferencia
        pasos = VGroup(
            MathTex(r"CD \cdot CG = CF \cdot CB"),
            MathTex(r"(b - c)(b + c) = (a - 2c\cos B)\,a"),
            MathTex(r"b^2 = a^2 + c^2 - 2ac\cos B"),
        ).scale(0.8).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        pasos.to_corner(UR, buff=0.5)
        self.play(Write(pasos[0]))
        self.play(TransformMatchingTex(pasos[0].copy(), pasos[1]))
        self.play(Write(pasos[2]), Create(SurroundingRectangle(
            pasos[2], color=YELLOW)))
