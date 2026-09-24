from manim import *


class Angulos(Scene):
    def construct(self):
        A, B, C = [np.array(p) for p in
                   ([-3, -2, 0], [3.5, -2, 0], [0, 2.5, 0])]
        self.add(Polygon(A, B, C, color=WHITE))
        colores = [BLUE, GREEN, RED]
        # En V: ángulo entre V→S (siguiente) y V→P (previo)
        for V, S, P, c in zip([A, B, C], [B, C, A], [C, A, B],
                              colores):
            angulo = Angle(Line(V, S), Line(V, P), radius=0.7,
                           color=c)
            grados = round(angulo.get_value(degrees=True))
            rotulo = MathTex(rf"{grados}^\circ", color=c,
                             font_size=36)
            rotulo.move_to(Angle(Line(V, S), Line(V, P),
                                 radius=1.15)
                           .point_from_proportion(0.5))
            self.add(angulo, rotulo)
