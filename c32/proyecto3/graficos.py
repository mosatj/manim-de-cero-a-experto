from manim import *

VIVO = "#6FA3C0"  # dado que sigue en juego
DESINTEGRADO = "#3A3F44"  # dado retirado
DATO, AJUSTE = "#E0B04A", "#B04A5A"  # puntos y curva ajustada


class MallaNucleos(VGroup):
    """Una casilla por dado. Quién «se desintegra» se sortea,
    pero cuántos lo hacen en cada ronda lo dicta el CSV."""

    def __init__(
        self, total=600, columnas=30, lado=0.17, semilla=7, **kwargs
    ):
        super().__init__(**kwargs)
        self.add(
            *[
                Square(
                    lado,
                    stroke_width=0,
                    fill_color=VIVO,
                    fill_opacity=1,
                )
                for _ in range(total)
            ]
        )
        self.arrange_in_grid(cols=columnas, buff=0.04)
        self.vivos = list(range(total))
        self.rng = np.random.default_rng(semilla)

    def desintegrar(self, cantidad):
        elegidos = self.rng.choice(
            self.vivos, cantidad, replace=False
        )
        self.vivos = [
            i for i in self.vivos if i not in set(elegidos)
        ]
        return LaggedStart(
            *[
                self[i].animate.set_fill(DESINTEGRADO)
                for i in elegidos
            ],
            lag_ratio=0.01,
        )


class GraficoDecaimiento(VGroup):
    """Ejes con los datos; cada método añade una capa."""

    def __init__(
        self, rondas_max=16, n_max=600, ancho=6, alto=4.2, **kwargs
    ):
        super().__init__(**kwargs)
        self.ejes = Axes(
            x_range=[0, rondas_max, 2],
            y_range=[0, n_max, 100],
            x_length=ancho,
            y_length=alto,
            tips=False,
            axis_config={"include_numbers": True, "font_size": 24},
        )
        self.rotulos = self.ejes.get_axis_labels(
            Text("ronda", font_size=24),
            Text("quedan", font_size=24),
        )
        self.add(self.ejes, self.rotulos)

    def punto(self, ronda, quedan):
        return Dot(
            self.ejes.c2p(ronda, quedan), radius=0.06, color=DATO
        )

    def curva_ajuste(self, n0, k, rondas_max=16):
        return self.ejes.plot(
            lambda n: n0 * np.exp(-k * n),
            x_range=[0, rondas_max],
            color=AJUSTE,
        )

    def marca_semivida(self, n0, semivida):
        mitad = n0 / 2
        return VGroup(
            DashedLine(
                self.ejes.c2p(0, mitad),
                self.ejes.c2p(semivida, mitad),
            ),
            DashedLine(
                self.ejes.c2p(semivida, mitad),
                self.ejes.c2p(semivida, 0),
            ),
        ).set_color(GREY_B)
