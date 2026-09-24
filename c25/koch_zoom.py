from manim import *


def koch(puntos, nivel):
    """Cambia cada segmento por los cuatro de la curva de Koch."""
    for _ in range(nivel):
        nuevos = [puntos[0]]
        for p, q in zip(puntos[:-1], puntos[1:]):
            d = (q - p) / 3
            pico = p + d + rotate_vector(d, PI / 3)
            nuevos += [p + d, pico, p + 2 * d, q]
        puntos = nuevos
    return puntos


class KochZoom(MovingCameraScene):
    def construct(self):
        marco = self.camera.frame
        ancho0 = marco.width
        S = np.array([-6.5, -1.8, 0])         # extremo izquierdo
        curva = VMobject(stroke_width=3).set_points_as_corners(
            koch([S, S + 13 * RIGHT], 6))     # 4^6 segmentos
        curva.set_color([BLUE, TEAL, YELLOW])
        self.add(curva)

        def rotulo():
            k = marco.width / ancho0          # escala del marco
            texto = MathTex(rf"\times{1 / k:.0f}", color=YELLOW)
            sitio = marco.get_corner(UL) + k * (RIGHT + DOWN)
            return texto.scale(k).move_to(sitio)

        aumento = always_redraw(rotulo)
        self.add(marco, aumento)
        self.wait()
        # El primer cuarto de la curva es toda la curva a escala 1/3
        for _ in range(2):
            centro = S + (marco.get_center() - S) / 3
            self.play(marco.animate.scale(1 / 3).move_to(centro),
                      # compensar: el trazo engorda con el zoom
                      curva.animate.set_stroke(
                          width=curva.get_stroke_width() / 3),
                      run_time=3)
