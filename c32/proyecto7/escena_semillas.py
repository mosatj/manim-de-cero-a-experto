from manim import *
from estilo import TRAZO, GRIS, TAM_TITULO, SEMILLAS_COLORES
from azar import puntos
from estimador import trayectoria
from vista import GraficoConvergencia

SEMILLAS = [1, 2, 3, 4, 5]
N_FINAL = 100_000


class CincoSemillas(Scene):
    def construct(self):
        # El eje baja hasta 2 porque con pocos puntos la estimación
        # oscila mucho más que en la primera escena
        grafico = GraficoConvergencia(y_min=2.0, ancho=9, alto=4.8)
        grafico.shift(UP * 0.05)
        titulo = Text(
            "Cinco semillas, cinco caminos, un mismo límite",
            font_size=TAM_TITULO, color=TRAZO,
        ).to_edge(UP, buff=0.3)
        self.play(Create(grafico), Write(titulo))

        enes = np.unique(np.logspace(1, 5, 400).astype(int))
        curvas, leyenda = VGroup(), VGroup()
        for semilla, color in zip(SEMILLAS, SEMILLAS_COLORES):
            valores = trayectoria(puntos(N_FINAL, semilla), enes)
            curvas.add(grafico.poligonal(enes, valores, color, 2))
            leyenda.add(
                VGroup(
                    Line(ORIGIN, RIGHT * 0.4, color=color),
                    Text(f"semilla {semilla}", font_size=20,
                         color=TRAZO),
                ).arrange(RIGHT, buff=0.12)
            )
        leyenda.arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        leyenda.next_to(grafico.ejes.get_corner(UR), DL, buff=0.3)
        self.play(
            LaggedStart(*[Create(c) for c in curvas],
                        lag_ratio=0.3),
            FadeIn(leyenda),
            run_time=6, rate_func=linear,
        )
        nota = Text(
            "--seed siembra random y np.random; "
            "default_rng(semilla) lleva la suya",
            font_size=22, color=GRIS,
        ).to_edge(DOWN, buff=0.15)
        self.play(FadeIn(nota))
        self.wait()
