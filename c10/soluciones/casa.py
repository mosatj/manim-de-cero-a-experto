from manim import *


class Casa(Scene):
    def construct(self):
        muros = Square(3, color=WHITE, fill_color=GOLD_E,
                       fill_opacity=1)
        tejado = Triangle(color=RED, fill_opacity=1)
        tejado.stretch_to_fit_width(3.6).stretch_to_fit_height(1.6)
        tejado.next_to(muros, UP, buff=0)
        puerta = Rectangle(width=0.8, height=1.4, color=DARK_BROWN,
                           fill_opacity=1)
        puerta.align_to(muros, DOWN)
        ventana = Square(0.7, color=BLUE_B, fill_opacity=1)
        ventana.move_to(muros).shift(0.8 * UP + 0.7 * RIGHT)
        self.add(VGroup(muros, tejado, puerta, ventana))
