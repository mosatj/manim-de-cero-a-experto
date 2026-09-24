from manim import *


class VectorialVsPixeles(Scene):
    def construct(self):
        radio = 2.2
        # Izquierda: el círculo como curva matemática
        vectorial = Circle(radius=radio, color=BLUE, stroke_width=6)
        vectorial.move_to(3.5 * LEFT)
        # Derecha: el mismo círculo en una rejilla de 12 x 12
        lado = 0.4
        pixeles = VGroup()
        for i in range(-6, 6):
            for j in range(-6, 6):
                x, y = (i + 0.5) * lado, (j + 0.5) * lado
                d = np.sqrt(x**2 + y**2)  # distancia al centro
                celda = Square(side_length=lado, stroke_width=0.6,
                               stroke_color=GRAY_D)
                # se pinta si su centro cae cerca de la curva
                if abs(d - radio) < 0.55 * lado:
                    celda.set_fill(BLUE, opacity=1)
                pixeles.add(celda.move_to([x, y, 0]))
        pixeles.move_to(3.5 * RIGHT)
        rotulo_v = Text("vectorial", font_size=32)
        rotulo_p = Text("mapa de bits", font_size=32)
        rotulo_v.next_to(vectorial, DOWN)
        rotulo_p.next_to(pixeles, DOWN)
        self.add(vectorial, pixeles, rotulo_v, rotulo_p)
