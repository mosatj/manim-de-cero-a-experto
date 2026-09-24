from manim import *


class CirculoElipse(Scene):
    def construct(self):
        plano = NumberPlane(
            background_line_style={"stroke_opacity": 0.5})
        circulo = Circle(radius=1, color=YELLOW)
        angulos = np.linspace(0, TAU, 12, endpoint=False)
        radios = VGroup(*[Line(ORIGIN, [np.cos(t), np.sin(t), 0],
                               color=YELLOW, stroke_width=2)
                          for t in angulos])
        A = np.array([[2, 1], [1, 2]])            # simétrica
        rotulo = MathTex(r"A=\begin{bmatrix}2&1\\1&2\end{bmatrix}")
        rotulo.add_background_rectangle().to_corner(UL)
        # Semiejes: 3 y 1 (autovalores) en las direcciones (1, 1)
        # y (1, -1) (autovectores unitarios u1 y u2)
        u1 = np.array([1, 1, 0]) / np.sqrt(2)
        u2 = np.array([1, -1, 0]) / np.sqrt(2)
        ejes_elipse = VGroup(DashedLine(-3 * u1, 3 * u1, color=RED),
                             DashedLine(-u2, u2, color=RED))

        self.add(plano, rotulo, circulo, radios)
        self.play(ApplyMatrix(A, plano), ApplyMatrix(A, circulo),
                  ApplyMatrix(A, radios), run_time=3)
        self.play(Create(ejes_elipse))
