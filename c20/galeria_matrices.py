from manim import *


class GaleriaMatrices(Scene):
    def construct(self):
        m1 = Matrix([["a", "b"], ["c", "d"]])            # MathTex
        m2 = IntegerMatrix([[1, -2, 0], [3, 4, 5]],
                           left_bracket="(", right_bracket=")")
        m3 = DecimalMatrix([[np.pi, np.e], [np.sqrt(2), 0.5]],
                           element_to_mobject_config={
                               "num_decimal_places": 3})
        figuras = [[Circle(0.3), Square(0.6)],
                   [Triangle().scale(0.35), Star().scale(0.3)]]
        m4 = MobjectMatrix(figuras)
        m2.set_column_colors(YELLOW, BLUE, GREEN)    # por columnas
        m3.get_brackets().set_color(RED)             # corchetes
        m4.get_rows()[1].set_color(TEAL)             # segunda fila
        # Determinante "det(...) = ad − bc" alrededor de m1
        det = get_det_text(m1, determinant="ad-bc",
                           initial_scale_factor=1)
        celdas = VGroup(VGroup(m1, det), m2, m3, m4)
        nombres = ["Matrix + get_det_text", "IntegerMatrix",
                   "DecimalMatrix", "MobjectMatrix"]
        for celda, nombre in zip(celdas, nombres):
            celda.add(Text(nombre, font_size=24, color=GRAY)
                      .next_to(celda, DOWN))
        celdas.arrange_in_grid(rows=2, cols=2, buff=(1.2, 0.8))
        self.add(celdas)
