from manim import *


class Proyeccion(Scene):
    def construct(self):
        u = np.array([4, 1, 0])
        v = np.array([2, 3, 0])
        # Proyección de v sobre u: (v·u / u·u) u
        p = (v @ u) / (u @ u) * u
        origen = 3 * LEFT + 2 * DOWN     # todo se dibuja desde aquí
        fu = Arrow(origen, origen + u, buff=0, color=BLUE)
        fv = Arrow(origen, origen + v, buff=0, color=GREEN)
        fp = Arrow(origen, origen + p, buff=0, color=YELLOW,
                   stroke_width=8)
        altura = DashedLine(origen + v, origen + p, color=GREY_B)
        base = Line(origen + p, origen + u)
        angulo_recto = RightAngle(altura, base, length=0.25,
                                  quadrant=(1, 1))
        rotulo = MathTex(r"\mathrm{proy}_{\vec u}\vec v")
        rotulo.set_color(YELLOW)
        rotulo.next_to(origen + p / 2, DOWN, buff=0.35)
        self.play(GrowArrow(fu), GrowArrow(fv))
        self.play(Create(altura), GrowArrow(fp))
        self.play(Create(angulo_recto), Write(rotulo))
