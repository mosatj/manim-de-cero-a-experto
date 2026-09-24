from manim import *


class EtiquetarVertices(Scene):
    def construct(self):
        vertices = [np.array(p) for p in
                    ([-3.5, -2, 0], [3, -1.5, 0], [0.5, 2.5, 0])]
        triangulo = Polygon(*vertices, color=BLUE,
                            fill_opacity=0.25)
        centro = np.mean(vertices, axis=0)       # baricentro
        self.add(triangulo, Dot(centro, color=GRAY))
        for v, nombre in zip(vertices, "ABC"):
            hacia_fuera = normalize(v - centro)
            rotulo = MathTex(nombre, font_size=56, color=YELLOW)
            rotulo.next_to(v, hacia_fuera, buff=0.15)
            guia = DashedLine(centro, v, color=GRAY,
                              stroke_width=2)
            self.add(guia, Dot(v, color=YELLOW), rotulo)
