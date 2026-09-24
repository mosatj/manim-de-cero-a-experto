from manim import *


class AgregarYQuitar(Scene):
    def construct(self):
        punto = Dot(LEFT * 3, radius=0.2, color=RED)
        estrella = Star(color=YELLOW, fill_opacity=0.6)
        rotulo = Text("add, play, wait, remove", font_size=32)
        rotulo.to_edge(DOWN)

        self.add(rotulo)            # aparece de golpe
        self.add(punto)
        self.wait(0.5)              # 0,5 s sin cambios
        self.remove(punto)          # desaparece de golpe
        self.play(FadeIn(estrella))  # aparece animada
        self.wait()
