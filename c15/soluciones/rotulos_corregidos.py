from manim import *


class RotulosCorregidos(Scene):
    def construct(self):
        fase = ValueTracker(0)
        puntos = VGroup(*[Dot(color=YELLOW) for _ in range(5)])
        rotulos = VGroup()
        for k, punto in enumerate(puntos):
            # k=k y p=punto congelan los valores de esta vuelta
            punto.add_updater(lambda m, k=k: m.move_to(
                [-4 + 2 * k, np.sin(fase.get_value() + k), 0]))
            rotulos.add(MathTex(f"P_{k}").add_updater(
                lambda m, p=punto: m.next_to(p, UP)))
        self.add(puntos, rotulos)
        self.play(fase.animate.set_value(PI), run_time=2)
