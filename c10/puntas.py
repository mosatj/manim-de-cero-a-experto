from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class Puntas(Scene):
    def construct(self):
        puntas = [StealthTip, ArrowTriangleTip,
                  ArrowTriangleFilledTip, ArrowCircleTip,
                  ArrowCircleFilledTip, ArrowSquareTip,
                  ArrowSquareFilledTip]
        filas = VGroup()
        for punta in puntas:
            linea = Line(ORIGIN, 3 * RIGHT, color=YELLOW)
            linea.add_tip(tip_shape=punta)
            nombre = Text(punta.__name__, font_size=26)
            fila = VGroup(nombre, linea).arrange(RIGHT, buff=0.5)
            filas.add(fila)
        filas.arrange(DOWN, aligned_edge=RIGHT, buff=0.3)
        doble = Line(ORIGIN, 3 * RIGHT, color=BLUE)
        doble.add_tip(tip_shape=StealthTip)
        doble.add_tip(tip_shape=StealthTip, at_start=True)
        texto = Text("add_tip(..., at_start=True)", font_size=24)
        grupo = VGroup(doble, texto).arrange(DOWN)
        todo = VGroup(filas, grupo).arrange(RIGHT, buff=1)
        todo.scale_to_fit_width(config.frame_width - 1)
        self.add(filas, grupo)
