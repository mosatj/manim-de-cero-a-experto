from manim import *


def suma_parcial(x, N):
    """S_N(x) = (4/pi) * suma de sen(nx)/n para n impar <= N."""
    impares = range(1, N + 1, 2)
    return 4 / PI * sum(np.sin(n * x) / n for n in impares)


class FourierCuadrada(Scene):
    def construct(self):
        ejes = Axes(x_range=[-PI, PI, PI / 2],
                    y_range=[-1.5, 1.5, 0.5],
                    x_length=11, y_length=5.2, tips=False)
        ejes.to_edge(DOWN, buff=0.6)
        # La onda cuadrada: -1 en (-pi, 0) y +1 en (0, pi)
        onda = VGroup(
            ejes.plot(lambda x: -1, x_range=[-PI, 0], color=GRAY),
            ejes.plot(lambda x: 1, x_range=[0, PI], color=GRAY))
        formula = MathTex(r"S_N(x) = \frac4\pi",
                          r"\sum_{n\ \mathrm{impar}}^{N}",
                          r"\frac{\sin nx}{n}", font_size=40)
        self.add(ejes, onda, formula.to_corner(UL))
        rotulo = lambda N: MathTex(f"N = {N}", color=YELLOW
                                   ).to_corner(UR)
        curva = ejes.plot(lambda x: suma_parcial(x, 1),
                          color=YELLOW)
        texto = rotulo(1)
        self.play(Create(curva), Write(texto))
        for N in (3, 9, 21):
            nueva = ejes.plot(lambda x, N=N: suma_parcial(x, N),
                              color=YELLOW)
            self.play(Transform(curva, nueva),
                      Transform(texto, rotulo(N)))
        # El sobrepaso de Gibbs no desaparece: tiende a 1,179
        tope = ejes.get_horizontal_line(ejes.c2p(PI, 1.179),
                                        color=RED)
        valor = MathTex(r"1{,}179", color=RED, font_size=30)
        valor.next_to(ejes.c2p(PI / 2, 1.179), UP)
        self.play(Create(tope), Write(valor))
