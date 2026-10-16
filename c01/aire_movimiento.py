from manim import *

# Franja apaisada: dos marcos 16:9, «antes» y «después»
config.frame_height = 4.6
config.pixel_height = round(config.pixel_width * 4.6 / config.frame_width)

ANCHO, ALTO = 6.3, 6.3 * 9 / 16


def trayectoria(x):
    """La curva que recorre el punto, en coordenadas del marco."""
    return 0.55 * np.sin(1.1 * x) - 0.15


def panel(x_punto, nombre):
    marco = Rectangle(width=ANCHO, height=ALTO, color=GREY_C,
                      stroke_width=3)
    izquierda = -ANCHO / 2 + 0.15
    # Lo recorrido queda como estela; lo que falta, como una guía tenue
    estela = FunctionGraph(trayectoria, x_range=[izquierda, x_punto],
                           color=BLUE, stroke_width=6)
    resto = DashedVMobject(FunctionGraph(
        trayectoria, x_range=[x_punto, ANCHO / 2 - 0.15]), num_dashes=24)
    resto.set_stroke(GREY_C, 2)
    punto = Dot([x_punto, trayectoria(x_punto), 0], radius=0.13,
                color=RED_C)
    # Flecha de velocidad: tangente a la curva en el punto
    pendiente = 0.55 * 1.1 * np.cos(1.1 * x_punto)
    direccion = normalize(np.array([1, pendiente, 0]))
    flecha = Arrow(punto.get_center(), punto.get_center() + 1.1 * direccion,
                   buff=0, color=RED_C, stroke_width=6)
    # El «aire»: distancia libre entre el punto y el borde hacia el que va
    aire = DoubleArrow([x_punto, -ALTO / 2 + 0.3, 0],
                       [ANCHO / 2, -ALTO / 2 + 0.3, 0], buff=0,
                       color=GREY_B, stroke_width=3, tip_length=0.18)
    etiqueta = Text("aire", font_size=28, color=GREY_B)
    etiqueta.next_to(aire, UP, buff=0.08)
    if aire.get_length() < etiqueta.width + 0.3:
        VGroup(aire, etiqueta).set_opacity(0)   # no hay aire que medir
    dibujo = VGroup(marco, resto, estela, aire, etiqueta, flecha, punto)
    rotulo = Text(nombre, font_size=30)
    return VGroup(dibujo, rotulo).arrange(DOWN, buff=0.28)


class AireMovimiento(Scene):
    def construct(self):
        antes = panel(ANCHO / 2 - 0.45,
                      "sin aire: la mirada choca con el borde")
        despues = panel(-ANCHO / 6,
                        "con aire: el movimiento tiene adónde ir")
        paneles = VGroup(antes, despues).arrange(RIGHT, buff=0.5)
        paneles.scale_to_fit_width(13.7)
        self.add(paneles)
