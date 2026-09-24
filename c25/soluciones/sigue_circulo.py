from manim import *


class SigueCirculo(MovingCameraScene):
    def construct(self):
        marco = self.camera.frame
        orbita = Circle(radius=3, color=GREY)
        planeta = Dot(orbita.point_at_angle(0), color=BLUE)
        estrella = Dot(color=YELLOW, radius=0.2)
        self.add(orbita, estrella, planeta)
        self.play(marco.animate.set(width=4).move_to(planeta))
        self.add(marco)                     # imprescindible
        marco.add_updater(lambda m: m.move_to(planeta))
        self.play(MoveAlongPath(planeta, orbita), run_time=4,
                  rate_func=linear)
        marco.clear_updaters()
        self.play(self.camera.auto_zoom([orbita], margin=2))
