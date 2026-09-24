from manim import *


class ActualizarDesdeAlpha(Scene):
    def construct(self):
        a = Dot(LEFT * 4 + UP, color=YELLOW)
        b = Dot(RIGHT * 4 + DOWN, color=YELLOW)
        enlace = Line(a.get_center(), b.get_center())
        disco = Circle(radius=0.2, color=BLUE, fill_opacity=0.6)
        disco.move_to(DOWN * 1.2)

        # UpdateFromFunc: aplica la función en cada fotograma
        # mientras dura la animación (y nada más).
        def unir(m):
            m.put_start_and_end_on(a.get_center(), b.get_center())

        # UpdateFromAlphaFunc: además recibe alpha ∈ [0, 1]
        def crecer(m, alpha):
            m.become(Circle(0.2 + 1.1 * alpha, fill_opacity=0.6,
                color=interpolate_color(BLUE, RED, alpha))
                .move_to(DOWN * 1.2))

        self.add(enlace, a, b, disco)
        self.play(
            a.animate.move_to(LEFT * 2 + UP * 3),
            b.animate.move_to(RIGHT * 5 + UP * 2),
            UpdateFromFunc(enlace, unir),
            UpdateFromAlphaFunc(disco, crecer),
            run_time=2,
        )
