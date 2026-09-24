from manim import *


def cortes(c1, c2, r):
    """Cortes de dos circunferencias de igual radio r."""
    m, d = (c1 + c2) / 2, np.linalg.norm(c2 - c1)
    u = (c2 - c1) / d
    n = np.array([-u[1], u[0], 0])
    h = np.sqrt(r**2 - (d / 2)**2)
    return m + h * n, m - h * n


class Mediatriz(Scene):
    def construct(self):
        A, B = np.array([-2, -0.5, 0]), np.array([2, 0.5, 0])
        r = 0.75 * np.linalg.norm(B - A)     # cualquier r > AB/2
        self.add(Line(A, B), Dot(A), Dot(B))
        self.play(Create(Circle(r, color=BLUE).move_to(A)),
                  Create(Circle(r, color=TEAL).move_to(B)))
        P, Q = cortes(A, B, r)
        self.play(FadeIn(Dot(P, color=YELLOW)),
                  FadeIn(Dot(Q, color=YELLOW)))
        recta = Line(P, Q, color=YELLOW).scale(1.4)
        self.play(Create(recta))
        self.add(Dot((A + B) / 2, color=RED),
                 RightAngle(Line((A + B) / 2, B),
                            Line((A + B) / 2, P), length=0.25))
