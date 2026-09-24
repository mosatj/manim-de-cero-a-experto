from manim import *

PENDIENTE, FIJADO, CAMINO = GREY_B, "#6FA3C0", "#E0B04A"


class GrafoPesado(VGroup):
    """Vista: un Graph de Manim con pesos y distancias
    provisionales. Sus métodos no animan: devuelven animaciones
    para self.play()."""

    def __init__(self, vertices, aristas, posiciones, **kwargs):
        super().__init__(**kwargs)
        self.grafo = Graph(
            vertices,
            list(aristas),
            layout=posiciones,
            vertex_config={"radius": 0.3, "color": PENDIENTE},
            edge_config={"stroke_width": 3, "color": GREY},
        )
        self.nombres = VGroup(
            *[
                MathTex(v, color=BLACK).move_to(self.grafo[v])
                for v in vertices
            ]
        ).set_z_index(1)  # siempre sobre el punto
        self.pesos = VGroup(
            *[
                self._peso(self.grafo.edges[e], p)
                for e, p in aristas.items()
            ]
        )
        centro = np.mean(
            [np.array(p) for p in posiciones.values()], axis=0
        )
        self.lugar = {
            v: normalize(np.array(posiciones[v]) - centro)
            for v in vertices
        }
        self.distancias = {
            v: self._distancia(v, r"\infty") for v in vertices
        }
        self.add(
            self.grafo,
            self.pesos,
            self.nombres,
            *self.distancias.values(),
        )

    @staticmethod
    def _peso(arista, peso):
        mitad = arista.get_center()
        normal = rotate_vector(arista.get_unit_vector(), PI / 2)
        return MathTex(
            str(peso), font_size=32, color=GREY_A
        ).move_to(mitad + 0.3 * normal)

    def _distancia(self, v, texto, color=WHITE):
        return MathTex(texto, font_size=38, color=color).move_to(
            self.grafo[v].get_center() + 0.7 * self.lugar[v]
        )

    def arista(self, u, v):
        aristas = self.grafo.edges
        return (
            aristas[(u, v)]
            if (u, v) in aristas
            else aristas[(v, u)]
        )

    # --- Una animación por cada evento del algoritmo ---
    def fijar(self, u, d):
        definitiva = self._distancia(u, str(d), color=FIJADO)
        return AnimationGroup(
            self.grafo[u].animate.set_color(FIJADO),
            Transform(self.distancias[u], definitiva),
        )

    def relajar(self, u, v, d, mejora):
        destello = ShowPassingFlash(
            self.arista(u, v).copy().set_stroke(YELLOW, 8),
            time_width=0.6,
        )
        if not mejora:
            return AnimationGroup(
                destello, Wiggle(self.distancias[v])
            )
        nueva = self._distancia(v, str(d), color=YELLOW)
        cambio = Transform(self.distancias[v], nueva)
        return AnimationGroup(destello, cambio)

    def camino(self, previos):
        tramos = [
            self.arista(previos[v], v)
            for v in previos
            if previos[v] is not None
        ]
        return AnimationGroup(
            *[t.animate.set_stroke(CAMINO, 7) for t in tramos]
        )
