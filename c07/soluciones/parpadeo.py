from manim import *


class Parpadeo(Scene):
    def construct(self):
        estrella = Star(color=YELLOW, fill_opacity=0.8)
        for _ in range(3):
            self.add(estrella)
            self.wait(0.3)
            self.remove(estrella)
            self.wait(0.3)
        self.add(estrella)   # termina visible
        self.wait()
