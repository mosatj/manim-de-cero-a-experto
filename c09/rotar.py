from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class Rotar(Scene):
    def construct(self):
        flecha = Arrow(ORIGIN, 2.8 * RIGHT, buff=0)
        colores = color_gradient([BLUE, RED], 6)
        # Izquierda: gira sobre su propio centro (por defecto)
        izq = VGroup(*[
            flecha.copy().rotate(k * 30 * DEGREES)
            for k in range(6)
        ]).move_to(3.5 * LEFT)
        # Derecha: gira alrededor de su punto de partida
        der = VGroup(*[
            flecha.copy().rotate(k * 30 * DEGREES,
                                 about_point=ORIGIN)
            for k in range(6)
        ]).shift(2.2 * RIGHT + 1.2 * DOWN)
        for grupo in (izq, der):
            for f, c in zip(grupo, colores):
                f.set_color(c)
        self.add(izq, der)
        self.add(Dot(izq.get_center(), color=WHITE),
                 Dot(der[0].get_start(), color=WHITE))
        self.add(Text("rotate(k*30*DEGREES)", font_size=28)
                 .move_to([-3.5, -2.9, 0]))
        self.add(Text("rotate(k*30*DEGREES,", font_size=28)
                 .move_to([3.5, -2.3, 0]),
                 Text("about_point=ORIGIN)", font_size=28)
                 .move_to([3.5, -2.9, 0]))
