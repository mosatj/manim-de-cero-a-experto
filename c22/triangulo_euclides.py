from manim import *


def cortes_circunferencias(c1, r1, c2, r2):
    """Los dos puntos de corte de dos circunferencias del plano."""
    d = np.linalg.norm(c2 - c1)
    a = (r1**2 - r2**2 + d**2) / (2 * d)   # de c1 a la cuerda
    h = np.sqrt(r1**2 - a**2)              # media cuerda
    u = (c2 - c1) / d                      # unitario de c1 hacia c2
    n = np.array([-u[1], u[0], 0])         # perpendicular a u
    m = c1 + a * u                         # pie de la cuerda
    return m + h * n, m - h * n


class TrianguloEuclides(Scene):
    def construct(self):
        A, B = np.array([-1.5, -0.8, 0]), np.array([1.5, -0.8, 0])
        lado = np.linalg.norm(B - A)
        segmento = Line(A, B, color=WHITE)
        rotulos = VGroup(MathTex("A").next_to(A, DL, buff=0.1),
                         MathTex("B").next_to(B, DR, buff=0.1))
        self.add(segmento, Dot(A), Dot(B), rotulos)
        # 1) Circunferencia de centro A que pasa por B
        c_a = Circle(radius=lado, color=BLUE).move_to(A)
        self.play(Create(c_a), run_time=1.5)
        # 2) Circunferencia de centro B que pasa por A
        c_b = Circle(radius=lado, color=TEAL).move_to(B)
        self.play(Create(c_b), run_time=1.5)
        # 3) C es uno de los puntos de corte
        C, _ = cortes_circunferencias(A, lado, B, lado)
        self.play(FadeIn(Dot(C, color=YELLOW), scale=3),
                  Write(MathTex("C").next_to(C, UP, buff=0.15)))
        # 4) El triángulo: AC = AB (radios de c_a), BC = BA (c_b)
        triangulo = Polygon(A, B, C, color=YELLOW, stroke_width=6)
        self.play(Create(triangulo))
