from manim import *

A, B = np.array([0.0, 0.0]), np.array([6.0, 0.0])


def notables(t):
    """C, O, H y N del triángulo de asy_euler_movil.asy."""
    ang = np.radians(50 + 80 * t)
    c = np.array([3 + 3.5 * np.cos(ang), 3.5 * np.sin(ang)])
    o = np.array([3, (c @ c - 6 * c[0]) / (2 * c[1])])
    h = A + B + c - 2 * o            # Euler: H = A + B + C - 2 O
    return c, o, h, (o + h) / 2


def escena(p):
    """Coordenadas del dibujo -> escena: escala y desplazamiento."""
    return np.array([*(0.85 * (p - [3, 1])), 0]) + LEFT * 3


class EulerManim(Scene):
    """El mismo triángulo móvil, recalculado en cada fotograma."""

    def construct(self):
        t = ValueTracker(0)

        def figura():
            c, o, h, n = notables(t.get_value())
            r = np.linalg.norm(o - A) * 0.85
            u = (h - o) / np.linalg.norm(h - o)
            return VGroup(
                Polygon(*[escena(p) for p in (A, B, c)],
                        color="#E9F2F7"),
                Circle(r, color="#E0B04A").move_to(escena(o)),
                Circle(r / 2, color="#7FB89A").move_to(escena(n)),
                Line(escena(n - 3 * u), escena(n + 3 * u),
                     color="#B04A5A", stroke_width=6),
                Dot(escena(o), color="#E0B04A"),
                Dot(escena(h), color="#7FB89A"),
            )

        dibujo = always_redraw(figura)
        # Recorrido de H hasta el valor actual de t: siempre exacto
        rastro = always_redraw(lambda: ParametricFunction(
            lambda s: escena(notables(s)[2]),
            t_range=[0, max(t.get_value(), 1e-3)],
            color="#7FB89A", stroke_width=5))
        texto = VGroup(
            Text("Recalculado en cada fotograma:", font_size=32),
            Text("el rastro de H es suave", font_size=32,
                 color="#7FB89A"),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UR, buff=0.4)
        self.add(dibujo, rastro, texto)
        self.play(t.animate.set_value(1), run_time=5,
                  rate_func=linear)
        self.wait()
