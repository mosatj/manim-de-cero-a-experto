from manim import *


def circunferencia(ejes):
    return ejes.plot_parametric_curve(
        lambda t: np.array([np.cos(t), np.sin(t), 0]),
        t_range=[0, TAU], color=YELLOW)


class EscalaAntes(Scene):
    def construct(self):
        # Ejes estirados para «llenar»: la unidad no mide igual
        ejes = Axes(x_range=[-1.5, 1.5, 0.5], y_range=[-1.5, 1.5, 0.5],
                    x_length=12, y_length=6.5)
        self.play(Create(ejes), Create(circunferencia(ejes)))


class EscalaDespues(Scene):
    def construct(self):
        # Misma longitud por unidad en ambos ejes: forma verdadera
        ejes = Axes(x_range=[-1.5, 1.5, 0.5], y_range=[-1.5, 1.5, 0.5],
                    x_length=6.5, y_length=6.5)
        self.play(Create(ejes), Create(circunferencia(ejes)))
