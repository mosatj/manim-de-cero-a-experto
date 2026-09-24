from manim import *


class Darboux(Scene):
    def construct(self):
        f = lambda x: 2 * (x - 1)**2 - (x - 1)**3 + 3
        criticos = [1, 7 / 3]                  # f'(x) = 0
        a, b, n = 0, 3, 8
        dx = (b - a) / n
        ejes = Axes(x_range=[-0.2, 3.2, 1], y_range=[0, 7, 1],
                    x_length=8, y_length=6, tips=False)
        ejes.add_coordinates(font_size=22).to_edge(LEFT)
        curva = ejes.plot(f, x_range=[-0.1, 3.2], color=WHITE)
        superior, inferior, U, L = VGroup(), VGroup(), 0, 0
        for i in range(n):
            x0, x1 = a + i * dx, a + (i + 1) * dx
            # En [x0, x1] los extremos de f están en los bordes
            # o en los puntos críticos interiores
            dentro = [c for c in criticos if x0 < c < x1]
            candidatos = [x0, x1] + dentro
            M = max(f(c) for c in candidatos)
            m = min(f(c) for c in candidatos)
            U, L = U + M * dx, L + m * dx
            for alto, grupo, color in [(M, superior, RED),
                                       (m, inferior, BLUE)]:
                p = ejes.c2p
                grupo.add(Polygon(p(x0, 0), p(x1, 0),
                                  p(x1, alto), p(x0, alto),
                                  color=color, fill_opacity=0.45,
                                  stroke_width=1))
        texto = MathTex(rf"U_8={U:.4f}", rf"L_8={L:.4f}",
                        rf"U_8-L_8={U - L:.4f}", r"I=11.25")
        texto.arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT)
        texto[0].set_color(RED)
        texto[1].set_color(BLUE)
        self.add(ejes, superior, inferior, curva, texto)
