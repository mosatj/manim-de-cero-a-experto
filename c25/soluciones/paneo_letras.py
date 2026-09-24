from manim import *


class PaneoLetras(MovingCameraScene):
    def construct(self):
        marco = self.camera.frame
        letras = VGroup(*[Text(c, font_size=144) for c in "MANIM"])
        letras.arrange(RIGHT, buff=4)            # unas 30 unidades
        self.add(letras)
        self.play(marco.animate.set(width=5).move_to(letras[0]))
        for letra in letras[1:]:
            self.play(marco.animate.move_to(letra), run_time=1.2)
        self.play(marco.animate.set(width=letras.width + 1)
                  .move_to(letras))
