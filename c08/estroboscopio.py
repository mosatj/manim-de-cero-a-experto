from manim import *


def fotos(animacion, n=5):
    """Copias del mobject en n instantes de la animación."""
    animacion.begin()
    copias = VGroup()
    for alpha in np.linspace(0, 1, n):
        animacion.interpolate(alpha)
        copias.add(animacion.mobject.copy())
    animacion.finish()
    return copias


class Estroboscopio(Scene):
    def construct(self):
        izq = Square(side_length=2.5, color=BLUE)
        der = Square(side_length=2.5, color=RED)
        izq.shift(LEFT * 3.5)
        der.shift(RIGHT * 3.5)
        # Mismo estado final, distinto camino
        fotos_a = fotos(izq.animate.rotate(PI / 2).build())
        fotos_b = fotos(Rotate(der, angle=PI / 2))
        for grupo in (fotos_a, fotos_b):
            for k, copia in enumerate(grupo):
                copia.set_stroke(opacity=0.25 + 0.75 * k / 4)
        rotulos = VGroup(
            Text(".animate.rotate(PI/2)", font_size=30),
            Text("Rotate(angle=PI/2)", font_size=30))
        rotulos[0].move_to([-3.5, -2.8, 0])
        rotulos[1].move_to([3.5, -2.8, 0])
        self.add(fotos_a, fotos_b, rotulos)
