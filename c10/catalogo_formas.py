from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class CatalogoFormas(Scene):
    def construct(self):
        p, q = LEFT + 0.3 * DOWN, RIGHT + 0.3 * UP  # dos puntos
        formas = [
            ("Dot", Dot(radius=0.15)),
            ("Line", Line(p, q)),
            ("DashedLine", DashedLine(p, q)),
            ("Arrow", Arrow(p, q, buff=0)),
            ("DoubleArrow", DoubleArrow(p, q, buff=0)),
            ("CurvedArrow", CurvedArrow(p, q)),
            ("Arc", Arc(radius=0.7, angle=PI)),
            ("ArcBetweenPoints", ArcBetweenPoints(p, q)),
            ("Circle", Circle(0.6)),
            ("Ellipse", Ellipse(width=1.8, height=1)),
            ("Annulus", Annulus(0.3, 0.6)),
            ("Sector", Sector(radius=0.7, angle=2)),
            ("AnnularSector", AnnularSector(0.3, 0.7, angle=4)),
            ("Square", Square(1.1)),
            ("Rectangle", Rectangle(width=1.8, height=1)),
            ("RoundedRectangle", RoundedRectangle(
                corner_radius=0.3, width=1.8, height=1)),
            ("Triangle", Triangle()),
            ("RegularPolygon", RegularPolygon(6).scale(0.6)),
            ("Star", Star(outer_radius=0.7)),
            ("Polygon", Polygon(p, q, 0.8 * DOWN + 0.5 * RIGHT)),
            ("Elbow", Elbow(width=0.6)),
            ("CubicBezier", CubicBezier(p, UP, DOWN, q)),
            ("ArcPolygon", ArcPolygon(p, q, 0.8 * (UP + LEFT))),
            ("ConvexHull", ConvexHull(*[
                [np.cos(k), np.sin(2 * k) / 2, 0]
                for k in range(8)])),
        ]
        celdas = VGroup()
        colores = color_gradient([BLUE, GREEN, YELLOW, RED], 24)
        for (nombre, forma), color in zip(formas, colores):
            forma.set_color(color)
            # Que cada forma quepa en su celda de 2.35 × 1.9
            if forma.width > 1.8:
                forma.scale_to_fit_width(1.8)
            if forma.height > 1.1:
                forma.scale_to_fit_height(1.1)
            forma.move_to(ORIGIN)
            caja = Rectangle(width=2.35, height=1.9).set_stroke(
                GRAY, 1, 0.4)
            rotulo = Text(nombre, font_size=24)
            rotulo.set(width=min(rotulo.width, 2.25))
            rotulo.next_to(caja.get_bottom(), UP, buff=0.12)
            celdas.add(VGroup(caja, forma.shift(0.2 * UP), rotulo))
        celdas.arrange_in_grid(rows=4, cols=6, buff=0)
        self.add(celdas)
