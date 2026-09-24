from manim import *
from componentes import Tarjeta  # módulo de esta carpeta


class Tarjetas(Scene):
    def construct(self):
        datos = [
            ("Pitágoras", r"a^2+b^2=c^2", BLUE),
            ("Euler", r"e^{i\pi}+1=0", GREEN),
            ("Binomio", r"(a+b)^2=a^2+2ab+b^2", ORANGE),
            ("Gauss", r"\sum_{k=1}^{n}k=\frac{n(n+1)}{2}", PURPLE),
        ]
        tarjetas = VGroup(*[Tarjeta(t, f, c) for t, f, c in datos])
        tarjetas.arrange_in_grid(rows=2, cols=2, buff=0.5)
        entradas = [FadeIn(x, shift=UP) for x in tarjetas]
        self.play(LaggedStart(*entradas, lag_ratio=0.25))
        # Cada tarjeta expone sus partes como atributos
        self.play(tarjetas[1].formula.animate.set_color(YELLOW),
                  tarjetas[1].animate.resaltar())
        self.wait()
