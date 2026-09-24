from manim import *
from congelar import congelar


class TrampaRotacion(Scene):
    def construct(self):
        def cuadrado():
            c = Square(side_length=1.3, color=BLUE,
                       fill_opacity=0.6)
            # Un punto rojo marca un vértice
            c.add(Dot(c.get_corner(UR), color=RED))
            return c

        casos = [
            (".animate.rotate(PI)",
             lambda c: c.animate.rotate(PI).build()),
            ("Rotate(c, PI)", lambda c: Rotate(c, angle=PI)),
            (".animate(path_arc=PI).rotate(PI)",
             lambda c: c.animate(path_arc=PI).rotate(PI).build()),
        ]
        for j, (nombre, crear) in enumerate(casos):
            y = 2.4 - 2.5 * j
            rotulo = Text(nombre, font="Monospace", font_size=18)
            self.add(rotulo.move_to([-4.6, y, 0]))
            for i, alfa in enumerate([0, 0.25, 0.5, 0.75, 1]):
                c = cuadrado().move_to([-1.2 + 1.75 * i, y, 0])
                congelar(self, crear(c), alfa)
                if j == 0:
                    etiqueta = MathTex(rf"\alpha={alfa}",
                                       font_size=28)
                    etiqueta.move_to([-1.2 + 1.75 * i, 3.6, 0])
                    self.add(etiqueta)
