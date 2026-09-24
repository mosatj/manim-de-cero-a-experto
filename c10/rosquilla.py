from manim import *


class Rosquilla(Scene):
    def construct(self):
        datos = {"Cálculo": 35, "Álgebra": 25,
                 "Geometría": 20, "Estadística": 20}
        colores = [BLUE, GREEN, YELLOW, RED]
        total = sum(datos.values())
        inicio = PI / 2           # empezamos arriba (las 12)
        grafico, leyenda = VGroup(), VGroup()
        for (nombre, valor), color in zip(datos.items(), colores):
            angulo = -TAU * valor / total   # sentido horario
            trozo = AnnularSector(inner_radius=1.3,
                                  outer_radius=2.5, angle=angulo,
                                  start_angle=inicio, color=color)
            # Porcentaje en el punto medio angular de la corona
            medio = inicio + angulo / 2
            pos = 1.9 * np.array([np.cos(medio), np.sin(medio), 0])
            cifra = Text(f"{valor} %", font_size=30, color=BLACK)
            grafico.add(trozo, cifra.move_to(pos))
            muestra = Square(0.35, fill_color=color,
                             fill_opacity=1, stroke_width=0)
            leyenda.add(VGroup(muestra, Text(nombre, font_size=30))
                        .arrange(RIGHT))
            inicio += angulo
        leyenda.arrange(DOWN, aligned_edge=LEFT)
        VGroup(grafico, leyenda).arrange(RIGHT, buff=1.2)
        self.add(grafico, leyenda)
