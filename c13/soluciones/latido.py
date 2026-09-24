from manim import *


class Latido(Scene):
    def construct(self):
        corazon = MathTex(r"\heartsuit", font_size=260, color=RED)
        self.add(corazon)
        for _ in range(3):
            # Crece, se sostiene un instante y vuelve
            self.play(corazon.animate.scale(1.3),
                      rate_func=there_and_back_with_pause,
                      run_time=0.8)
            self.wait(0.3)
