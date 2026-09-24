# 1. Importar la biblioteca
from manim import *


# 2. Una clase que hereda de Scene
class NombreDeLaEscena(Scene):
    """Plantilla mínima de un script de Manim."""

    # 3. El método construct: aquí va la animación
    def construct(self):
        texto = Text("Hola, Manim")  # un objeto
        self.play(Write(texto))      # una animación
        self.wait()                  # una pausa de 1 s
