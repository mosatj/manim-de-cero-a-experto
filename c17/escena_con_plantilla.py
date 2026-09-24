from manim import *
from mimanim import Medidor, PlantillaScene


class Resultados(PlantillaScene):
    def construct(self):
        self.titular("Resultados del cuestionario")
        medidor = Medidor(color=self.COLOR_ACENTO).shift(UP * 0.3)
        nota = Text("aprobados", color=GRAY).next_to(medidor, DOWN)
        self.play(FadeIn(medidor), FadeIn(nota))
        self.play(medidor.animate(run_time=2).fijar_valor(72))
        self.wait()
