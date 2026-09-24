from manim import *


class Copias(Scene):
    def construct(self):
        original = Star(color=YELLOW, fill_opacity=0.6).scale(0.6)
        alias = original          # NO es una copia: mismo objeto
        alias.shift(3 * LEFT)     # mueve también «original»
        # copy() crea un objeto nuevo, con copias de sus submobjects
        fila = VGroup(original)
        for k in range(1, 5):
            nueva = fila[-1].copy()
            nueva.shift(1.5 * RIGHT).rotate(PI / 10)
            nueva.set_color(interpolate_color(YELLOW, RED, k / 4))
            fila.add(nueva)
        self.play(LaggedStart(*[GrowFromCenter(e) for e in fila],
                              lag_ratio=0.3))
        self.wait()
