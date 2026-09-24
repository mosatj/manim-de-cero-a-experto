from manim import *
from datos_grafo import VERTICES, ARISTAS, POSICIONES, ORIGEN
from dijkstra import pasos_dijkstra
from vista_grafo import GrafoPesado


class DijkstraAnimado(Scene):
    """Controlador: recorre los eventos del modelo y los traduce a
    animaciones de la vista. Cambiar el grafo no toca esta clase."""

    def construct(self):
        vista = GrafoPesado(VERTICES, ARISTAS, POSICIONES)
        titulo = Text(
            "Dijkstra: caminos más cortos desde A", font_size=34
        ).to_edge(UP, buff=0.3)
        self.play(
            Create(vista.grafo),
            Write(vista.nombres),
            FadeIn(vista.pesos),
            Write(titulo),
        )
        self.play(FadeIn(*vista.distancias.values()))

        rotulo = Text(" ", font_size=28).to_edge(DOWN)
        for evento in pasos_dijkstra(VERTICES, ARISTAS, ORIGEN):
            if evento[0] == "fijar":
                _, u, d = evento
                texto = f"Fijamos {u}: distancia {d}, definitiva"
                animacion = vista.fijar(u, d)
            elif evento[0] == "relajar":
                _, u, v, d, mejora = evento
                texto = f"{u} → {v}: {d} " + (
                    "mejora la marca" if mejora else "no mejora"
                )
                animacion = vista.relajar(u, v, d, mejora)
            else:
                texto = "Árbol de caminos más cortos"
                animacion = vista.camino(evento[2])
            nuevo = Text(texto, font_size=28).to_edge(DOWN)
            self.play(
                animacion, Transform(rotulo, nuevo), run_time=0.9
            )
