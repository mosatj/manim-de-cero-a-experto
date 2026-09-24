from manim import *


class TablaSeno(Scene):
    def construct(self):
        angulos = [0, 30, 45, 60, 90]
        valores = [np.sin(a * DEGREES) for a in angulos]
        tabla = DecimalTable(
            [valores],
            col_labels=[MathTex(rf"{a}^\circ") for a in angulos],
            row_labels=[MathTex(r"\sin\theta")],
            element_to_mobject_config={"num_decimal_places": 3},
            include_outer_lines=True,
        ).scale(0.85)
        tabla.get_labels().set_color(YELLOW)
        tabla.get_entries_without_labels().set_color(BLUE)
        self.add(tabla)
