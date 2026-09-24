from manim import *


class EjesAnatomia(Scene):
    def construct(self):
        ejes = Axes(
            x_range=[-1, 6, 1],          # [mínimo, máximo, paso]
            y_range=[-1, 4, 1],
            x_length=9,                  # tamaño en pantalla
            y_length=5,
            axis_config={"include_numbers": True, "font_size": 28},
            tips=True,
        )
        rotulos = ejes.get_axis_labels(x_label="x", y_label="y")
        # c2p (coords_to_point) pasa de coordenadas a pantalla
        p = ejes.c2p(4, 3)
        punto = Dot(p, color=YELLOW)
        texto = MathTex(r"(4,\,3)", color=YELLOW)
        texto.next_to(punto, UR, buff=0.1)
        # El centro de la pantalla es el punto medio de los rangos
        centro = Cross(scale_factor=0.12, stroke_width=4)
        centro.move_to(ORIGIN)
        et_centro = Text("ORIGIN = c2p(2.5, 1.5)", font_size=22)
        et_centro.next_to(centro, DR, buff=0.1)
        self.add(ejes, rotulos)
        self.play(FadeIn(punto, texto, centro, et_centro))
        self.wait()
