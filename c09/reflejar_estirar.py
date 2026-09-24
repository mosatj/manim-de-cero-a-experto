from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class ReflejarEstirar(Scene):
    def construct(self):
        base = Text("F", font="serif", font_size=170, color=BLUE)
        casos = [
            ("original", base.copy()),
            ("flip()", base.copy().flip()),          # eje UP
            ("flip(RIGHT)", base.copy().flip(RIGHT)),
            ("stretch(2, 0)", base.copy().stretch(2, 0)),
            ("stretch(0.5, 1)", base.copy().stretch(0.5, 1)),
        ]
        grupo = VGroup()
        for nombre, letra in casos:
            rotulo = Text(nombre, font_size=26)
            rotulo.next_to(letra, DOWN, buff=0.4)
            grupo.add(VGroup(letra, rotulo))
        grupo.arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        self.add(grupo)
        # Los ejes de reflexión de flip() y de flip(RIGHT)
        for i, eje in [(1, UP), (2, RIGHT)]:
            c = grupo[i][0].get_center()
            self.add(DashedLine(c - 1.2 * eje, c + 1.2 * eje,
                                color=YELLOW))
