from manim import *


class NubeAleatoria(Scene):
    def construct(self):
        gen = np.random.default_rng(2026)    # siempre la misma nube
        p = gen.uniform(-1, 1, size=(600, 2))
        dentro = (p**2).sum(axis=1) <= 1
        lado = 3                              # semilado en unidades
        cuadro = Square(side_length=2 * lado, color=GREY_B)
        circulo = Circle(radius=lado, color=WHITE, stroke_width=2)
        puntos = VGroup(*[
            Dot(lado * np.array([x, y, 0]), radius=0.04,
                color=YELLOW if d else BLUE)
            for (x, y), d in zip(p, dentro)])
        pi_aprox = 4 * dentro.mean()
        estimacion = MathTex(rf"\pi \approx {pi_aprox:.3f}")
        estimacion.next_to(cuadro, RIGHT, buff=0.6)
        self.add(cuadro, circulo)
        self.play(LaggedStart(*[FadeIn(d) for d in puntos],
                              lag_ratio=0.01), run_time=3)
        self.play(Write(estimacion))
