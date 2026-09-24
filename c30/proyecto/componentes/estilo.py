"""Estilo común: paleta, tamaños de letra y la escena base."""
from manim import *

TINTA = ManimColor("#E9F2F7")
ACERO = ManimColor("#4F7C99")
CIAN = ManimColor("#6FA3C0")
GRANATE = ManimColor("#B04A5A")
TAM_TITULO = 40
TAM_TEXTO = 30


class LeccionScene(Scene):
    """Escena base: encabezado con el título y pie con el curso."""

    titulo = "Lección sin título"   # cada escena hija lo cambia
    curso = "Matemática visual"

    def setup(self):
        encabezado = Text(self.titulo, font_size=TAM_TITULO,
                          color=TINTA).to_edge(UP, buff=0.4)
        filete = Line(LEFT, RIGHT, color=ACERO, stroke_width=2)
        filete.set_width(config.frame_width - 1)
        filete.next_to(encabezado, DOWN, buff=0.2)
        pie = Text(self.curso, font_size=20, color=ACERO)
        self.add(encabezado, filete, pie.to_corner(DR, buff=0.3))

    def construct(self):
        # Vista previa de la plantilla: manim estilo.py LeccionScene
        self.add(Text("contenido", font_size=TAM_TEXTO, color=CIAN))
