from manim import *


def celda(funcion, nombre, ancho=2.5, alto=1.3):
    """Gráfica de una función de ritmo en una caja [0,1] x [-0.65, 1.45]."""
    def a_escena(t, y):
        return np.array([ancho * t, alto * (y + 0.65) / 2.1, 0])
    marco = Rectangle(width=ancho, height=alto, stroke_width=1,
                      stroke_color=GRAY_D).move_to(a_escena(0.5, 0.5))
    # Referencias: progreso 0 y progreso 1
    cero = DashedLine(a_escena(0, 0), a_escena(1, 0), stroke_width=1,
                      color=GRAY_C, dash_length=0.05)
    uno = DashedLine(a_escena(0, 1), a_escena(1, 1), stroke_width=1,
                     color=GRAY_C, dash_length=0.05)
    curva = ParametricFunction(lambda t: a_escena(t, funcion(t)),
                               t_range=[0, 1, 0.002], color=BLUE_B,
                               stroke_width=3)
    rotulo = Text(nombre, font="Menlo", font_size=15, color=WHITE)
    if rotulo.width > ancho:          # el nombre más largo no cabe
        rotulo.scale_to_fit_width(ancho)
    rotulo.next_to(marco, DOWN, buff=0.1)
    return VGroup(marco, cero, uno, curva, rotulo)


class RitmosManim(Scene):
    def construct(self):
        # Las 15 funciones de ritmo propias de Manim y dos envoltorios
        nombres = ["linear", "smooth", "smoothstep", "smootherstep",
                   "smoothererstep", "rush_into", "rush_from", "slow_into",
                   "double_smooth", "there_and_back",
                   "there_and_back_with_pause", "running_start", "wiggle",
                   "lingering", "exponential_decay"]
        celdas = [celda(globals()[n], n) for n in nombres]
        celdas.append(celda(not_quite_there(smooth, 0.7),
                            "not_quite_there"))
        celdas.append(celda(squish_rate_func(smooth, 0.4, 0.6),
                            "squish_rate_func"))
        rejilla = VGroup(*celdas).arrange_in_grid(rows=4, cols=5,
                                                  buff=(0.3, 0.25))
        # que quepa a lo ancho y a lo alto del fotograma
        rejilla.scale(min(13.4 / rejilla.width, 7.5 / rejilla.height))
        self.add(rejilla.move_to(ORIGIN))
