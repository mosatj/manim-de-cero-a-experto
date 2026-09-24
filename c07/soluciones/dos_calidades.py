from manim import *


class Borrador(Scene):
    def construct(self):
        self.play(DrawBorderThenFill(
            RegularPolygon(n=6, color=TEAL,
                           fill_opacity=0.5)))
        self.wait()


if __name__ == "__main__":
    for calidad in ["low_quality", "high_quality"]:
        with tempconfig({"quality": calidad}):
            Borrador().render()
