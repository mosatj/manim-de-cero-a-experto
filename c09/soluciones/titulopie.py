from manim import *


class TituloPie(Scene):
    def construct(self):
        titulo = Text("Semejanza de triángulos", font_size=48)
        titulo.to_edge(UP)
        pie = Text("Geometría · lección 3", font_size=24)
        pie.set_color(GRAY).to_corner(DL)
        self.add(titulo, pie)
