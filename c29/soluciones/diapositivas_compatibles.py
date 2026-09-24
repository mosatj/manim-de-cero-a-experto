from manim import *

try:
    from manim_slides import Slide
except ImportError:
    # Sin Manim Slides, cada diapositiva será una sección
    class Slide(Scene):
        def next_slide(self, loop=False, notes="", **kwargs):
            self.next_section()


class DiapositivasCompatibles(Slide):
    def construct(self):
        titulo = Text("Teorema de Pitágoras", font_size=48)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.next_slide(notes="Presentar el problema.")
        tri = Polygon([-2, -1.5, 0], [2, -1.5, 0], [-2, 1.5, 0],
                      color=BLUE)
        self.play(Create(tri))
        self.next_slide(loop=True)
        self.play(Indicate(tri))  # se repite hasta que avances
        self.next_slide()
        formula = MathTex(r"a^2+b^2=c^2").next_to(tri, RIGHT)
        self.play(Write(formula))
