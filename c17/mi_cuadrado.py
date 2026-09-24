from manim import *


class MiCuadrado(Square):
    @override_animation(FadeIn)
    def _entrar(self, **kwargs):
        # Para esta clase, FadeIn dibuja
        return Create(self, **kwargs)


class EscenaMiCuadrado(Scene):
    def construct(self):
        c = MiCuadrado(color=BLUE)
        self.play(FadeIn(c))  # ¡es Create!
