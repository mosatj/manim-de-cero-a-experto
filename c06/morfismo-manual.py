from manim import *

N = 200                                   # puntos de cada contorno
t = np.linspace(0, 1, N)
angulo = 2 * np.pi * t


def cuadrado(t):
    """Contorno del cuadrado de lado 2, parametrizado por ángulo."""
    a = 2 * np.pi * t
    escala = 1 / np.maximum(np.abs(np.cos(a)), np.abs(np.sin(a)))
    return np.column_stack([escala * np.cos(a), escala * np.sin(a),
                            np.zeros_like(a)])


circulo = np.column_stack([np.cos(angulo), np.sin(angulo),
                           np.zeros(N)])


class MorfismoManual(Scene):
    def construct(self):
        formas = VGroup()
        for alfa in np.linspace(0, 1, 5):
            puntos = (1 - alfa) * cuadrado(t) + alfa * circulo
            forma = VMobject().set_points_as_corners(puntos)
            color = interpolate_color(BLUE, YELLOW, alfa)
            forma.set_stroke(color, width=4)
            formas.add(forma)
        formas.arrange(RIGHT, buff=0.5)
        rotulos = VGroup(*[
            MathTex(rf"\alpha={a:g}", font_size=34).next_to(f, DOWN)
            for a, f in zip(np.linspace(0, 1, 5), formas)])
        self.play(LaggedStart(*[Create(f) for f in formas],
                              lag_ratio=0.3), Write(rotulos))
