from manim import *


class EscenaDelLibroBase(Scene):
    """Base común: prepara el fondo de todas las escenas."""

    def setup(self):
        self.plano = NumberPlane(background_line_style={
            "stroke_opacity": 0.25})
        self.firma = Text("Manim", font_size=24)
        self.firma.to_corner(DR).set_opacity(0.6)
        self.add(self.plano, self.firma)


class ConFondoComun(EscenaDelLibroBase):
    # Solo escribe construct: setup() se hereda
    def construct(self):
        vector = Arrow(ORIGIN, [3, 2, 0], buff=0,
                       color=YELLOW)
        self.play(GrowArrow(vector))
        self.wait()
