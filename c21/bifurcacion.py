from manim import *


def diagrama(r_min, r_max, columnas=1200, transitorio=600,
             muestras=120):
    """Pares (r, x) que forman el atractor del mapa logístico."""
    r = np.linspace(r_min, r_max, columnas)
    x = np.full(columnas, 0.5)
    for _ in range(transitorio):          # olvida el estado inicial
        x = r * x * (1 - x)
    pares = []
    for _ in range(muestras):              # registra lo que queda
        x = r * x * (1 - x)
        pares.append(np.column_stack([r, x]))
    return np.vstack(pares)


class Bifurcacion(Scene):
    def construct(self):
        ejes = Axes(x_range=[2.8, 4, 0.2], y_range=[0, 1, 0.2],
                    x_length=12, y_length=6.4, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 22,
                                 "decimal_number_config":
                                     {"num_decimal_places": 1}})
        ejes.to_edge(DOWN, buff=0.4)
        datos = diagrama(2.8, 4.0)                  # 144 000 pares
        # c2p acepta un array (N, 2) entero: una sola llamada
        pantalla = ejes.c2p(datos)                  # forma (N, 3)
        r_act = ValueTracker(2.8)

        def revelar(nube):
            # Nube de puntos (PMobject): se vacía y se rellena en
            # cada fotograma con las columnas de r ya barridas
            nube.reset_points()
            barridas = datos[:, 0] <= r_act.get_value()
            nube.add_points(pantalla[barridas], color=WHITE)

        nube = PMobject(stroke_width=2).add_updater(revelar)
        self.add(ejes, nube)
        self.play(r_act.animate.set_value(4), run_time=8,
                  rate_func=linear)
        # Primeras bifurcaciones: r1 = 3, r2 = 1 + sqrt(6)
        marcas = VGroup()
        for valor, texto, lado in (
                (3, "r_1 = 3", UP),
                (1 + np.sqrt(6), r"r_2 = 1+\sqrt 6", UL),
                (3.5699, r"r_\infty \approx 3.5699", UR)):
            linea = ejes.get_vertical_line(ejes.c2p(valor, 1),
                                           color=YELLOW)
            rot = MathTex(texto, font_size=26, color=YELLOW)
            rot.next_to(linea.get_top(), lado, buff=0.1)
            marcas.add(linea, rot)
        self.play(FadeIn(marcas))
