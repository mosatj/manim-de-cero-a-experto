from manim import *
import sympy as sp

# SymPy escribe cada paso; Manim solo lo muestra
x = sp.symbols("x")
f = x**2 * sp.sin(x)


class DerivadaSimbolica(Scene):
    def construct(self):
        pasos = [
            sp.Eq(sp.Function("f")(x), f),
            sp.Eq(sp.Derivative(f, x), sp.diff(f, x)),
            sp.Eq(sp.Symbol("f'(x)"), sp.factor(sp.diff(f, x))),
        ]
        lineas = VGroup(*[
            MathTex(sp.latex(p), font_size=44) for p in pasos
        ]).arrange(DOWN, buff=0.7)
        lineas[0].set_color(BLUE_C)
        lineas[2].set_color(GREEN_C)
        titulo = Text("Regla del producto, calculada por SymPy",
                      font_size=30).to_edge(UP)
        self.play(Write(titulo), Write(lineas[0]))
        for anterior, linea in zip(lineas, lineas[1:]):
            self.play(TransformFromCopy(anterior, linea))
            self.wait(0.5)
        # Comprobación numérica en un punto, también desde SymPy
        valor = sp.diff(f, x).subs(x, 1).evalf(4)
        nota = MathTex(rf"f'(1) \approx {sp.latex(valor)}",
                       font_size=36).to_edge(DOWN)
        self.play(FadeIn(nota))
        self.wait()
