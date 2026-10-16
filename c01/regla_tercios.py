from manim import *

# Fotograma apaisado (franja): tres marcos 16:9 en fila, sin aire sobrante
config.frame_height = 4.4
config.pixel_height = round(config.pixel_width * 4.4 / config.frame_width)

ANCHO, ALTO = 4.2, 4.2 * 9 / 16  # cada panel es un marco 16:9 reducido
PHI = (1 + 5**0.5) / 2


def lineas_guia(fracciones, tono, discontinuas=True):
    """Líneas verticales y horizontales en las fracciones dadas."""
    guia = VGroup()
    for f in fracciones:
        x, y = -ANCHO / 2 + f * ANCHO, -ALTO / 2 + f * ALTO
        guia.add(Line([x, -ALTO / 2, 0], [x, ALTO / 2, 0]),
                 Line([-ANCHO / 2, y, 0], [ANCHO / 2, y, 0]))
    guia.set_stroke(tono, 2)
    return VGroup(*[DashedLine(l.get_start(), l.get_end(), dash_length=0.08)
                    .set_stroke(tono, 2) for l in guia]) if discontinuas \
        else guia


def bloque_texto(lineas, ancho):
    """Un párrafo esquemático: barras grises en lugar de letras."""
    return VGroup(*[RoundedRectangle(corner_radius=0.04, height=0.09,
                                     width=ancho * (0.6 if k == lineas - 1
                                                    else 1),
                                     stroke_width=0, fill_color=GREY_B,
                                     fill_opacity=1)
                    for k in range(lineas)]).arrange(DOWN, buff=0.09,
                                                     aligned_edge=LEFT)


def escena(foco, texto_en, horizonte):
    """El mismo contenido: horizonte, un objeto protagonista y un texto."""
    marco = Rectangle(width=ANCHO, height=ALTO, color=GREY_C,
                      stroke_width=3)
    suelo = Line([-ANCHO / 2, horizonte, 0], [ANCHO / 2, horizonte, 0],
                 color=GREY_C, stroke_width=3)
    protagonista = Circle(radius=0.36, color=RED_C, fill_opacity=0.85)
    protagonista.move_to(foco)
    titulo = RoundedRectangle(corner_radius=0.05, height=0.16, width=1.3,
                              stroke_width=0, fill_color=BLUE,
                              fill_opacity=1)
    parrafo = bloque_texto(3, 1.3)
    texto = VGroup(titulo, parrafo).arrange(DOWN, buff=0.14,
                                            aligned_edge=LEFT)
    texto.move_to(texto_en)
    return VGroup(marco, suelo, protagonista, texto)


class ReglaTercios(Scene):
    def construct(self):
        tercio_x, tercio_y = ANCHO / 6, ALTO / 6   # ±1/6 = 1/3 y 2/3
        aureo_x = ANCHO * (1 / PHI - 0.5)          # 0,618 desde la izq.
        aureo_y = ALTO * (1 / PHI**2 - 0.5)        # 0,382 desde abajo
        centrado = escena(ORIGIN, UP * 0.8, 0.0)
        tercios = VGroup(
            # el protagonista en un punto fuerte; el horizonte, en un tercio
            escena([-tercio_x, -tercio_y, 0], [tercio_x + 0.62,
                   tercio_y - 0.2, 0], -tercio_y),
            lineas_guia([1 / 3, 2 / 3], RED_C))
        puntos = VGroup(*[Dot([sx * tercio_x, sy * tercio_y, 0],
                              radius=0.06, color=RED_C)
                          for sx in (-1, 1) for sy in (-1, 1)])
        tercios.add(puntos)
        aurea = VGroup(
            escena([aureo_x, aureo_y, 0], [-0.95, ALTO / 4, 0], aureo_y),
            lineas_guia([1 / PHI**2, 1 / PHI], TEAL_C))

        paneles = VGroup()
        for dibujo, nombre, nota in (
                (centrado, "centrado", "estable, estático"),
                (tercios, "regla de los tercios", "puntos fuertes en 1/3 y 2/3"),
                (aurea, "proporción áurea", "líneas en 0,382 y 0,618")):
            rotulo = Text(nombre, font_size=28)
            detalle = Text(nota, font_size=22, color=GREY_B)
            paneles.add(VGroup(dibujo, VGroup(rotulo, detalle)
                               .arrange(DOWN, buff=0.1)
                               ).arrange(DOWN, buff=0.3))
        paneles.arrange(RIGHT, buff=0.35).scale_to_fit_width(13.7)
        self.add(paneles)
