from manim import *


class Termometro(VGroup):
    def __init__(self, t_min=0, t_max=100, alto=5, **kwargs):
        super().__init__(**kwargs)
        self.t_min, self.t_max, self.alto = t_min, t_max, alto
        self.tubo = RoundedRectangle(corner_radius=0.2, width=0.4,
                                     height=alto, color=WHITE)
        self.bulbo = Circle(radius=0.4, color=RED, fill_opacity=1)
        self.bulbo.next_to(self.tubo, DOWN, buff=-0.15)
        self.columna = Rectangle(width=0.2, height=0.01, color=RED,
                                 fill_opacity=1, stroke_width=0)
        self.add(self.tubo, self.columna, self.bulbo)
        self.nivel(t_min)

    def nivel(self, t):
        """Ajusta la columna a la temperatura t; devuelve self."""
        fraccion = (t - self.t_min) / (self.t_max - self.t_min)
        alto = max(0.01, fraccion * (self.alto - 0.3))
        self.columna.stretch_to_fit_height(alto)
        self.columna.next_to(self.bulbo, UP, buff=-0.1)
        return self


class EscenaTermometro(Scene):
    def construct(self):
        termo = Termometro()
        self.add(termo)
        self.play(termo.animate.nivel(75), run_time=2)
        self.wait()
