from manim import *


class Espia(Animation):
    """Animación que solo anuncia qué método se llama."""

    def begin(self):
        print("    begin()")
        super().begin()

    def interpolate_mobject(self, alpha):
        print(f"      interpolate_mobject({alpha:.2f})")

    def finish(self):
        print("    finish()")
        super().finish()

    def clean_up_from_scene(self, scene):
        print("    clean_up_from_scene()")
        super().clean_up_from_scene(scene)


class Ciclo(Scene):
    def setup(self):
        print("setup()")

    def construct(self):
        print("construct()")
        print("  play(Espia) con run_time=1 a 5 fps:")
        self.play(Espia(Square(), run_time=1))

    def tear_down(self):
        print("tear_down()")


if __name__ == "__main__":
    ajustes = {"frame_rate": 5, "dry_run": True,
               "verbosity": "WARNING", "progress_bar": "none"}
    with tempconfig(ajustes):
        Ciclo().render()
