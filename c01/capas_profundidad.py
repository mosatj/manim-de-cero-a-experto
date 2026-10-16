from manim import *

# Franja apaisada: el mismo contenido en un solo plano y en tres capas,
# y la velocidad de cada capa cuando la cámara se desplaza (travelling)
config.frame_height = 3.9
config.pixel_height = round(config.pixel_width * 3.9 / config.frame_width)

ANCHO, ALTO = 4.2, 4.2 * 9 / 16


def contenido(capas):
    """Retícula de fondo, gráfica y ficha con la fórmula. Con capas, cada
    pieza recibe tamaño, opacidad, grosor y z_index según su distancia."""
    reticula = NumberPlane(x_range=[-4, 4, 0.5], y_range=[-2, 2, 0.5],
                           x_length=ANCHO, y_length=ALTO,
                           axis_config={"stroke_width": 0})
    ejes = Axes(x_range=[-3, 3], y_range=[-1.3, 1.3], x_length=3.4,
                y_length=1.45, tips=False).shift(DOWN * 0.2)
    curva = ejes.plot(np.sin, x_range=[-3, 3], color=BLUE)
    tarjeta = MathTex(r"y=\sin x", font_size=34)
    ficha = VGroup(SurroundingRectangle(tarjeta, buff=0.12,
                                        corner_radius=0.08), tarjeta)
    if capas:
        reticula.set_stroke(GREY_D, 1.5, opacity=0.5).set_z_index(0)
        VGroup(ejes, curva).set_z_index(1)
        ejes.set_stroke(GREY_B, 2)
        curva.set_stroke(width=6)
        ficha[0].set_fill(BLACK, 1).set_stroke(RED_C, 4)
        ficha.scale(1.15).set_z_index(2)
        # La ficha opaca tapa la retícula: la oclusión dice «está delante»
        ficha.move_to([ANCHO / 2 - 0.8, ALTO / 2 - 0.36, 0])
    else:
        reticula.set_stroke(GREY_B, 2)
        ejes.set_stroke(GREY_B, 2.5)
        curva.set_stroke(GREY_B, 2.5)
        ficha[0].set_stroke(GREY_B, 2.5)
        ficha.move_to([ANCHO / 2 - 0.75, ALTO / 2 - 0.35, 0])
    marco = Rectangle(width=ANCHO, height=ALTO, color=GREY_C,
                      stroke_width=3)
    return VGroup(reticula, ejes, curva, ficha, marco)


def paralaje():
    """Leyenda: al desplazar la cámara, lo cercano corre más."""
    filas = VGroup()
    for nombre, factor, tono in (("primer plano", 1, RED_C),
                                 ("plano medio", 1 / 2, BLUE),
                                 ("fondo", 1 / 4, GREY_C)):
        flecha = Arrow(ORIGIN, RIGHT * 2.0 * factor, buff=0, color=tono,
                       stroke_width=6, max_tip_length_to_length_ratio=0.5)
        texto = Text(nombre, font_size=28)
        filas.add(VGroup(texto, flecha).arrange(RIGHT, buff=0.25))
    filas.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
    return filas


class CapasProfundidad(Scene):
    def construct(self):
        plano = contenido(False)
        capas = contenido(True)
        rotulos = ["un solo plano", "tres capas"]
        paneles = VGroup(*[VGroup(p, Text(r, font_size=30)).arrange(
            DOWN, buff=0.25) for p, r in zip((plano, capas), rotulos)])
        leyenda = VGroup(paralaje(), Text("velocidad en un travelling",
                                          font_size=30)).arrange(
            DOWN, buff=0.4)
        todo = VGroup(*paneles, leyenda).arrange(RIGHT, buff=0.45)
        todo.scale_to_fit_width(13.7).move_to(ORIGIN)
        self.add(todo)
