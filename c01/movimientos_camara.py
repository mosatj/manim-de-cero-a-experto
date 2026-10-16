from manim import *

INICIO, FINAL = GREY_B, RED_C  # marco al empezar y al terminar


def mundo():
    """Lo que hay delante de la cámara: tres figuras sencillas."""
    return VGroup(
        Circle(radius=0.32, color=BLUE, fill_opacity=0.6),
        Square(side_length=0.6, color=TEAL, fill_opacity=0.6),
        Triangle(color=GREEN, fill_opacity=0.6).scale(0.38),
    ).arrange(RIGHT, buff=0.45)


def marco(ancho, tono, discontinuo=False):
    rect = Rectangle(width=ancho, height=ancho * 9 / 16, color=tono,
                     stroke_width=4)
    return DashedVMobject(rect, num_dashes=40) if discontinuo else rect


def flecha(desde, hasta):
    return Arrow(desde, hasta, buff=0.05, color=FINAL, stroke_width=4,
                 max_tip_length_to_length_ratio=0.3)


def panel(nombre, api, *piezas):
    # Cada dibujo ocupa una caja del mismo tamaño: las filas se alinean
    caja = Rectangle(width=4.0, height=2.3, stroke_opacity=0)
    dibujo = VGroup(*piezas)
    dibujo.scale_to_fit_height(min(dibujo.height, 2.1))
    dibujo.scale_to_fit_width(min(dibujo.width, 3.9)).move_to(caja)
    rotulo = Text(nombre, font_size=28)
    codigo = Text(api, font_size=20, color=GREY_B, font="Monospace")
    VGroup(rotulo, codigo).arrange(DOWN, buff=0.12).next_to(
        caja, DOWN, buff=0.15)
    return VGroup(caja, dibujo, rotulo, codigo)


class MovimientosCamara(Scene):
    def construct(self):
        # 1. Paneo o travelling: el marco se desliza de lado
        m1 = marco(1.9, INICIO).move_to(mundo()[0])
        m2 = marco(1.9, FINAL, True).move_to(mundo()[2])
        p1 = panel("paneo / travelling", "frame.animate.shift(RIGHT)",
                   mundo(), m1, m2, flecha(m1.get_top() + UP * 0.15,
                                           m2.get_top() + UP * 0.15))
        # 2. Inclinación: el marco sube o baja
        alto = VGroup(mundo(), mundo().shift(UP * 1.1)).move_to(ORIGIN)
        m1 = marco(2.6, INICIO).move_to(alto[0])
        m2 = marco(2.6, FINAL, True).move_to(alto[1])
        p2 = panel("inclinación", "frame.animate.shift(UP)", alto, m1,
                   m2, flecha(m1.get_right() + RIGHT * 0.2,
                              m2.get_right() + RIGHT * 0.2))
        # 3. Zoom (acercar): el marco se encoge sobre un detalle
        m1 = marco(3.0, INICIO)
        m2 = marco(1.1, FINAL, True).move_to(mundo()[1])
        p3 = panel("zoom (acercar)", "frame.animate.scale(0.4)",
                   mundo(), m1, m2,
                   flecha(m1.get_corner(UL), m2.get_corner(UL)),
                   flecha(m1.get_corner(DR), m2.get_corner(DR)))
        # 4. Giro (alabeo): el marco rota sobre su centro
        m1 = marco(2.6, INICIO)
        m2 = marco(2.6, FINAL, True).rotate(20 * DEGREES)
        giro = CurvedArrow(m1.get_corner(UR) + UP * 0.1,
                           m2.get_corner(UR) + UP * 0.25 + RIGHT * 0.1,
                           color=FINAL, angle=-PI / 3)
        p4 = panel("giro", "frame.animate.rotate(PI/9)", mundo(), m1,
                   m2, giro)
        # 5. Seguimiento: el marco acompaña a un objeto que se mueve
        camino = ArcBetweenPoints(LEFT * 1.4, RIGHT * 1.4, angle=-PI / 2,
                                  color=GREY_C)
        bola = Dot(camino.point_from_proportion(0.75), color=BLUE,
                   radius=0.12)
        m1 = marco(1.2, INICIO).move_to(camino.point_from_proportion(0.25))
        m2 = marco(1.2, FINAL, True).move_to(bola)
        p5 = panel("seguimiento", "add_updater(...)", camino, bola, m1,
                   m2, Dot(m1.get_center(), color=GREY_B, radius=0.08))
        # 6. Órbita (3D): la cámara gira alrededor de los objetos
        cubo = Square(side_length=0.8, color=BLUE, fill_opacity=0.5)
        tapa = cubo.copy().shift(UR * 0.3).set_fill(opacity=0.25)
        aristas = VGroup(*[Line(cubo.get_corner(d), tapa.get_corner(d),
                                color=BLUE) for d in (UL, UR, DL, DR)])
        orbita = Ellipse(width=3.2, height=1.7, color=FINAL)
        orbita.move_to(cubo.get_center() + UR * 0.15)
        camara = VGroup(Square(side_length=0.3, color=FINAL,
                               fill_opacity=1),
                        Triangle(color=FINAL, fill_opacity=1).scale(0.14)
                        .rotate(-PI / 2).shift(RIGHT * 0.22))
        camara.move_to(orbita.point_from_proportion(0.75))
        p6 = panel("órbita (3D)", "move_camera(theta=...)", cubo, tapa,
                   aristas, orbita, camara)

        paneles = VGroup(p1, p2, p3, p4, p5, p6)
        paneles.arrange_in_grid(rows=2, cols=3, buff=(0.5, 0.45))
        paneles.scale(min(13.4 / paneles.width, 7.6 / paneles.height))
        self.add(paneles)
