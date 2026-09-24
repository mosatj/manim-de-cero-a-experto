from manim import *


class AnimateEquivalente(Scene):
    def construct(self):
        a = Square(color=BLUE).shift(LEFT * 3 + UP)
        b = Square(color=RED).shift(RIGHT * 1 + UP)
        self.add(a, b)

        # Forma corta: el constructor .animate
        anim_a = a.animate.shift(DOWN * 2).set_fill(BLUE, 0.6)

        # Forma larga: objetivo + MoveToTarget
        b.generate_target()               # b.target = copia
        b.target.shift(DOWN * 2).set_fill(RED, 0.6)
        anim_b = MoveToTarget(b)

        self.play(anim_a, anim_b, run_time=2)
        self.wait()
