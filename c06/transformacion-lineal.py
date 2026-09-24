from manim import *


class TransformacionLineal(Scene):
    def construct(self):
        estilo = {"stroke_opacity": 0.3}         # cuadrícula tenue
        plano = NumberPlane(background_line_style=estilo)
        cizalla = np.array([[1, 1],        # x' = x + y
                            [0, 1]])       # y' = y
        original = Square(2, color=BLUE, fill_opacity=0.4)
        original.move_to([1, 1, 0])       # vértices (0, 0) a (2, 2)
        imagen = original.copy().set_color(YELLOW)
        imagen.apply_matrix(cizalla, about_point=ORIGIN)
        rotulo = MathTex(r"\begin{pmatrix}1&1\\0&1\end{pmatrix}")
        rotulo.to_corner(UL).add_background_rectangle()
        self.add(plano, original)
        self.play(TransformFromCopy(original, imagen),
                  Write(rotulo))
