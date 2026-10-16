from manim import *
import sympy as sp

x = sp.symbols("x")
F = sp.cos(x)


def taylor(n):
    """Polinomio de Taylor de orden < n en x = 0."""
    return sp.series(F, x, 0, n).removeO()


class TaylorSymPy(Scene):
    def construct(self):
        ejes = Axes(x_range=[-7, 7, 1], y_range=[-2, 2, 1],
                    x_length=12, y_length=5, tips=False)
        curva = ejes.plot(sp.lambdify(x, F, "numpy"), color=BLUE_C)
        self.add(ejes, curva)
        rotulo_f = MathTex(sp.latex(F), color=BLUE_C).to_corner(UL)
        self.add(rotulo_f)
        aprox = None
        for n in (2, 4, 6, 8, 10):
            p = taylor(n)
            nueva = ejes.plot(sp.lambdify(x, p, "numpy"),
                              x_range=[-6.5, 6.5], color=ORANGE)
            texto = MathTex("P_{%d}(x) = " % (n - 2) + sp.latex(p),
                            font_size=32, color=ORANGE)
            texto.to_edge(DOWN)
            if aprox is None:
                aprox, rotulo = nueva, texto
                self.play(Create(aprox), Write(rotulo))
            else:
                self.play(Transform(aprox, nueva),
                          Transform(rotulo, texto))
            self.wait(0.6)
