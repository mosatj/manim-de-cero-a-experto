from manim import *


class CurvasRitmo(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 1, 0.25], y_range=[0, 1, 0.25],
                    x_length=6, y_length=6, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24})
        funciones = [(linear, GREY_B, "linear"),
                     (smoothstep, BLUE, "smoothstep"),
                     (smooth, GREEN, "smooth"),
                     (rush_into, RED, "rush_into")]
        leyenda = VGroup()
        self.add(ejes)
        for f, color, nombre in funciones:
            curva = ejes.plot(f, x_range=[0, 1], color=color)
            self.play(Create(curva), run_time=0.8)
            fila = VGroup(Line(ORIGIN, 0.5 * RIGHT, color=color),
                          Text(nombre, font_size=26))
            leyenda.add(fila.arrange(RIGHT, buff=0.2))
        leyenda.arrange(DOWN, aligned_edge=LEFT)
        leyenda.next_to(ejes, RIGHT, buff=0.6)
        self.play(FadeIn(leyenda))
