from manim import *
import sympy as sp

x = sp.symbols("x")
INTEGRANDO = x * sp.exp(x)


class IntegralSimbolica(Scene):
    def construct(self):
        primitiva = sp.integrate(INTEGRANDO, x)
        definida = sp.integrate(INTEGRANDO, (x, 0, 1))
        lineas = VGroup(
            MathTex(r"\int " + sp.latex(INTEGRANDO) + r"\,dx = "
                    + sp.latex(primitiva) + " + C"),
            MathTex(r"\int_0^1 " + sp.latex(INTEGRANDO) + r"\,dx = "
                    + sp.latex(definida)
                    + r" \approx " + sp.latex(definida.evalf(4))),
        ).arrange(DOWN, buff=0.8)
        self.play(Write(lineas[0]))
        self.play(Write(lineas[1]))
        # Verificación: derivar la primitiva devuelve el integrando
        ok = sp.simplify(sp.diff(primitiva, x) - INTEGRANDO) == 0
        nota = Text("d/dx de la primitiva = integrando: "
                    + ("sí" if ok else "no"), font_size=26,
                    color=GREEN_C).to_edge(DOWN)
        self.play(FadeIn(nota))
        self.wait()
