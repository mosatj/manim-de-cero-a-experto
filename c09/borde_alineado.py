from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class BordeAlineado(Scene):
    def construct(self):
        # Izquierda: next_to con distintos bordes alineados
        filas = VGroup()
        for borde, nombre in [(ORIGIN, "ORIGIN"), (UP, "UP"),
                              (DOWN, "DOWN")]:
            grande = Square(1.5, color=BLUE, fill_opacity=0.3)
            chico = Square(0.6, color=YELLOW, fill_opacity=0.6)
            chico.next_to(grande, RIGHT, buff=0.1,
                          aligned_edge=borde)
            rotulo = Text(f"aligned_edge={nombre}", font_size=26)
            rotulo.next_to(grande, LEFT, buff=0.3)
            filas.add(VGroup(rotulo, grande, chico))
        filas.arrange(DOWN, buff=0.45, aligned_edge=RIGHT)
        filas.to_edge(LEFT, buff=0.5)
        # Derecha: align_to iguala una sola coordenada
        suelo = Line(LEFT, RIGHT, color=GRAY).set_length(5.2)
        suelo.move_to([3.6, -1.2, 0])
        techo = suelo.copy().shift(3.4 * UP)
        formas = VGroup(Circle(0.5, color=RED),
                        Triangle(color=GREEN).scale(0.8),
                        Square(1.3, color=BLUE))
        formas.arrange(RIGHT, buff=0.5).move_to([3.6, 0.5, 0])
        abajo = formas.copy()
        for f in abajo:
            f.align_to(suelo, DOWN)   # «apoyadas» en el suelo
        arriba = formas.copy()
        for f in arriba:
            f.align_to(techo, UP)     # «colgadas» del techo
        self.add(filas, suelo, techo, abajo, arriba)
        self.add(Text("align_to(suelo, DOWN)", font_size=24)
                 .next_to(suelo, DOWN))
        self.add(Text("align_to(techo, UP)", font_size=24)
                 .next_to(techo, UP))
