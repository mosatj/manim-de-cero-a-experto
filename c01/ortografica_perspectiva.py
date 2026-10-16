from manim import *

# Cuatro cubos en fila que se alejan de la cámara (eje z negativo)
VERTICES = [np.array([x, y, z]) for x in (0, 1) for y in (0, 1)
            for z in (0, -1)]
ARISTAS = [(i, j) for i in range(8) for j in range(i + 1, 8)
           if np.sum(np.abs(VERTICES[i] - VERTICES[j])) == 1]
GIRO = rotation_matrix(-42 * DEGREES, UP) @ rotation_matrix(
    18 * DEGREES, RIGHT)  # mirar la fila un poco desde arriba y de lado


def proyectar(p, distancia=None):
    q = GIRO @ p
    if distancia is None:  # ortográfica: se descarta la profundidad
        return np.array([q[0], q[1], 0])
    factor = distancia / (distancia - q[2])  # perspectiva: lo lejano encoge
    return np.array([q[0] * factor, q[1] * factor, 0])


def fila_de_cubos(distancia=None):
    grupo = VGroup()
    for k in range(4):
        desplazamiento = np.array([-0.5, -0.5, -2.0 * k])
        tono = interpolate_color(BLUE, GREY_B, k / 3)
        for i, j in ARISTAS:
            a = proyectar(VERTICES[i] + desplazamiento, distancia)
            b = proyectar(VERTICES[j] + desplazamiento, distancia)
            grupo.add(Line(a, b, color=tono, stroke_width=4))
    return grupo


def fugas(distancia):
    """Prolonga las cuatro aristas de profundidad del primer cubo hasta
    el punto de fuga: la proyección de un punto infinitamente lejano."""
    g = GIRO @ np.array([0, 0, -1.0])
    fuga = np.array([distancia * g[0] / -g[2], distancia * g[1] / -g[2], 0])
    esquinas = [np.array([x, y, 0]) - np.array([0.5, 0.5, 0])
                for x in (0, 1) for y in (0, 1)]
    lineas = VGroup(*[DashedLine(proyectar(e, distancia), fuga,
                                 color=RED_C, stroke_width=2)
                      for e in esquinas])
    return VGroup(lineas, Dot(fuga, color=RED_C, radius=0.07))


class OrtograficaPerspectiva(Scene):
    def construct(self):
        orto = fila_de_cubos().scale(0.75)
        persp = VGroup(fila_de_cubos(distancia=4.0), fugas(4.0))
        persp.scale_to_fit_width(5.6)
        for dibujo, x in ((orto, -3.6), (persp, 3.6)):
            dibujo.move_to([x, 0.5, 0])
        titulos = VGroup(
            Text("ortográfica (sin profundidad)", font_size=28),
            Text("perspectiva (cámara 3D)", font_size=28))
        notas = VGroup(
            Text("Mismo tamaño a cualquier distancia;\n"
                 "las paralelas siguen paralelas.",
                 font_size=22, color=GREY_B, line_spacing=0.9),
            Text("Lo lejano se achica y las paralelas\n"
                 "convergen hacia un punto de fuga.",
                 font_size=22, color=GREY_B, line_spacing=0.9))
        for dibujo, titulo, nota in zip((orto, persp), titulos, notas):
            titulo.next_to(dibujo, UP, buff=0.4)
            nota.next_to(dibujo, DOWN, buff=0.4)
        separador = DashedLine(UP * 3.6, DOWN * 3.6, color=GREY_D)
        self.add(orto, persp, titulos, notas, separador)
