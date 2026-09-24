from manim import *


class Bandera(Scene):
    def construct(self):
        mastil = Line(DOWN * 3.5, UP * 2.5, color=GREY_B)
        mastil.set_stroke(width=8).shift(LEFT * 4)
        tela = Rectangle(width=6, height=3.5, color=RED,
                         fill_opacity=0.8)
        tela.next_to(mastil.get_top(), RIGHT, buff=0)
        tela.shift(DOWN * 1.75).insert_n_curves(40)
        x_mastil = mastil.get_x()

        # Onda viajera; la amplitud crece al alejarse del mástil
        def ondear(x, y, z, t):
            d = x - x_mastil
            return (x, y + 0.12 * d * np.sin(2 * d - 8 * PI * t), z)

        self.add(mastil)
        self.play(Homotopy(ondear, tela, run_time=4),
                  rate_func=linear)
