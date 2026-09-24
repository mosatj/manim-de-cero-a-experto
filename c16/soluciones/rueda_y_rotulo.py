from manim import *


class RuedaYRotulo(Scene):
    def construct(self):
        rueda = VGroup(Circle(radius=1.5, color=BLUE), *[
            Line(ORIGIN, 1.5 * rotate_vector(RIGHT, k * PI / 3))
            for k in range(6)]).shift(LEFT * 4)
        always_rotate(rueda, rate=-PI)     # media vuelta por s
        v = 1.5 * PI                       # v = r·ω: sin deslizar
        rueda.add_updater(lambda m, dt: m.shift(v * dt * RIGHT))
        # El rótulo la sigue sin girar: no forma parte de ella
        rotulo = Text("rueda", font_size=30)
        rotulo.add_updater(lambda m: m.next_to(rueda, UP))
        self.add(rueda, rotulo)
        self.wait(1.6)
