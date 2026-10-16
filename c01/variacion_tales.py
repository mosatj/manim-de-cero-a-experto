from manim import *

# Franja apaisada: cuatro casos del teorema de Tales en fila
config.frame_height = 4.2
config.pixel_height = round(config.pixel_width * 4.2 / config.frame_width)


def caso(radio, giro, t, distancia=1.0):
    """Triángulo con la base en un diámetro y el tercer vértice en el
    ángulo t (radianes). Con distancia < 1, el vértice queda dentro del
    círculo. Devuelve el dibujo y el ángulo en el vértice, en grados."""
    a, b = LEFT * radio, RIGHT * radio
    c = distancia * radio * np.array([np.cos(t), np.sin(t), 0])
    semicirculo = Arc(radius=radio, angle=PI, color=GREY_B,
                      stroke_width=3)
    triangulo = Polygon(a, c, b, color=BLUE, stroke_width=5,
                        fill_opacity=0.15)
    lado_a, lado_b = Line(c, a), Line(c, b)
    u, v = normalize(a - c), normalize(b - c)
    grados = np.degrees(np.arccos(np.dot(u, v)))
    if abs(grados - 90) < 0.5:
        marca = RightAngle(lado_a, lado_b, length=0.24, color=RED_C,
                           stroke_width=4)
    else:
        marca = Angle(lado_a, lado_b, radius=0.32, color=RED_C,
                      stroke_width=4)
    vertice = Dot(c, radius=0.07, color=RED_C)
    dibujo = VGroup(semicirculo, triangulo, marca, vertice)
    return dibujo.rotate(giro, about_point=ORIGIN), grados


class VariacionTales(Scene):
    def construct(self):
        # Varía lo accesorio (tamaño, giro, posición del vértice) y
        # conserva la relación; el último caso rompe una condición
        datos = [(1.3, 0, 2.2, 1.0), (1.0, 25 * DEGREES, 1.0, 1.0),
                 (1.5, -10 * DEGREES, 1.7, 1.0), (1.3, 0, 1.9, 0.6)]
        casos = VGroup()
        for radio, giro, t, distancia in datos:
            dibujo, grados = caso(radio, giro, t, distancia)
            valor = MathTex(f"{grados:.0f}" + r"^\circ", font_size=40,
                            color=RED_C)
            nota = Text("en el círculo" if distancia == 1 else
                        "vértice dentro", font_size=28, color=GREY_B)
            casos.add(VGroup(dibujo, valor, nota).arrange(DOWN,
                                                          buff=0.2))
        casos.arrange(RIGHT, buff=0.6, aligned_edge=DOWN)
        casos.scale_to_fit_width(13.4).move_to(ORIGIN)
        self.add(casos)
