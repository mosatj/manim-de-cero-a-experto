from manim import *


class RotarMarco(MovingCameraScene):
    def construct(self):
        marco = self.camera.frame
        flecha = Arrow(DOWN, 2 * UP, color=YELLOW)
        texto = Text("ARRIBA").next_to(flecha, UP)
        self.add(NumberPlane(), flecha, texto)
        # Girar el marco NO gira la imagen: solo agranda su caja
        self.play(marco.animate.rotate(PI / 6))
