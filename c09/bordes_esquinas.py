from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class BordesEsquinas(Scene):
    def construct(self):
        # Rectángulo discontinuo: el margen por defecto (0.5)
        ancho = config.frame_width - 1
        alto = config.frame_height - 1
        margen = DashedVMobject(
            Rectangle(width=ancho, height=alto, color=GRAY),
            num_dashes=80)
        self.add(margen)
        for esquina, nombre in [(UL, "UL"), (UR, "UR"),
                                (DL, "DL"), (DR, "DR")]:
            caja = Square(0.9, color=YELLOW, fill_opacity=0.5)
            caja.to_corner(esquina)
            t = Text(f"to_corner({nombre})", font_size=26,
                     color=YELLOW)
            # El rótulo, hacia dentro del marco (en horizontal)
            t.next_to(caja, -esquina[0] * RIGHT)
            self.add(caja, t)
        for borde, nombre in [(UP, "UP"), (DOWN, "DOWN"),
                              (LEFT, "LEFT"), (RIGHT, "RIGHT")]:
            circulo = Circle(0.45, color=BLUE, fill_opacity=0.5)
            circulo.to_edge(borde)
            t = Text(f"to_edge({nombre})", font_size=26,
                     color=BLUE)
            t.next_to(circulo, -borde)
            self.add(circulo, t)
        cero = Square(0.5, color=RED, fill_opacity=1)
        cero.to_edge(DOWN, buff=0).shift(3.2 * LEFT)
        self.add(cero, Text("to_edge(DOWN, buff=0)", font_size=22,
                            color=RED).next_to(cero, RIGHT))
