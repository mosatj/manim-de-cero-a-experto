from manim import *


class Contador(Animation):
    llamadas = 0

    def interpolate_mobject(self, alpha):
        Contador.llamadas += 1


class Prueba(Scene):
    def construct(self):
        self.play(Contador(Circle(), run_time=2))


if __name__ == "__main__":
    ajustes = {"quality": "low_quality", "dry_run": True,
               "verbosity": "WARNING", "progress_bar": "none"}
    with tempconfig(ajustes):
        Prueba().render()
    print("fps:", 15, "| run_time:", 2)
    print("Llamadas a interpolate_mobject:",
          Contador.llamadas)
