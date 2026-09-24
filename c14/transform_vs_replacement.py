from manim import *


def si_no(valor):
    return "sí" if valor else "no"


class TransformVsReplacement(Scene):
    def construct(self):
        clases = [Transform, ReplacementTransform,
                  TransformFromCopy]
        for k, clase in enumerate(clases):
            x = -4.6 + 4.6 * k
            a = Circle(radius=0.7, color=BLUE, fill_opacity=0.6)
            b = Square(side_length=1.4, color=YELLOW,
                       fill_opacity=0.6)
            a.move_to([x, 1.3, 0])
            b.move_to([x, -1.0, 0])
            self.add(a)
            self.play(clase(a, b))
            # ¿Qué objetos quedaron en la escena?
            en_escena = self.mobjects
            estado = VGroup(
                Text(f"a en escena: {si_no(a in en_escena)}",
                     font_size=26),
                Text(f"b en escena: {si_no(b in en_escena)}",
                     font_size=26),
            ).arrange(DOWN, aligned_edge=LEFT).move_to([x, -2.6, 0])
            nombre = Text(clase.__name__, font="Monospace",
                          font_size=24)
            self.add(estado, nombre.move_to([x, 3.0, 0]))
