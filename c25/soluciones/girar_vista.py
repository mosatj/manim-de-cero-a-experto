from manim import *


class GirarVista(MovingCameraScene):
    def construct(self):
        marco = self.camera.frame
        plano = NumberPlane()
        flecha = Arrow(DOWN, 2 * UP, color=YELLOW)
        texto = Text("ARRIBA").next_to(flecha, UP)
        self.add(plano, flecha, texto)
        # Simular que la cámara gira: girar el mundo al revés
        mundo = Group(*self.mobjects)
        self.play(Rotate(mundo, angle=-PI / 6,
                         about_point=marco.get_center()))
