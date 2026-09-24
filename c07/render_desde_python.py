from manim import *


class Saludo(Scene):
    def construct(self):
        self.play(Write(Text("Renderizado desde Python")))
        self.wait()


if __name__ == "__main__":
    # Equivale a: manim -pql render_desde_python.py Saludo
    opciones = {"quality": "low_quality", "preview": True}
    with tempconfig(opciones):
        escena = Saludo()
        escena.render()
