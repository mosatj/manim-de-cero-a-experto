from manim import *
from estilo import DENTRO, FUERA, PI_REF, TRAZO
from estilo import TAM_TITULO, TAM_ROTULO
from azar import puntos, SEMILLA
from estimador import dentro, estimaciones, trayectoria
from vista import TableroPuntos, GraficoConvergencia

LOTES = [10, 40, 50, 100, 200, 400, 800, 400]  # suman 2000
N_FINAL = 100_000  # hasta aquí se cuenta; se dibuja hasta 2000


class EstimarPi(Scene):
    def construct(self):
        datos = puntos(N_FINAL)
        mascara = dentro(datos)
        tablero = TableroPuntos().to_edge(LEFT, buff=0.6)
        tablero.shift(DOWN * 0.2)
        grafico = GraficoConvergencia().to_edge(RIGHT, buff=0.5)
        grafico.shift(DOWN * 0.2)
        titulo = Text(
            f"Estimar π con puntos al azar (semilla {SEMILLA})",
            font_size=TAM_TITULO, color=TRAZO,
        ).to_edge(UP, buff=0.25)
        # Contadores: n y la estimación, bajo el título
        n_rotulo = MathTex("n =", font_size=36, color=TRAZO)
        n_valor = Integer(0, font_size=36, color=TRAZO,
                          group_with_commas=False)
        pi_rotulo = MathTex(r"\pi \approx", font_size=36,
                            color=TRAZO)
        pi_valor = DecimalNumber(
            0, num_decimal_places=4, font_size=36, color=PI_REF
        )
        # Dos bloques separados: cada número crece hacia la derecha
        # (edge_to_fix=LEFT por defecto) sin empujar al otro
        bloque_n = VGroup(n_rotulo, n_valor)
        bloque_n.arrange(RIGHT, buff=0.2)
        bloque_pi = VGroup(pi_rotulo, pi_valor)
        bloque_pi.arrange(RIGHT, buff=0.2)
        bloque_n.next_to(titulo, DOWN, buff=0.15)
        bloque_pi.next_to(titulo, DOWN, buff=0.15)
        bloque_n.shift(LEFT * 2.6), bloque_pi.shift(RIGHT * 1.6)
        self.play(Create(tablero), Create(grafico), Write(titulo))
        self.play(FadeIn(bloque_n), FadeIn(bloque_pi))

        # Lotes visibles: cada play añade un VGroup de puntos y
        # prolonga la trayectoria desde el n anterior
        n_previo = 0
        for n, d, estimacion in estimaciones(datos, LOTES):
            enes = list(range(max(n_previo, 10), n + 1))
            valores = trayectoria(datos, enes)
            tramo = grafico.poligonal(enes, valores)
            self.play(
                tablero.anadir(datos[n_previo:n],
                               mascara[n_previo:n]),
                Create(tramo),
                n_valor.animate.set_value(n),
                pi_valor.animate.set_value(estimacion),
                run_time=1.2,
            )
            n_previo = n

        # De 2000 a 100 000: se cuenta pero ya no se dibuja
        aviso = Text(
            "hasta 100 000 puntos:\nse cuentan, no se dibujan",
            font_size=TAM_ROTULO, color=FUERA, line_spacing=0.8,
        ).next_to(tablero, DOWN, buff=0.15)
        enes = np.logspace(np.log10(2000), 5, 300).astype(int)
        enes = np.unique(enes)
        valores = trayectoria(datos, enes)
        cola = grafico.poligonal(enes, valores, color=DENTRO)
        self.play(
            FadeIn(aviso),
            Create(cola, rate_func=linear),
            n_valor.animate.set_value(N_FINAL),
            pi_valor.animate.set_value(valores[-1]),
            run_time=4,
        )
        error = abs(valores[-1] - PI)
        cierre = MathTex(
            rf"|\,\text{{estimación}}-\pi\,| = {error:.4f}",
            font_size=30, color=TRAZO,
        ).next_to(grafico.nombre_x, DOWN, buff=0.15)
        cierre.align_to(grafico.ejes, RIGHT)
        self.play(Write(cierre))
        self.wait()
