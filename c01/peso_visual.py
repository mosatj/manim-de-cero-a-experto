from manim import *

# Franja apaisada: tres marcos 16:9 en fila, cada uno sobre su balanza
config.frame_height = 4.6
config.pixel_height = round(config.pixel_width * 4.6 / config.frame_width)

ANCHO, ALTO = 4.2, 4.2 * 9 / 16


def pieza(forma, x, y, opacidad, color):
    """Un elemento con su «masa visual»: área (caja) por contraste."""
    forma.set_fill(color, opacity=opacidad).set_stroke(width=0)
    forma.move_to([x, y, 0])
    forma.masa = forma.width * forma.height * opacidad
    return forma


def barras(lineas, ancho):
    """Un párrafo esquemático: barras grises en lugar de letras."""
    return VGroup(*[RoundedRectangle(corner_radius=0.04, height=0.09,
                                     width=ancho * (0.6 if k == lineas - 1
                                                    else 1))
                    for k in range(lineas)]).arrange(DOWN, buff=0.09,
                                                     aligned_edge=LEFT)


def balanza(piezas):
    """Barra con el fulcro en el centro del marco. Se inclina hacia el
    centro de masas visual: x_media = suma(m * x) / suma(m)."""
    total = sum(p.masa for p in piezas)
    x_media = sum(p.masa * p.get_x() for p in piezas) / total
    x_media = 0.0 if abs(x_media) < 0.005 else x_media
    giro = -0.12 * x_media                 # inclinación proporcional
    barra = Line(LEFT * ANCHO / 2, RIGHT * ANCHO / 2, color=GREY_B,
                 stroke_width=6).rotate(giro)
    fulcro = Triangle(color=GREY_B, fill_opacity=1).scale(0.16)
    fulcro.next_to(ORIGIN, DOWN, buff=0.03)
    marca = Dot(x_media * np.array([np.cos(giro), np.sin(giro), 0]),
                radius=0.09, color=RED_C)
    return VGroup(barra, fulcro, marca), x_media


def panel(piezas, nombre):
    marco = Rectangle(width=ANCHO, height=ALTO, color=GREY_C,
                      stroke_width=3)
    eje = DashedLine(UP * ALTO / 2, DOWN * ALTO / 2, dash_length=0.08)
    dibujo = VGroup(marco, eje.set_stroke(GREY_C, 2), *piezas)
    aparato, x_media = balanza(piezas)
    aparato.next_to(marco, DOWN, buff=0.35)
    rotulo = Text(nombre, font_size=30)
    valor = MathTex(r"\bar x = " + f"{x_media:.2f}".replace(".", "{,}"),
                    font_size=34, color=GREY_B)
    return VGroup(dibujo, aparato, VGroup(rotulo, valor)
                  .arrange(RIGHT, buff=0.3)).arrange(DOWN, buff=0.25)


class PesoVisual(Scene):
    def construct(self):
        # (a) Simétrico: todo el peso sobre el eje central
        simetrico = [pieza(Circle(radius=0.5), 0, -0.2, 0.85, RED_C),
                     pieza(barras(2, 1.4), 0, 0.75, 1, GREY_B)]
        # (b) Desequilibrado: protagonista y texto en el mismo lado
        cargado = [pieza(Circle(radius=0.5), 1.3, -0.3, 0.85, RED_C),
                   pieza(barras(3, 1.2), 1.25, 0.7, 1, GREY_B)]
        # (c) Asimétrico en equilibrio: lo pequeño e intenso, lejos;
        # lo grande y tenue, cerca del centro, donde lo pide la palanca
        chico = pieza(Circle(radius=0.2), 1.5, 0.45, 1, RED_C)
        grande = pieza(Circle(radius=0.8), 0, -0.1, 0.2, BLUE)
        grande.set_x(-chico.masa * chico.get_x() / grande.masa)
        asimetrico = [grande, chico]

        paneles = VGroup(panel(simetrico, "simétrico"),
                         panel(cargado, "desequilibrado"),
                         panel(asimetrico, "asimétrico"))
        paneles.arrange(RIGHT, buff=0.35, aligned_edge=UP)
        paneles.scale_to_fit_width(13.7).move_to(ORIGIN)
        self.add(paneles)
