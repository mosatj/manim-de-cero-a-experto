from manim import *


class ConResumen(Scene):
    def construct(self):
        self.play(Create(Circle()), run_time=1.5)
        self.play(FadeIn(Square()))
        self.wait(0.5)

    def tear_down(self):
        # Se ejecuta tras el último fotograma
        print("Mobjects en escena:", self.mobjects)
        print("Tiempo total:", round(self.time, 3), "s")
        print("Llamadas a play:", self.renderer.num_plays)


if __name__ == "__main__":
    ajustes = {"dry_run": True, "verbosity": "WARNING",
               "progress_bar": "none"}
    with tempconfig(ajustes):
        ConResumen().render()
