from manim import *


class GaleriaRitmos(Scene):
    def construct(self):
        ritmos = [
            linear, smooth, rush_into, rush_from,
            slow_into, double_smooth, there_and_back,
            there_and_back_with_pause, running_start,
            exponential_decay,
            lingering, rate_functions.ease_out_bounce,
        ]
        for k, funcion in enumerate(ritmos):
            fila, columna = divmod(k, 4)
            marco = Square(side_length=1.5, color=GRAY_D,
                           stroke_width=2)
            marco.move_to([-5.1 + 3.4 * columna,
                           2.6 - 2.65 * fila, 0])
            origen = marco.get_corner(DL)
            # Curva (t, f(t)) con t en [0, 1] dentro del marco
            curva = ParametricFunction(
                lambda t, f=funcion: origen
                + 1.5 * np.array([t, f(t), 0]),
                t_range=[0, 1, 0.005], color=YELLOW,
                stroke_width=3,
            )
            nombre = Text(funcion.__name__, font="Monospace",
                          font_size=17).next_to(marco, UP, 0.12)
            self.add(marco, curva, nombre)
