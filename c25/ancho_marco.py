from manim import *


class AnchoDelMarco(MovingCameraScene):
    def construct(self):
        marco = self.camera.frame
        tarjetas = VGroup(*[
            VGroup(Square(side_length=3, color=c),
                   MathTex(t, font_size=72))
            for c, t in [(BLUE, r"1"), (GREEN, r"2"), (RED, r"3")]
        ]).arrange(RIGHT, buff=5)  # más ancho que la pantalla
        self.add(tarjetas)

        # 1) Encuadrar la primera tarjeta con un ancho exacto
        self.play(marco.animate.set(width=6).move_to(tarjetas[0]))
        # 2) Paneo: el marco conserva su ancho y solo se traslada
        for tarjeta in tarjetas[1:]:
            self.play(marco.animate.move_to(tarjeta), run_time=1.5)
        # 3) Plano general: que quepa todo con un margen
        self.play(marco.animate.set(width=tarjetas.width + 2)
                  .move_to(tarjetas))
