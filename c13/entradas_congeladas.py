from manim import *
from congelar import congelar


def cuadro():
    return Square(side_length=1.4, color=TEAL, fill_opacity=0.6)


def palabra():
    return Text("Hola", font_size=60)


def flecha():
    return Arrow(1.2 * LEFT, 1.2 * RIGHT, color=YELLOW, buff=0)


class EntradasCongeladas(Scene):
    def construct(self):
        casos = [
            ("Create", cuadro, Create),
            ("DrawBorderThenFill", cuadro, DrawBorderThenFill),
            ("Write", palabra, Write),
            ("FadeIn(shift=UP)", cuadro,
             lambda m: FadeIn(m, shift=UP)),
            ("FadeIn(scale=0.3)", cuadro,
             lambda m: FadeIn(m, scale=0.3)),
            ("GrowFromCenter", cuadro, GrowFromCenter),
            ("GrowFromEdge(m, DOWN)", cuadro,
             lambda m: GrowFromEdge(m, DOWN)),
            ("GrowArrow", flecha, GrowArrow),
            ("SpinInFromNothing", cuadro, SpinInFromNothing),
        ]
        for i, (nombre, crear_fig, crear_anim) in enumerate(casos):
            fila, columna = divmod(i, 3)
            centro = np.array([-4.6 + 4.6 * columna,
                               2.5 - 2.6 * fila, 0])
            # Primero se coloca la figura; luego, la animación
            figura = crear_fig().move_to(centro)
            guia = DashedVMobject(
                SurroundingRectangle(figura, buff=0.05),
                num_dashes=30).set_stroke(GRAY, 1.5)
            rotulo = Text(nombre, font="Monospace", font_size=20)
            rotulo.next_to(guia, DOWN, buff=0.12)
            self.add(guia, rotulo)
            congelar(self, crear_anim(figura), 0.5)
