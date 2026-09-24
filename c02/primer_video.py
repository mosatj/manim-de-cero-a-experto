from manim import *


class PrimerVideo(Scene):
    def construct(self):
        texto = Text("¡Hola, Manim!")
        self.play(Write(texto))  # se escribe como a mano (1 s)
        self.wait(2)  # la imagen queda quieta 2 s
