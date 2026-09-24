from manim import *


class TextoBasico(Scene):
    def construct(self):
        # Tamaño, color, peso e inclinación: todo son parámetros
        saludo = Text("¡Hola, año nuevo!", font_size=72)
        grande = Text("Tamaño 36", font_size=36, color=BLUE)
        negrita = Text("Peso BOLD", weight=BOLD, color=YELLOW)
        cursiva = Text("Inclinación ITALIC", slant=ITALIC)
        sans = Text("Fuente Sans", font="Sans", color=GREEN)
        mono = Text("Fuente Monospace", font="Monospace")
        muestras = VGroup(grande, negrita, cursiva, sans, mono)
        muestras.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        VGroup(saludo, muestras).arrange(DOWN, buff=0.6)
        self.play(Write(saludo))
        self.play(LaggedStart(*[FadeIn(m) for m in muestras],
                              lag_ratio=0.3))
        self.wait()
