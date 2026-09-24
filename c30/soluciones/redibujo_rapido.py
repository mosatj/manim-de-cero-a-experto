from manim import *


class RedibujoRapido(Scene):
    def construct(self):
        t = ValueTracker(0)
        plano = NumberPlane()
        girado = [0.0]          # ángulo ya aplicado al plano

        def girar(m):           # gira lo que falta, sin crear nada
            m.rotate(t.get_value() - girado[0])
            girado[0] = t.get_value()

        plano.add_updater(girar)
        self.add(plano)
        self.play(t.animate.set_value(PI / 6), run_time=6)
