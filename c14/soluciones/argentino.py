from manim import *


class Argentino(Scene):
    def construct(self):
        origen = Text("ARGENTINO", font_size=90)
        destino = Text("IGNORANTE", font_size=90)
        self.play(Write(origen))
        self.wait()
        # Cada letra busca otra de la misma forma en el destino
        self.play(TransformMatchingShapes(origen, destino,
                                          path_arc=PI / 2),
                  run_time=2.5)
        self.wait()
