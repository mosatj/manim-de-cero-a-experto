from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class ArcosSectores(Scene):
    def construct(self):
        # Arc: start_angle y angle, medidos desde el eje x
        arco = Arc(radius=2, start_angle=PI / 6, angle=PI / 2,
                   color=YELLOW, stroke_width=8)
        radios = VGroup(
            DashedLine(ORIGIN, 2.3 * RIGHT),
            Line(ORIGIN, arco.get_start()),
            Line(ORIGIN, arco.get_end())).set_color(GRAY)
        a1 = Arc(radius=0.7, angle=PI / 6, color=BLUE)
        a2 = Arc(radius=1.1, start_angle=PI / 6, angle=PI / 2,
                 color=RED)
        r1 = Text("start_angle", font_size=24, color=BLUE)
        r1.next_to(a1, RIGHT, buff=0.15)
        r2 = Text("angle", font_size=24, color=RED)
        r2.move_to(1.5 * rotate_vector(RIGHT, 80 * DEGREES))
        arcos = VGroup(radios, arco, a1, a2, r1, r2)
        # ArcBetweenPoints: el mismo par de puntos, varios ángulos
        p, q = LEFT * 1.5, RIGHT * 1.5
        entre = VGroup(Dot(p), Dot(q))
        for ang, c in [(PI / 3, BLUE), (2 * PI / 3, GREEN),
                       (PI, YELLOW), (-PI / 2, RED)]:
            entre.add(ArcBetweenPoints(p, q, angle=ang, color=c))
        # Los tres «parientes» rellenos del arco
        sector = Sector(radius=1.2, angle=2 * PI / 3, color=BLUE)
        anular = AnnularSector(inner_radius=0.6, outer_radius=1.2,
                               angle=4 * PI / 3, color=GREEN)
        corona = Annulus(inner_radius=0.6, outer_radius=1.2,
                         color=RED)
        formas = [arcos, entre, sector, anular, corona]
        nombres = ["Arc", "ArcBetweenPoints", "Sector",
                   "AnnularSector", "Annulus"]
        celdas = VGroup()
        for forma, t in zip(formas, nombres):
            texto = Text(t, font_size=26).next_to(forma, DOWN)
            celdas.add(VGroup(forma, texto))
        arriba = VGroup(*celdas[:2]).arrange(RIGHT, buff=1.5)
        abajo = VGroup(*celdas[2:]).arrange(RIGHT, buff=1)
        VGroup(arriba, abajo).arrange(DOWN, buff=0.6)
        self.add(arriba, abajo)
