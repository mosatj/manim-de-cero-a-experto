from manim import *


class LupaEsquina(ZoomedScene):
    def __init__(self, **kwargs):
        super().__init__(zoom_factor=0.3,
                         zoomed_display_corner=DL,
                         zoomed_display_width=4,
                         zoomed_display_height=2.5, **kwargs)

    def construct(self):
        serie = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2}",
                        r"=\frac{\pi^2}{6}", font_size=60)
        serie.to_edge(UP)
        self.add(serie)
        lente = self.zoomed_camera.frame
        lente.move_to(serie[0][2:5])          # el índice «n=1»
        lente.set_color(RED)
        self.zoomed_display.display_frame.set_color(RED)
        self.activate_zooming(animate=True)
