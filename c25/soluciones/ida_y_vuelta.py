from manim import *


class IdaYVuelta(MovingCameraScene):
    def construct(self):
        marco = self.camera.frame
        puntos = VGroup(*[Dot([x, 0, 0]) for x in range(-6, 7, 2)])
        self.add(puntos)
        marco.save_state()                   # 1) guardar
        for punto in [puntos[1], puntos[5]]:
            self.play(marco.animate.scale(0.3).move_to(punto))
            self.play(punto.animate.set_color(RED))
            self.play(Restore(marco))        # 2) volver
