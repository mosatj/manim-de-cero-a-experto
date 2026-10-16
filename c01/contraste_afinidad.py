from manim import *

# Franja apaisada: tres planos de una misma historia y, debajo, su curva
# de intensidad visual
config.frame_height = 5.4
config.pixel_height = round(config.pixel_width * 5.4 / config.frame_width)

ANCHO, ALTO = 4.2, 4.2 * 9 / 16


def f(x):
    return 0.35 * x**2


def plano(x0, x1, contraste):
    """Una secante de la parábola entre x0 y x1 (tangente si x0 == x1).
    contraste va de 0 (todo afín) a 1 (todo contrastado)."""
    marco = Rectangle(width=ANCHO, height=ALTO, color=GREY_C,
                      stroke_width=3)
    ejes = Axes(x_range=[-2.6, 2.6], y_range=[-0.4, 2.4], x_length=3.9,
                y_length=2.1, tips=False)
    # Con afinidad, ejes y curva comparten tono y grosor; con contraste,
    # el contexto se apaga y la recta protagonista se enciende
    ejes.set_stroke(GREY_B if contraste < 1 else GREY_D,
                    3 - 1.5 * contraste)
    curva = ejes.plot(f, x_range=[-2.5, 2.5],
                      color=GREY_B if contraste == 0 else BLUE,
                      stroke_width=3 + 2 * contraste)
    if x0 == x1:
        pendiente = 2 * 0.35 * x0          # f'(x0)
        puntos = [x0]
    else:
        pendiente = (f(x1) - f(x0)) / (x1 - x0)
        puntos = [x0, x1]

    def recta(x):
        return f(x0) + pendiente * (x - x0)

    tono = [GREY_B, TEAL_C, RED_C][round(2 * contraste)]
    linea = ejes.plot(recta, x_range=[-2.5, 2.5], color=tono,
                      stroke_width=3 + 4 * contraste)
    linea.set_points(linea.get_subcurve(*[
        np.clip(a, 0, 1) for a in recorte(ejes, recta)]).points)
    marcas = VGroup(*[Dot(ejes.c2p(x, f(x)), color=tono,
                          radius=0.06 + 0.06 * contraste) for x in puntos])
    dibujo = VGroup(ejes, curva, linea, marcas)
    if contraste == 1:
        # Triángulo de pendiente: la forma más dinámica, en el clímax
        a, b = ejes.c2p(x0 - 0.6, recta(x0 - 0.6)), ejes.c2p(x0, f(x0))
        dibujo.add(Polygon(a, [b[0], a[1], 0], b, stroke_width=0,
                           fill_color=RED_C, fill_opacity=0.35))
    return VGroup(marco, dibujo.move_to(marco))


def recorte(ejes, recta):
    """Fracciones de la recta que quedan dentro del rango vertical."""
    xs = np.linspace(-2.5, 2.5, 201)
    dentro = [x for x in xs if -0.4 <= recta(x) <= 2.4]
    return (dentro[0] + 2.5) / 5, (dentro[-1] + 2.5) / 5


class ContrasteAfinidad(Scene):
    def construct(self):
        etapas = [(-1.5, 1.5, 0, "afinidad", "horizontales, un solo tono"),
                  (0.3, 2.0, 0.5, "progresión", "la recta se inclina"),
                  (1.6, 1.6, 1, "contraste", "diagonal, color, triángulo")]
        columnas = VGroup()
        for x0, x1, c, nombre, nota in etapas:
            textos = VGroup(Text(nombre, font_size=30),
                            Text(nota, font_size=28, color=GREY_B))
            columnas.add(VGroup(plano(x0, x1, c), textos.arrange(
                DOWN, buff=0.1)).arrange(DOWN, buff=0.22))
        columnas.arrange(RIGHT, buff=0.35)

        # La curva de intensidad de Block: sube con el contraste
        base = columnas.get_bottom()[1] - 1.05
        alturas = [0.15, 0.4, 0.85]
        nodos = [[col.get_x(), base + h, 0]
                 for col, h in zip(columnas, alturas)]
        curva = VMobject(color=RED_C, stroke_width=5)
        curva.set_points_smoothly([[columnas.get_left()[0], base + 0.05,
                                    0], *nodos,
                                   [columnas.get_right()[0], base + 0.5,
                                    0]])
        suelo = Line([columnas.get_left()[0], base, 0],
                     [columnas.get_right()[0], base, 0], color=GREY_C,
                     stroke_width=2)
        hitos = VGroup(*[Dot(p, color=RED_C, radius=0.07) for p in nodos])
        nombre = Text("intensidad visual", font_size=28, color=GREY_B)
        nombre.next_to(suelo, DOWN, buff=0.1).align_to(suelo, LEFT)
        todo = VGroup(columnas, suelo, curva, hitos, nombre)
        todo.scale_to_fit_width(13.7).move_to(ORIGIN)
        self.add(todo)
