from manim import *


def fotos_de(animacion, n=7):
    """Fotografía el objeto en n instantes, sin reproducir nada."""
    fotos = VGroup()
    animacion.begin()
    for k in range(n):
        alpha = k / (n - 1)
        animacion.interpolate(alpha)
        foto = animacion.mobject.copy()
        opacidad = 0.15 + 0.85 * alpha
        foto.set_stroke(opacity=opacidad)
        foto[1].set_fill(opacity=opacidad)  # la esquina
        fotos.add(foto)
    animacion.finish()
    return fotos


class EstroboscopioRotaciones(Scene):
    def construct(self):
        def pieza(centro):
            cuadro = Square(1.4, color=BLUE)
            esquina = Dot(cuadro.get_corner(UR), color=YELLOW)
            return VGroup(cuadro, esquina).move_to(centro)

        a, b, c = pieza(LEFT * 4.5), pieza(ORIGIN), pieza(RIGHT * 3)
        giro_a = a.animate(rate_func=linear).rotate(PI).build()
        fotos = VGroup(
            fotos_de(giro_a),
            fotos_de(Rotate(b, PI, rate_func=linear)),
            fotos_de(Rotating(c, PI, about_point=4.5 * RIGHT)),
        )
        nombres = VGroup(Text(".animate.rotate"), Text("Rotate"),
                         Text("Rotating (about_point)"))
        for texto, x in zip(nombres, [-4.5, 0, 4.5]):
            texto.scale(0.5).move_to([x, -3, 0])
        self.add(fotos, nombres, Dot(RIGHT * 4.5, color=RED))
