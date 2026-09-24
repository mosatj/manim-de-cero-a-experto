from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class TrazoRelleno(Scene):
    def construct(self):
        anchos = [1, 4, 8, 16]
        opacidades = [0, 0.25, 0.5, 1]
        rejilla = VGroup()
        for w in anchos:
            for o in opacidades:
                rejilla.add(Square(1.1).set_style(
                    stroke_color=YELLOW, stroke_width=w,
                    fill_color=BLUE, fill_opacity=o))
        rejilla.arrange_in_grid(rows=4, cols=4, buff=0.4)
        rejilla.shift(1.5 * RIGHT + 0.5 * DOWN)
        self.add(rejilla)
        # Rótulos de filas (grosor) y de columnas (opacidad)
        for i, w in enumerate(anchos):
            self.add(Text(f"stroke_width={w}", font_size=26)
                     .next_to(rejilla[4 * i], LEFT, buff=0.5))
        for j, o in enumerate(opacidades):
            self.add(Text(str(o), font_size=26)
                     .next_to(rejilla[j], UP, buff=0.2))
        self.add(Text("fill_opacity", font_size=26)
                 .next_to(rejilla, UP, buff=0.8))
