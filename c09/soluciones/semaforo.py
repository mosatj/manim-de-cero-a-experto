from manim import *


class Semaforo(Scene):
    def construct(self):
        luces = VGroup(*[Circle(0.6, color=c, fill_opacity=0.9)
                         for c in (RED, YELLOW, GREEN)])
        luces.arrange(DOWN, buff=0.3)
        caja = SurroundingRectangle(luces, buff=0.3,
                                    corner_radius=0.3,
                                    color=GRAY)
        poste = Rectangle(width=0.4, height=2.5, color=GRAY,
                          fill_opacity=1)
        poste.next_to(caja, DOWN, buff=0)
        semaforo = VGroup(poste, caja, luces).move_to(ORIGIN)
        self.add(semaforo)
