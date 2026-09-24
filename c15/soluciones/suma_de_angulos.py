from manim import *


class SumaDeAngulos(Scene):
    def construct(self):
        A, B = np.array([-4, -2, 0]), np.array([3, -2, 0])
        c = ValueTracker(-1.0)                       # abscisa de C
        C = lambda: np.array([c.get_value(), 2, 0])

        def angulo_en(p, q, r):   # ángulo en p del triángulo pqr
            u, v = q - p, r - p
            return np.degrees(np.arccos(np.dot(u, v) / (
                np.linalg.norm(u) * np.linalg.norm(v))))

        triangulo = always_redraw(
            lambda: Polygon(A, B, C(), color=BLUE))
        fila = VGroup(*[DecimalNumber(0, num_decimal_places=1)
                        if k % 2 == 0 else MathTex(s)
                        for k, s in enumerate("0+0+0=0")])

        def actualizar(g):  # primero los valores, luego el acomodo
            angulos = [angulo_en(A, B, C()), angulo_en(B, C(), A),
                       angulo_en(C(), A, B)]
            for numero, v in zip(g[::2], angulos + [sum(angulos)]):
                numero.set_value(v)
            g.arrange(RIGHT).to_edge(UP)

        fila.add_updater(actualizar, call_updater=True)
        self.add(triangulo, fila)
        self.play(c.animate.set_value(5), run_time=3)
