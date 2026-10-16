from manim import *
import os
import sympy as sp

# La fórmula llega por una variable de entorno:
#   FUNCION="sin(x)*x" manim -pql py_parametros.py \
#       GraficaParametrica
TEXTO = os.environ.get("FUNCION", "x**2 - 2")
x = sp.symbols("x")
EXPRESION = sp.sympify(TEXTO)


class GraficaParametrica(Scene):
    def construct(self):
        ejes = Axes(x_range=[-3, 3, 1], y_range=[-3, 7, 1],
                    x_length=9, y_length=5.5, tips=False)
        f = sp.lambdify(x, EXPRESION, "numpy")
        curva = ejes.plot(f, x_range=[-3, 3], color=BLUE_C)
        rotulo = MathTex("f(x)=" + sp.latex(EXPRESION),
                         font_size=40)
        rotulo.to_edge(UP)
        raices = [r for r in sp.solve(EXPRESION, x) if r.is_real]
        puntos = VGroup(*[Dot(ejes.c2p(float(r), 0), color=RED)
                          for r in raices if abs(float(r)) <= 3])
        self.play(Create(ejes), Write(rotulo))
        self.play(Create(curva))
        self.play(FadeIn(puntos, scale=2))
        self.wait()
