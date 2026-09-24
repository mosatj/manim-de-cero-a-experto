from manim import *


class BinomioTex(Scene):
    def construct(self):
        paso1 = MathTex(r"(a+b)^2", font_size=80)
        paso2 = MathTex(r"(a+b)(a+b)", font_size=80)
        paso3 = MathTex(r"a^2+2ab+b^2", font_size=80)
        self.play(Write(paso1))
        # Ninguna parte tiene el mismo código TeX que otra, así que
        # TransformMatchingTex fundiría todo. Emparejamos por forma:
        self.play(TransformMatchingShapes(paso1, paso2))
        self.wait()
        self.play(TransformMatchingShapes(paso2, paso3))
        self.play(Circumscribe(paso3))
