"""Escena base con el estilo común del proyecto (capítulo 17)."""
from manim import *

__all__ = ["PlantillaScene"]


class PlantillaScene(Scene):
    """Fondo, tipografía y utilidades comunes a las escenas."""

    COLOR_FONDO = "#0B2A3C"
    COLOR_ACENTO = "#2A8FBD"
    FIRMA = "Manim 0.21 · de cero a experto"

    def setup(self):
        super().setup()
        self.camera.background_color = self.COLOR_FONDO
        Text.set_default(font_size=34)    # estilo de la casa
        self.add(self.marca_de_agua())

    def tear_down(self):
        Text.set_default()                # restaura la clase
        super().tear_down()

    def marca_de_agua(self):
        firma = Text(self.FIRMA, font_size=24, color=GRAY_B)
        return firma.set_opacity(0.6).to_corner(DR, buff=0.3)

    def titular(self, texto):
        """Título arriba con filete de acento, animado al entrar."""
        titulo = Text(texto, font_size=46).to_edge(UP, buff=0.5)
        filete = Line(LEFT, RIGHT, color=self.COLOR_ACENTO)
        filete.match_width(titulo).next_to(titulo, DOWN, 0.15)
        self.play(FadeIn(titulo, shift=0.3 * UP), Create(filete))
        return VGroup(titulo, filete)

    def construct(self):
        # Demostración de la plantilla (las subclases la sustituyen)
        self.titular("Plantilla del proyecto")
        self.add(Text("setup() puso el fondo y la firma"))
