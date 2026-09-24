from manim import *


class VentanaPeriodo3(Scene):
    def construct(self):
        r = np.linspace(3.82, 3.87, 900)
        x = np.full(r.shape, 0.5)
        for _ in range(1500):          # transitorio largo: cerca de
            x = r * x * (1 - x)        # 3.8284 la convergencia
        pares = []                     # es lenta
        for _ in range(150):
            x = r * x * (1 - x)
            pares.append(np.column_stack([r, x, 0 * r]))
        datos = np.vstack(pares)
        ejes = Axes(x_range=[3.82, 3.87, 0.01], y_range=[0, 1, 0.2],
                    x_length=12, y_length=6.5, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 22,
                                 "decimal_number_config":
                                     {"num_decimal_places": 2}})
        nube = PMobject(stroke_width=1)
        nube.add_points(ejes.c2p(datos), color=WHITE)
        r3 = 1 + np.sqrt(8)            # nace el ciclo de periodo 3
        marca = ejes.get_vertical_line(ejes.c2p(r3, 1), color=RED)
        rot = MathTex(r"1+\sqrt{8}", color=RED, font_size=30)
        self.add(ejes, nube)
        self.play(Create(marca),
                  Write(rot.next_to(marca, UP, buff=0.1)))
