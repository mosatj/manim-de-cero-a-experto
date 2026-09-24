from manim import *


class SistemaRectas(Scene):
    def construct(self):
        # Vista por filas: cada ecuación es una recta
        filas = NumberPlane(x_range=[-1, 5], y_range=[-2, 5],
                            x_length=6, y_length=7,
                            background_line_style={
                                "stroke_opacity": 0.4})
        # Vista por columnas: b es combinación de las columnas
        columnas = filas.copy()
        dos = VGroup(filas, columnas).arrange(RIGHT, buff=0.6)
        dos.shift(0.3 * DOWN)
        r1 = filas.plot(lambda x: 5 - 2 * x, x_range=[0, 3.5],
                        color=YELLOW)                   # 2x + y = 5
        r2 = filas.plot(lambda x: x - 1, x_range=[-1, 5],
                        color=BLUE)                     # x - y = 1
        corte = Dot(filas.c2p(2, 1), color=GREEN)
        nom1 = MathTex("2x+y=5", color=YELLOW, font_size=30)
        nom1.next_to(filas.c2p(0.4, 4.2), RIGHT)
        nom2 = MathTex("x-y=1", color=BLUE, font_size=30)
        nom2.next_to(filas.c2p(4, 3), DOWN)
        nom_c = MathTex("(2,1)", color=GREEN, font_size=30)
        nom_c.next_to(corte, DR, buff=0.1)

        pc = columnas.c2p
        # 2·(2, 1) seguido de 1·(1, −1) llega a b = (5, 1)
        c1 = Arrow(pc(0, 0), pc(4, 2), buff=0, color=YELLOW)
        c2 = Arrow(pc(4, 2), pc(5, 1), buff=0, color=BLUE)
        b = Arrow(pc(0, 0), pc(5, 1), buff=0, color=GREEN)
        texto = MathTex(r"2\begin{bmatrix}2\\1\end{bmatrix}+1"
                        r"\begin{bmatrix}1\\-1\end{bmatrix}="
                        r"\begin{bmatrix}5\\1\end{bmatrix}",
                        font_size=30)
        texto.next_to(columnas.c2p(2, 4), UP, buff=0)
        titulos = VGroup(
            Text("filas", font_size=28).next_to(filas, UP),
            Text("columnas", font_size=28).next_to(columnas, UP))

        self.add(filas, columnas, titulos)
        self.play(Create(r1), Write(nom1))
        self.play(Create(r2), Write(nom2))
        self.play(FadeIn(corte), Write(nom_c))
        self.play(GrowArrow(c1), GrowArrow(c2))
        self.play(GrowArrow(b), Write(texto))
