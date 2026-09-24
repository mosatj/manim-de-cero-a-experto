from manim import *
from metodos_edo import euler, heun, rk4, resolver, f, exacta


class ErroresLogLog(Scene):
    def construct(self):
        # Escala log: x_range e y_range son EXPONENTES de 10
        ejes = Axes(
            x_range=[-3, 0, 1], y_range=[-14, 0, 2],
            x_length=7.5, y_length=6.3, tips=False,
            x_axis_config={"scaling": LogBase(), "font_size": 24},
            y_axis_config={"scaling": LogBase(), "font_size": 24},
        ).add_coordinates().to_edge(LEFT, buff=0.9)
        rotulos = ejes.get_axis_labels(MathTex("h"),
                                       Tex("error en $t=2$"))
        self.add(ejes, rotulos)
        pasos = 2 / 2.0 ** np.arange(2, 11)       # de 1/2 a 1/512
        leyenda = VGroup()
        for metodo, nombre, p, tono in ((euler, "Euler", 1, YELLOW),
                                         (heun, "Heun", 2, GREEN),
                                         (rk4, "RK4", 4, RED)):
            errores = [abs(resolver(metodo, f, 0.0, 0.5, h,
                                    round(2/h))[1][-1] - exacta(2))
                       for h in pasos]
            puntos = ejes.c2p(np.column_stack([pasos, errores]))
            linea = VMobject(color=tono)
            linea.set_points_as_corners(puntos)
            nodos = VGroup(*[Dot(q, radius=0.05, color=tono)
                             for q in puntos])
            self.play(Create(linea), FadeIn(nodos))
            leyenda.add(Tex(f"{nombre}: pendiente {p}", color=tono,
                            font_size=34))
        self.play(Write(leyenda.arrange(DOWN, aligned_edge=LEFT)
                        .to_edge(RIGHT, buff=0.4)))
