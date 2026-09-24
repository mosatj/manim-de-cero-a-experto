from manim import *


def acelera_y_frena(t):
    # 3t^2 - 2t^3: f(0) = 0, f(1) = 1 y velocidad nula en ambos
    return 3 * t**2 - 2 * t**3


class RitmoPropio(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 1, 0.25], y_range=[0, 1, 0.25],
                    x_length=5.5, y_length=5.5, tips=False)
        ejes.to_edge(LEFT)
        rotulos = ejes.get_axis_labels(MathTex("t"),
                                       MathTex("f(t)"))
        comprimida = squish_rate_func(acelera_y_frena, 0.3, 0.7)
        curvas = VGroup(ejes.plot(linear, color=GRAY),
                        ejes.plot(acelera_y_frena, color=YELLOW),
                        ejes.plot(comprimida, color=BLUE))
        self.add(ejes, rotulos)
        self.play(Create(curvas), rate_func=linear)
        # Las mismas funciones como rate_func de dos animaciones
        casos = [(acelera_y_frena, YELLOW, "acelera_y_frena"),
                 (comprimida, BLUE, "squish_rate_func(…)")]
        for k, (ritmo, color, nombre) in enumerate(casos):
            carril = Line(ORIGIN, 5 * RIGHT, color=GRAY_D)
            carril.move_to(3.4 * RIGHT + (1.2 - 2 * k) * UP)
            texto = Text(nombre, font="Menlo", font_size=22,
                         color=color).next_to(carril, UP)
            punto = Dot(carril.get_start(), color=color)
            self.add(carril, texto)
            self.play(punto.animate.move_to(carril.get_end()),
                      rate_func=ritmo, run_time=2)
