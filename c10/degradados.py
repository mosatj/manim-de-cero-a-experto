from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class Degradados(Scene):
    def construct(self):
        # 1) interpolate_color: once pasos de BLUE a RED
        barra = VGroup(*[
            Square(0.9, stroke_width=0, fill_opacity=1,
                   fill_color=interpolate_color(BLUE, RED, k / 10))
            for k in range(11)
        ]).arrange(RIGHT, buff=0).to_edge(UP, buff=1)
        # 2) color_gradient: una lista de n colores
        tonos = color_gradient([YELLOW, GREEN, BLUE], 15)
        puntos = VGroup(*[Dot(radius=0.25, color=c)
                          for c in tonos])
        puntos.arrange(RIGHT, buff=0.2).shift(0.4 * UP)
        # 3) set_color_by_gradient sobre las partes de un grupo
        texto = Text("degradado", font_size=90, font="sans-serif")
        texto.set_color_by_gradient(ORANGE, PINK, PURPLE)
        texto.shift(1.3 * DOWN)
        # 4) En un solo trazo: el degradado va a lo largo
        onda = FunctionGraph(lambda x: 0.3 * np.sin(3 * x),
                             x_range=[-6, 6])
        onda.set_stroke(width=10).set_color([TEAL, YELLOW, RED])
        onda.to_edge(DOWN, buff=0.5)
        self.add(barra, puntos, texto, onda)
        notas = ["interpolate_color", "color_gradient",
                 "set_color_by_gradient"]
        for obj, t in zip([barra, puntos, texto], notas):
            self.add(Text(t, font_size=22, color=GRAY_A)
                     .next_to(obj, UP, buff=0.12))
