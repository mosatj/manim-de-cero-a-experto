from manim import *

FILAS = ["figura", "fórmula", "resultado", "cierre"]


def hoja(tramos, titulo, acento=None):
    """tramos: (duración, pausa) de cada fila, en segundos."""
    eje = NumberLine(x_range=[0, 10, 2], length=9.5,
                     include_numbers=True, font_size=40)
    eje.shift([-3.3, -2.4, 0] - eje.n2p(0))  # el 0 en (-3.3, -2.4)
    hoja = VGroup(eje, Text(titulo, font_size=48).to_edge(UP))
    t = 0
    for i, (fila, (duracion, pausa)) in enumerate(zip(FILAS, tramos)):
        y = 1.9 - 1.1 * i
        x0 = eje.n2p(t)[0]
        x1 = eje.n2p(t + duracion)[0]
        x2 = eje.n2p(t + duracion + pausa)[0]
        color = RED if i == acento else BLUE
        barra = Rectangle(width=x1 - x0, height=0.6, stroke_width=0,
                          fill_color=color, fill_opacity=0.85)
        barra.move_to([(x0 + x1) / 2, y, 0])
        rotulo = Text(fila, font_size=44)
        rotulo.move_to([-3.6, y, 0], aligned_edge=RIGHT)
        hoja.add(barra, rotulo)
        if pausa:  # una línea fina: la escena está quieta
            hoja.add(Line([x1, y, 0], [x2, y, 0], color=GRAY,
                          stroke_width=5))
        t += duracion + pausa
    return hoja


class TiemposAntes(Scene):
    def construct(self):
        self.play(FadeIn(hoja([(1, 0)] * 4, "Todo dura 1 s")))


class TiemposDespues(Scene):
    def construct(self):
        tramos = [(2, 1), (1.5, 0.5), (0.5, 2), (1, 1)]
        tabla = hoja(tramos, "Acento breve, pausa larga", acento=2)
        pausa = Text("pausa", font_size=40, color=GRAY)
        pausa.move_to([tabla[0].n2p(6.5)[0], -0.8, 0])
        self.play(FadeIn(tabla), FadeIn(pausa))
