from manim import *


class HiperbolasNivel(Scene):
    def construct(self):
        plano = NumberPlane(x_range=[-4, 4, 1], y_range=[-3, 3, 1],
                            x_length=9.5, y_length=7.1,
                            background_line_style={
                                "stroke_opacity": 0.3})
        niveles = [-2, -1, 0, 1, 2]
        colores = color_gradient([BLUE, WHITE, RED], len(niveles))
        curvas = VGroup()
        for c, color in zip(niveles, colores):
            # Curva de nivel x^2 - y^2 = c  (cierre sobre c)
            curva = plano.plot_implicit_curve(
                lambda x, y, c=c: x ** 2 - y ** 2 - c, color=color)
            curvas.add(curva)
        leyenda = MathTex(r"x^2-y^2=c,\ c\in\{-2,\dots,2\}",
                          font_size=34)
        leyenda.add_background_rectangle(opacity=0.85, buff=0.1)
        leyenda.to_corner(UL)
        self.add(plano)
        self.play(LaggedStart(*[Create(c) for c in curvas],
                              lag_ratio=0.3))
        self.add(leyenda)
        self.wait()
