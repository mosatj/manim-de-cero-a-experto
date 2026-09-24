from manim import *


class AnimacionComoActualizador(Scene):
    def construct(self):
        titulo = Text("Movimiento reactivo").to_edge(UP)
        estrella = Star(color=YELLOW).shift(4 * LEFT)
        halo = Circle(radius=1.4, color=BLUE).shift(RIGHT * 4)

        # Write se «desprende» de play: corre sola durante 1.5 s
        turn_animation_into_updater(Write(titulo, run_time=1.5))
        # cycle_animation: el halo late sin parar
        cycle_animation(Indicate(halo, scale_factor=1.3))
        self.add(titulo, halo)

        # Mientras tanto, play mueve la estrella
        self.play(estrella.animate.shift(RIGHT * 8), run_time=2)
        self.wait(0.5)
