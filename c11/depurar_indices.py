from manim import *


class DepurarIndices(Scene):
    def construct(self):
        formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}",
                          font_size=110).to_edge(UP)
        # Paso 1: numerar los glifos del trozo 0 (el único que hay)
        formula.set_color(GRAY_D)          # atenuada: se leen mejor
        etiquetas = index_labels(formula[0], label_height=0.24)
        etiquetas.set_color(YELLOW)
        self.add(formula, etiquetas)
        # Paso 2: una copia coloreada con los números ya leídos
        copia = formula.copy().set_color(WHITE).scale(0.7)
        copia.to_edge(DOWN, buff=0.8)
        copia[0][3].set_color(BLUE)        # la b de -b
        copia[0][7:13].set_color(GREEN)    # b^2-4ac (sin la barra)
        copia[0][14:16].set_color(RED)     # 2a
        self.add(copia)
