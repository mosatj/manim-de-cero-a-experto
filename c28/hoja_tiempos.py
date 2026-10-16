from manim import *

# Hoja de tiempos de Snyder (guion de 110 páginas) trasladada a un
# vídeo de DURACION segundos con una regla de tres
DURACION = 360
PAGINAS = 110
TIEMPOS = [  # (nombre, página inicial, página final si es tramo)
    ("Imagen de apertura", 1, None),
    ("Declaración del tema", 5, None),
    ("Planteamiento", 1, 10),
    ("Catalizador", 12, None),
    ("Debate", 12, 25),
    ("Transición al 2.º acto", 25, None),
    ("Trama B", 30, None),
    ("Juegos y risas", 30, 55),
    ("Punto intermedio", 55, None),
    ("Los malos estrechan el cerco", 55, 75),
    ("Todo está perdido", 75, None),
    ("Noche oscura del alma", 75, 85),
    ("Transición al 3.er acto", 85, None),
    ("Final", 85, 110),
    ("Imagen de cierre", 110, None),
]
ACTOS = [(0, 25, "Acto I", BLUE_D), (25, 55, "II a", TEAL_D),
         (55, 85, "II b", GOLD_D), (85, 110, "Acto III", RED_D)]
X0, X1 = -1.2, 6.6  # tramo del marco que ocupa el eje del tiempo


def x_de(pagina):
    return X0 + (X1 - X0) * pagina / PAGINAS


def color_de(pagina):
    for inicio, fin, _, color in ACTOS:
        if pagina < fin:
            return color
    return ACTOS[-1][3]


def barra(inicio, fin, alto, y, **estilo):
    """Rectángulo desde la página inicio hasta la página fin."""
    ancho = x_de(fin) - x_de(inicio)
    rect = RoundedRectangle(width=ancho, height=alto, stroke_width=0,
                            fill_opacity=1, **estilo)
    return rect.move_to([(x_de(inicio) + x_de(fin)) / 2, y, 0])


class HojaTiempos(Scene):
    def construct(self):
        fondo, filas = VGroup(), VGroup()
        for inicio, fin, nombre, color in ACTOS:
            banda = barra(inicio, fin, 7, -0.05, corner_radius=0,
                          fill_color=color).set_fill(opacity=0.12)
            rotulo = Text(nombre, font_size=28, color=color)
            fondo.add(banda, rotulo.next_to(banda, UP, buff=0.1))
        for i, (nombre, inicio, fin) in enumerate(TIEMPOS):
            y = 3.05 - 0.44 * i
            color = color_de(inicio)
            texto = Text(nombre, font_size=28)
            texto.move_to([X0 - 0.3, y, 0], aligned_edge=RIGHT)
            if fin is None:  # un instante: un punto
                marca = Dot([x_de(inicio), y, 0], radius=0.11,
                            color=color)
            else:  # un tramo: una barra
                marca = barra(inicio, fin, 0.2, y,
                              corner_radius=0.08, fill_color=color)
            filas.add(VGroup(texto, marca))
        eje = NumberLine(x_range=[0, DURACION, 60], length=X1 - X0,
                         include_numbers=False)
        eje.move_to([(X0 + X1) / 2, -3.45, 0])
        minutos = VGroup(*[
            Text(f"{m}:00", font_size=28).next_to(
                eje.n2p(60 * m), DOWN, buff=0.12)
            for m in range(DURACION // 60 + 1)])
        self.add(fondo, eje, minutos)
        self.play(LaggedStart(*[FadeIn(f, shift=0.2 * RIGHT)
                                for f in filas], lag_ratio=0.15),
                  run_time=3)
        self.wait()
