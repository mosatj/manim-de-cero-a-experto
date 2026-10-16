from manim import *

# Línea del tiempo de la animación, de la fotografía secuencial a Manim.
# (año, texto en dos líneas, época)
HITOS = [
    (1878, "Muybridge:\nel caballo en galope", 0),
    (1908, "Cohl:\nFantasmagorie", 0),
    (1937, "Disney:\nBlancanieves", 0),
    (1961, "Whitney:\nCatalog (analógico)", 1),
    (1963, "Sutherland: Sketchpad;\nZajac: filme en Bell Labs", 1),
    (1972, "Catmull y Parke:\nuna mano en 3D", 1),
    (1974, "Foldès: Hunger,\nclaves interpoladas", 1),
    (1982, "Disney:\nTron", 1),
    (1986, "Pixar:\nLuxo Jr.", 2),
    (1995, "Pixar:\nToy Story", 2),
    (1996, "Flash: vectores\nanimados en la web", 2),
    (2002, "Blender se\nvuelve libre", 2),
    (2015, "Sanderson:\n3Blue1Brown y Manim", 3),
    (2020, "nace\nManim Community", 3),
]
EPOCAS = [("antes de la computadora", GREY_B),
          ("pioneros digitales", TEAL_C),
          ("industria y web", BLUE_C),
          ("matemática animada", RED_C)]


def fila(hitos, y, ancho=13.4):
    paso = ancho / len(hitos)
    grupo = VGroup()
    eje = Line([-ancho / 2, y, 0], [ancho / 2, y, 0], color=GREY_C,
               stroke_width=3)
    grupo.add(eje)
    for k, (anio, texto, epoca) in enumerate(hitos):
        x = -ancho / 2 + paso * (k + 0.5)
        tono = EPOCAS[epoca][1]
        punto = Dot([x, y, 0], radius=0.1, color=tono)
        lado = UP if k % 2 == 0 else DOWN  # alterna para ganar espacio
        cifra = Text(str(anio), font_size=28, weight=BOLD, color=tono)
        rotulo = VGroup(*[Text(linea, font_size=19)
                          for linea in texto.splitlines()])
        rotulo.arrange(DOWN, buff=0.07)  # líneas centradas
        bloque = VGroup(cifra, rotulo).arrange(DOWN, buff=0.08)
        bloque.next_to(punto, lado, buff=0.22)
        palito = Line(punto.get_center(), bloque.get_edge_center(-lado),
                      color=tono, stroke_width=2)
        grupo.add(palito, punto, bloque)
    return grupo


class LineaTiempo(Scene):
    def construct(self):
        arriba = fila(HITOS[:7], 1.55)
        abajo = fila(HITOS[7:], -2.2)
        leyenda = VGroup(*[
            VGroup(Square(side_length=0.22, color=tono, fill_opacity=1),
                   Text(nombre, font_size=22)).arrange(RIGHT, buff=0.12)
            for nombre, tono in EPOCAS]).arrange(RIGHT, buff=0.5)
        leyenda.to_edge(UP, buff=0.15)
        self.add(arriba, abajo, leyenda)
