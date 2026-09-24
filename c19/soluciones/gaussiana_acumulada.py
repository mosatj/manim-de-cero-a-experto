from manim import *


class GaussianaAcumulada(Scene):
    def construct(self):
        ejes = Axes(x_range=[-3, 3, 1], y_range=[-1.2, 1.2, 0.5],
                    x_length=11, y_length=6, tips=False)
        ejes.add_coordinates(font_size=22)
        f = ejes.plot(lambda t: np.exp(-t**2), x_range=[-3, 3],
                      color=BLUE)
        # F(x) = ∫_0^x e^(−t²) dt con la regla del trapecio
        F = ejes.plot_antiderivative_graph(f, samples=200,
                                           color=GREEN)
        cota = np.sqrt(PI) / 2
        asintotas = VGroup(*[
            DashedLine(ejes.c2p(-3, s*cota), ejes.c2p(3, s*cota),
                       color=GRAY) for s in (1, -1)])
        nom = MathTex(
            r"F(x)=\int_0^x e^{-t^2}dt\ \to\ \frac{\sqrt\pi}{2}",
                      color=GREEN, font_size=38).to_corner(UL)
        self.add(ejes, asintotas, f, F, nom)
