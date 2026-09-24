from manim import *

# Datos: temperatura de una taza de café que se enfría (modelo de
# Newton, T = 20 + 70 e^(-0.08 t)) calculada cada 5 minutos
TIEMPOS = np.arange(0, 45, 5)
TEMPERATURAS = 20 + 70 * np.exp(-0.08 * TIEMPOS)


class GraficaAntes(Scene):
    """Todo por defecto: funciona, pero cuesta leerla."""

    def construct(self):
        ejes = Axes(x_range=[0, 45, 5], y_range=[0, 100, 10],
                    axis_config={"include_numbers": True})
        rotulos = ejes.get_axis_labels("t", "T")
        datos = ejes.plot_line_graph(TIEMPOS, TEMPERATURAS)
        modelo = ejes.plot(lambda t: 20 + 70 * np.exp(-0.08 * t),
                           color=GREEN)
        ambiente = ejes.plot(lambda t: 20, color=RED)
        leyenda = VGroup(
            Text("datos", color=YELLOW),
            Text("modelo", color=GREEN),
            Text("ambiente", color=RED)).arrange(DOWN).to_corner(UR)
        self.add(ejes, rotulos, datos, modelo, ambiente, leyenda)


class GraficaDespues(Scene):
    """Las mismas capas, diseñadas para leerse de un vistazo."""

    def construct(self):
        tinta, gris = GRAY_B, GRAY_D
        ejes = Axes(
            x_range=[0, 42, 10], y_range=[0, 100, 20],
            x_length=10, y_length=4.8, tips=False,
            axis_config={"color": tinta, "stroke_width": 1.5,
                         "include_numbers": True, "font_size": 26,
                         "tick_size": 0.06},
        ).shift(DOWN * 0.1)
        # Rejilla horizontal tenue: ayuda a leer valores, no compite
        rejilla = VGroup(*[
            Line(ejes.c2p(0, y), ejes.c2p(42, y), color=gris,
                 stroke_width=1) for y in range(20, 101, 20)])
        eje_x = Text("tiempo (min)", font_size=24, color=tinta)
        eje_x.next_to(ejes.x_axis, DOWN, buff=0.5)
        eje_y = Text("temperatura (°C)", font_size=24, color=tinta)
        eje_y.next_to(ejes.y_axis, UP, buff=0.2)
        eje_y.align_to(ejes, LEFT)
        ambiente = DashedLine(ejes.c2p(0, 20), ejes.c2p(42, 20),
                              color=GRAY_B, stroke_width=2)
        modelo = ejes.plot(lambda t: 20 + 70 * np.exp(-0.08 * t),
                           x_range=[0, 42], color=BLUE,
                           stroke_width=3)
        puntos = VGroup(*[Dot(ejes.c2p(t, T), radius=0.07,
                              color=YELLOW)
                          for t, T in zip(TIEMPOS, TEMPERATURAS)])
        puntos.set_z_index(2)           # por encima de la curva
        # Rótulos directos junto a cada elemento, sin leyenda
        et_datos = Text("cada 5 min", font_size=24, color=YELLOW)
        et_datos.next_to(puntos[1], UR, buff=0.15)
        et_modelo = Text("ley de Newton", font_size=24, color=BLUE)
        et_modelo.next_to(ejes.c2p(20, 34), UR, buff=0.1)
        et_amb = Text("ambiente, 20 °C", font_size=22, color=GRAY_B)
        et_amb.next_to(ejes.c2p(42, 20), DOWN, buff=0.12)
        et_amb.align_to(ejes.c2p(42, 0), RIGHT)
        titulo = Text("El café tarda media hora en llegar a 26 °C",
                      font_size=30).to_edge(UP, buff=0.3)
        self.add(rejilla, ejes, eje_x, eje_y, ambiente, modelo,
                 puntos, et_datos, et_modelo, et_amb, titulo)
