from manim import *


class AnticipacionArco(Scene):
    def construct(self):
        suelo = Line(6 * LEFT, 6 * RIGHT, color=GREY_D).shift(2 * DOWN)
        bola = Circle(radius=0.4, color=ORANGE, fill_opacity=1)
        bola.next_to(suelo, UP, buff=0).shift(4 * LEFT)
        salida = bola.get_center()
        llegada = salida + 8 * RIGHT
        # Guía estática: el mismo arco que recorrerá con path_arc
        guia = DashedVMobject(ArcBetweenPoints(salida, llegada,
                                               angle=-PI / 1.5))
        guia.set_stroke(GREY_B, width=2)
        self.add(suelo, guia, bola)
        # Anticipación: se agacha (squash) antes de saltar
        self.play(bola.animate.stretch(0.7, 1, about_edge=DOWN)
                  .stretch(1.2, 0), run_time=0.4)
        agachada = bola.copy().set_opacity(0.3)  # pose clave que queda
        self.add(agachada)
        self.play(bola.animate.stretch(1 / 0.7, 1, about_edge=DOWN)
                  .stretch(1 / 1.2, 0), run_time=0.15)
        # Arco: el salto sigue una curva, no una línea recta
        self.play(bola.animate(path_arc=-PI / 1.5).shift(8 * RIGHT),
                  run_time=1.2, rate_func=smooth)
        # Continuidad (follow through): al caer se aplasta un poco
        self.play(bola.animate.stretch(0.8, 1, about_edge=DOWN),
                  run_time=0.15)
        self.play(bola.animate.stretch(1 / 0.8, 1, about_edge=DOWN),
                  run_time=0.25)
