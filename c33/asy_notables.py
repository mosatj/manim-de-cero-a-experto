from manim import *
from asy_puente import importar_asy

AZUL, OCRE, VERDE = "#6FA3C0", "#E0B04A", "#7FB89A"
GRANATE = "#B04A5A"


class NotablesAsy(Scene):
    """geometry.asy construye; Manim lo cuenta paso a paso."""

    # (rótulo, color, primera recta, punto): índices del .asy;
    # cada paso tiene tres rectas y la letra va 3 lugares después
    PASOS = [("Medianas: baricentro G", AZUL, 4, 15),
             ("Mediatrices: circuncentro O", OCRE, 7, 16),
             ("Alturas: ortocentro H", VERDE, 11, 17)]

    def construct(self):
        fig = importar_asy("asy_notables.asy", height=7.4)
        fig.to_edge(LEFT, buff=0.5)
        for k in [1, 2, 3, 18, 19, 20]:          # etiquetas
            fig[k].set_fill("#E9F2F7")
        self.play(Create(fig[0]), Write(fig[1:4]), run_time=1.5)
        rotulo = VMobject()
        for texto, color, recta, punto in self.PASOS:
            nuevo = Text(texto, font_size=36, color=color)
            nuevo.to_corner(UR, buff=0.6)
            self.play(ReplacementTransform(rotulo, nuevo))
            rotulo = nuevo
            rectas = fig[recta:recta + 3]
            self.play(LaggedStart(*[Create(r) for r in rectas]))
            self.play(GrowFromCenter(fig[punto]),
                      Write(fig[punto + 3]))
        self.play(Create(fig[10]), run_time=1.5)   # circunscrita
        euler = Text("Recta de Euler", font_size=36, color=GRANATE)
        euler.to_corner(UR, buff=0.6)
        auxiliares = VGroup(*fig[4:10], *fig[11:14])
        self.play(ReplacementTransform(rotulo, euler),
                  auxiliares.animate.set_stroke(opacity=0.35),
                  Create(fig[14]), run_time=1.5)
        formula = MathTex(r"\overline{HG} = 2\,\overline{GO}",
                          font_size=44)
        formula.next_to(euler, DOWN, buff=0.6)
        self.play(Write(formula))
        self.wait()
