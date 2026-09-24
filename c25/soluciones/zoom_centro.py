from manim import *


class ZoomCentro(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#1E1E1E"
        plano = NumberPlane()
        circulo = Circle(radius=0.5, color=YELLOW)
        self.add(plano, circulo)
        # scale(0.5): el marco mide la mitad, todo se ve el doble
        self.play(self.camera.frame.animate.scale(0.5), run_time=2)
