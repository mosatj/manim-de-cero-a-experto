from manim import *


class PrimerZoom(MovingCameraScene):
    def construct(self):
        plano = NumberPlane()
        # Un texto diminuto: ilegible en el plano general
        secreto = Text("¡Aquí estoy!", color=YELLOW).scale(0.2)
        secreto.move_to([4, 2.5, 0])
        punto = Dot([4, 2.3, 0], radius=0.03, color=RED)
        self.add(plano, secreto, punto)

        marco = self.camera.frame  # el rectángulo que la cámara ve
        # Acercar: el marco se reduce al 15 % y se centra en el texto
        self.play(marco.animate.scale(0.15).move_to(secreto),
                  run_time=2)
