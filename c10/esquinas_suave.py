from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class EsquinasSuave(Scene):
    def construct(self):
        # Los mismos seis puntos, unidos de dos maneras
        xs = np.linspace(-2.5, 2.5, 6)
        puntos = [[x, 1.2 * (-1) ** i, 0]
                  for i, x in enumerate(xs)]
        quebrada = VMobject(color=BLUE)
        quebrada.set_points_as_corners(puntos)
        suave = VMobject(color=YELLOW)
        suave.set_points_smoothly(puntos)
        izq = VGroup(quebrada, *[Dot(p) for p in puntos])
        der = VGroup(suave, *[Dot(p) for p in puntos])
        VGroup(izq, der).arrange(DOWN, buff=1.4)
        self.add(izq, der)
        self.add(Text("set_points_as_corners(puntos)",
                      font_size=26, color=BLUE)
                 .next_to(izq, UP, buff=0.2))
        self.add(Text("set_points_smoothly(puntos)",
                      font_size=26, color=YELLOW)
                 .next_to(der, UP, buff=0.2))
