from manim import *
from estilo import DENTRO, FUERA, PI_REF, TRAZO, GRIS, RADIO_PUNTO


class TableroPuntos(VGroup):
    """El cuadrado unidad con su cuarto de círculo. Los puntos se
    añaden por lotes: un VGroup por lote, no un Dot por play."""

    def __init__(self, lado=4.4, **kwargs):
        super().__init__(**kwargs)
        self.lado = lado
        self.cuadrado = Square(lado, color=TRAZO, stroke_width=2)
        self.arco = Arc(
            radius=lado, angle=PI / 2, color=PI_REF, stroke_width=3,
            arc_center=self.cuadrado.get_corner(DL),
        )
        self.lotes = VGroup()
        self.add(self.cuadrado, self.arco, self.lotes)

    def punto(self, xy, esta_dentro):
        """Traduce (x, y) de [0, 1]^2 a la pantalla. La esquina se
        lee ahora, por si el tablero se ha movido tras crearse."""
        origen = self.cuadrado.get_corner(DL)
        return Dot(
            origen + self.lado * np.array([xy[0], xy[1], 0]),
            radius=RADIO_PUNTO,
            color=DENTRO if esta_dentro else FUERA,
        )

    def anadir(self, coords, mascara):
        """Devuelve la animación que hace aparecer un lote."""
        lote = VGroup(
            *[self.punto(xy, d) for xy, d in zip(coords, mascara)]
        )
        self.lotes.add(lote)
        return FadeIn(lote, lag_ratio=0.5 / len(lote))


class GraficoConvergencia(VGroup):
    """Ejes con n en escala logarítmica y la recta y = pi.
    Cada método devuelve un objeto nuevo o una animación."""

    def __init__(
        self, exp_max=5, y_min=2.4, y_max=4.0, ancho=5.6,
        alto=4.2, **kwargs,
    ):
        super().__init__(**kwargs)
        self.y_min, self.y_max = y_min, y_max
        self.ejes = Axes(
            x_range=[1, exp_max, 1],  # exponentes: de 10^1 a 10^5
            y_range=[y_min, y_max, 0.4],
            x_length=ancho,
            y_length=alto,
            tips=False,
            x_axis_config={"scaling": LogBase()},
            y_axis_config={"include_numbers": True,
                           "decimal_number_config":
                           {"num_decimal_places": 1}},
            axis_config={"font_size": 22, "color": GRIS},
        )
        self.ejes.x_axis.add_labels(  # 10^1 ... 10^5 bajo el eje
            {10**k: MathTex(f"10^{k}", font_size=22)
             for k in range(1, exp_max + 1)}
        )
        self.recta_pi = DashedLine(
            self.ejes.c2p(10, PI), self.ejes.c2p(10**exp_max, PI),
            color=PI_REF, stroke_width=2,
        )
        self.rotulo_pi = MathTex(r"\pi", font_size=30, color=PI_REF)
        self.rotulo_pi.next_to(self.recta_pi, RIGHT, buff=0.1)
        self.nombre_x = Text("n (puntos)", font_size=22, color=GRIS)
        self.nombre_x.next_to(self.ejes.x_axis, DOWN, buff=0.35)
        self.nombre_x.align_to(self.ejes.x_axis, RIGHT)
        self.add(self.ejes, self.recta_pi, self.rotulo_pi,
                 self.nombre_x)

    def poligonal(self, enes, valores, color=DENTRO, grosor=2.5):
        """La trayectoria de la estimación como línea quebrada.
        Los valores se recortan al rango del eje (solo afecta a
        los primeros n, cuando la estimación salta mucho)."""
        valores = np.clip(valores, self.y_min, self.y_max)
        return self.ejes.plot_line_graph(
            enes, valores, add_vertex_dots=False,
            line_color=color, stroke_width=grosor,
        )["line_graph"]
