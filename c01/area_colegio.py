from manim import *

# Franja apaisada: la figura ocupa todo el ancho de la página
config.frame_height = 4.6
config.pixel_height = round(config.pixel_width * 4.6 / config.frame_width)

COLORES = [BLUE, GREEN, RED_C]


def sector(vertice, desde, hasta, tono):
    """Ángulo pintado en el vértice, de la dirección desde a la hasta."""
    a0 = np.arctan2(*(desde - vertice)[[1, 0]])
    a1 = np.arctan2(*(hasta - vertice)[[1, 0]])
    return AnnularSector(inner_radius=0, outer_radius=0.55, start_angle=a0,
                         angle=(a1 - a0) % TAU, color=tono,
                         fill_opacity=0.8).shift(vertice)


class AreaColegio(Scene):
    def construct(self):
        a, b, c = np.array([-5.6, -1.6, 0]), np.array([-1.6, -1.6, 0]), \
            np.array([-4.2, 1.5, 0])
        triangulo = Polygon(a, b, c, color=GREY_B, stroke_width=4)
        angulos = VGroup(sector(a, b, c, COLORES[0]),
                         sector(b, c, a, COLORES[1]),
                         sector(c, a, b, COLORES[2]))
        # Los tres ángulos, «recortados» y puestos uno junto a otro
        recta = Line([0.6, -1.6, 0], [6.4, -1.6, 0], color=GREY_B,
                     stroke_width=4)
        centro = np.array([3.5, -1.6, 0])
        juntos = VGroup()
        inicio = 0
        for ang, tono in zip(angulos, COLORES):
            amplitud = ang.angle
            juntos.add(AnnularSector(inner_radius=0, outer_radius=1.6,
                                     start_angle=inicio, angle=amplitud,
                                     color=tono, fill_opacity=0.45)
                       .shift(centro))
            inicio += amplitud
        # Cada letra, en la bisectriz de su ángulo (pequeño y grande)
        letras_chicas, letras_grandes = VGroup(), VGroup()
        for sec_chico, vertice, sec_grande, letra in zip(
                angulos, (a, b, c), juntos,
                (r"\alpha", r"\beta", r"\gamma")):
            for sec, centro_sec, d, grupo in (
                    (sec_chico, vertice, 0.85, letras_chicas),
                    (sec_grande, centro, 1.05, letras_grandes)):
                medio = sec.start_angle + sec.angle / 2
                grupo.add(MathTex(letra, font_size=40).move_to(
                    centro_sec + d * np.array([np.cos(medio),
                                               np.sin(medio), 0])))
        flecha = Arrow([-1.2, 0, 0], [0.9, 0, 0], color=GREY_C)
        formula = MathTex(r"\alpha+\beta+\gamma=180^\circ",
                          font_size=52).move_to([3.5, 1.4, 0])
        self.play(Create(triangulo))
        self.play(FadeIn(angulos), Write(letras_chicas))
        self.play(GrowArrow(flecha), Create(recta))
        # Cada ángulo viaja desde su vértice hasta la recta
        for chico, grande, l_chica, l_grande in zip(
                angulos, juntos, letras_chicas, letras_grandes):
            self.play(TransformFromCopy(chico, grande),
                      TransformFromCopy(l_chica, l_grande), run_time=1.2)
        self.play(Write(formula))
        self.wait()
