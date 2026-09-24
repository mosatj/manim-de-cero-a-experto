from manim import *


class TrackerComplejo(Scene):
    def construct(self):
        plano = ComplexPlane(x_range=[-4, 4], y_range=[-3, 3])
        plano.add_coordinates()
        z = ComplexValueTracker(2 + 1j)

        vector = always_redraw(lambda: Arrow(
            ORIGIN, plano.n2p(z.get_value()), buff=0, color=YELLOW))
        rotulo = always_redraw(lambda: MathTex(
            "z", color=YELLOW).next_to(vector.get_end(), UR))
        rastro = VGroup()  # copias fijas de cada posición

        self.add(plano, vector, rotulo)
        for _ in range(3):
            rastro.add(vector.copy().clear_updaters().fade(0.7))
            self.add(rastro)
            # multiplicar por i = girar 90° en el plano complejo
            self.play(z.animate.set_value(z.get_value() * 1j))
