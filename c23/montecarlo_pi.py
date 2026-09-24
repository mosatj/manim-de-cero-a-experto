from manim import *


class MontecarloPi(Scene):
    def construct(self):
        lado = 6
        cuadrado = Square(lado, color=WHITE).to_edge(LEFT, buff=0.8)
        circulo = Circle(lado / 2, color=YELLOW).move_to(cuadrado)
        centro = cuadrado.get_center()

        rng = np.random.default_rng(314)
        puntos = rng.uniform(-1, 1, size=(2000, 2))  # en [-1, 1]^2
        dentro = (puntos ** 2).sum(axis=1) <= 1

        formula = MathTex(r"\pi \approx 4\cdot\frac{\text{dentro}}"
                          r"{\text{total}}", font_size=44)
        estimacion = DecimalNumber(0, num_decimal_places=4,
                                   font_size=48, color=YELLOW)
        rotulo = MathTex(r"\pi \approx", font_size=48)
        linea_est = VGroup(rotulo, estimacion).arrange(RIGHT)
        contador = Tex("total: 0", font_size=36)
        panel = VGroup(formula, linea_est, contador).arrange(
            DOWN, buff=0.6).to_edge(RIGHT, buff=1)
        self.add(cuadrado, circulo, panel)

        inicio = 0
        for fin in [50, 250, 2000]:          # tres tandas de puntos
            tanda = VGroup(*[
                Dot(centro + lado / 2 * np.array([x, y, 0]),
                    radius=0.03, color=TEAL_C if d else RED_C)
                for (x, y), d in zip(puntos[inicio:fin],
                                     dentro[inicio:fin])
            ])
            valor = 4 * dentro[:fin].mean()
            nuevo = Tex(f"total: {fin}", font_size=36)
            nuevo.move_to(contador)
            self.play(
                LaggedStart(*[FadeIn(p) for p in tanda],
                            lag_ratio=0.01),
                ChangeDecimalToValue(estimacion, valor),
                Transform(contador, nuevo),
                run_time=2,
            )
            inicio = fin
        self.wait()
