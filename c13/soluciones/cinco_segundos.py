from manim import *


class CincoSegundos(Scene):
    def construct(self):
        circulo = Circle(radius=1.5, color=TEAL)
        nombre = Text("Círculo").next_to(circulo, DOWN)
        self.play(Create(circulo), run_time=2)     # 0 s -> 2 s
        self.wait(1)                               # 2 s -> 3 s
        self.play(FadeIn(nombre), run_time=1.5)    # 3 s -> 4.5 s
        self.wait(0.5)                             # 4.5 s -> 5 s
        reloj = Text(f"t = {self.time:.1f} s", font_size=36)
        self.add(reloj.to_corner(UR))
