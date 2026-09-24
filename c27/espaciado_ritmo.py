from manim import *

# Carta de espaciado: dónde está el objeto en 13 instantes igualmente
# separados en el tiempo, según la función de ritmo
RITMOS = [("linear", linear), ("smooth", smooth),
          ("rush_into", rush_into), ("running_start", running_start)]


class EspaciadoRitmo(Scene):
    def construct(self):
        filas = VGroup()
        for i, (nombre, ritmo) in enumerate(RITMOS):
            y = 2.4 - 1.6 * i
            inicio, fin = np.array([-2, y, 0]), np.array([6, y, 0])
            guia = Line(inicio, fin, stroke_width=1, color=GREY_D)
            puntos = VGroup(*[
                Dot(inicio + ritmo(k / 12) * (fin - inicio),
                    radius=0.09,
                    color=interpolate_color(BLUE, YELLOW, k / 12))
                for k in range(13)
            ])
            # Hueco a la izquierda: running_start retrocede al salir
            rotulo = Text(nombre, font="Monospace", font_size=26)
            rotulo.next_to([-3.8, y, 0], LEFT, buff=0)
            filas.add(VGroup(guia, puntos, rotulo))
        self.play(LaggedStart(*[FadeIn(f) for f in filas],
                              lag_ratio=0.3))
        # Una bola real recorre la fila de smooth con ese mismo ritmo
        guia = filas[1][0]
        bola = Dot(guia.get_start(), radius=0.14, color=RED)
        self.play(bola.animate.move_to(guia.get_end()),
                  rate_func=smooth, run_time=2)
