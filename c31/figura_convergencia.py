from manim import *
from tabla_heun_corregida import euler, heun, rk4, exacta

# Figura para un artículo: ejes log-log y datos calculados
ARTICULO = False  # True: fondo blanco y tinta negra (revista)
FONDO, TINTA = (WHITE, BLACK) if ARTICULO else (BLACK, WHITE)
config.background_color = FONDO
COLORES = {"Euler": "#B04A5A", "Heun": "#6FA3C0", "RK4": "#E0B04A"}


def error_final(paso, h, t_final=2.0):
    """Error absoluto en t_final al integrar con paso h."""
    t, y = 0.0, 0.5
    for _ in range(round(t_final / h)):
        y, t = paso(t, y, h), t + h
    return abs(y - exacta(t_final))


class FiguraConvergencia(Scene):
    def construct(self):
        ejes = Axes(
            x_range=[-6, -1, 1],
            y_range=[-10, 0, 2],
            x_length=8,
            y_length=5.6,
            x_axis_config={"scaling": LogBase(base=2)},
            y_axis_config={"scaling": LogBase()},
            axis_config={"color": TINTA, "include_numbers": True},
            tips=False,
        ).shift(LEFT * 1.2)
        ejes.set_color(TINTA)  # ejes, marcas y rótulos 2^k, 10^k
        rotulos = ejes.get_axis_labels(
            MathTex("h", color=TINTA),
            MathTex(r"|e(2)|", color=TINTA),
        )
        self.add(ejes, rotulos)

        pasos = [2.0**-k for k in range(1, 7)]
        leyenda = VGroup()
        for nombre, paso in (
            ("Euler", euler),
            ("Heun", heun),
            ("RK4", rk4),
        ):
            puntos = [
                ejes.c2p(h, error_final(paso, h)) for h in pasos
            ]
            linea = VMobject(color=COLORES[nombre], stroke_width=4)
            linea.set_points_as_corners(puntos)
            marcas = VGroup(
                *[Dot(p, color=COLORES[nombre]) for p in puntos]
            )
            self.play(Create(linea), FadeIn(marcas))
            leyenda.add(
                VGroup(
                    Dot(color=COLORES[nombre]),
                    Text(nombre, color=TINTA, font_size=26),
                ).arrange(RIGHT, buff=0.15)
            )
        leyenda.arrange(DOWN, aligned_edge=LEFT).next_to(
            ejes, RIGHT
        )
        self.add(leyenda)
