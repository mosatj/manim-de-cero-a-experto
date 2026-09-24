from manim import *


def primos_hasta(n):
    criba = [True] * (n + 1)
    criba[0] = criba[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if criba[p]:
            criba[p * p::p] = [False] * len(criba[p * p::p])
    return [k for k, es in enumerate(criba) if es]


def porcentajes(n):
    """% de primos mayores que 5 que terminan en 1, 3, 7 y 9."""
    finales = [p % 10 for p in primos_hasta(n) if p > 5]
    return [round(100 * finales.count(d) / len(finales), 1)
            for d in (1, 3, 7, 9)]


class DigitosPrimos(Scene):
    def construct(self):
        grafico = BarChart(porcentajes(100),
                           bar_names=["1", "3", "7", "9"],
                           y_range=[0, 35, 5], y_length=5,
                           x_length=7, bar_colors=[BLUE_D, TEAL])
        titulo = Text("Última cifra de los primos menores que 100",
                      font_size=30).to_edge(UP)
        self.add(grafico, titulo)
        # Al subir el límite, los cuatro finales se igualan
        nuevo = Text("... menores que 1 000 000", font_size=30)
        nuevo.move_to(titulo)
        self.play(grafico.animate.change_bar_values(
                      porcentajes(10 ** 6)),
                  Transform(titulo, nuevo), run_time=2)
        self.add(grafico.get_bar_labels(font_size=28))
        self.wait()
