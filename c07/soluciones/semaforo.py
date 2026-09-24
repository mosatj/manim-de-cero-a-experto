from manim import *


class Semaforo(Scene):
    def construct(self):
        caja = RoundedRectangle(width=2, height=5,
                                corner_radius=0.3, color=GRAY)
        luces = VGroup(*[Circle(radius=0.6, color=GRAY,
                                fill_opacity=0.2)
                         for _ in range(3)])
        luces.arrange(DOWN, buff=0.3)
        self.play(Create(caja), FadeIn(luces))
        for luz, color in zip(luces, [RED, YELLOW, GREEN]):
            self.play(luz.animate.set_fill(color, opacity=1))
            self.wait(0.5)
            self.play(luz.animate.set_fill(GRAY, opacity=0.2))
        # Estado final: verde encendido
        self.play(luces[2].animate.set_fill(GREEN, opacity=1))
        self.wait()
