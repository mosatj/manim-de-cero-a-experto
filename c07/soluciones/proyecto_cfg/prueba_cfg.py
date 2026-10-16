from manim import *


# Escena para comprobar el manim.cfg de esta carpeta:
#   manim prueba_cfg.py PruebaCfg       -> renders/images/..., 1280x720, fondo blanco
#   manim -qh prueba_cfg.py PruebaCfg   -> la misma imagen en 1920x1080
class PruebaCfg(Scene):
    def construct(self):
        # Con fondo blanco, el texto blanco por defecto no se vería
        titulo = Text("Fondo blanco desde manim.cfg", color=BLACK)
        marco = SurroundingRectangle(titulo, color=BLUE, buff=0.4)
        self.add(titulo, marco)
