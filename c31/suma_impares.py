from manim import *


class SumaImpares(Scene):
    """Argumento sin palabras: 1 + 3 + ... + (2n - 1) = n^2."""

    def construct(self):
        n, lado = 5, 0.7
        colores = color_gradient(
            [BLUE, TEAL, GREEN, YELLOW, RED], n
        )
        malla = VGroup()
        for k in range(n):
            # El k-ésimo gnomon (forma de L) tiene 2k + 1 casillas
            gnomon = VGroup(
                *[
                    Square(
                        lado,
                        fill_color=colores[k],
                        fill_opacity=0.8,
                        stroke_color=WHITE,
                        stroke_width=2,
                    ).move_to(lado * np.array([i, j, 0]))
                    for i in range(k + 1)
                    for j in range(k + 1)
                    if max(i, j) == k
                ]
            )
            malla.add(gnomon)
        malla.move_to(LEFT * 3)
        for gnomon in malla:
            self.play(
                LaggedStart(
                    *[GrowFromCenter(c) for c in gnomon],
                    lag_ratio=0.1,
                ),
                run_time=0.8,
            )
        # El símbolo llega al final: el estudiante lo anticipa
        suma = MathTex(
            *[
                f"{2 * k + 1}" + ("+" if k < n - 1 else "")
                for k in range(n)
            ],
            "=",
            f"{n}^2",
            font_size=60,
        ).move_to(RIGHT * 3)
        for k in range(n):
            suma[k].set_color(colores[k])
        self.play(Write(suma))
