from manim import *


class Pasos(Scene):
    def construct(self):
        titulo = Title("Cómo renderizar")
        pasos = BulletedList("Escribe la escena",
                             "Renderiza con -ql",
                             "Revisa y corrige",
                             font_size=44)
        pasos.next_to(titulo, DOWN, buff=0.8)
        self.add(titulo, pasos)
        for k in range(3):
            self.play(pasos.animate.fade_all_but(k, opacity=0.25))
