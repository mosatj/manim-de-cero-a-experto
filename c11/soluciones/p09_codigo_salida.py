from manim import *

FUENTE = '''for n in range(1, 4):
    print(n, n ** 2)'''


class CodigoSalida(Scene):
    def construct(self):
        listado = Code(code_string=FUENTE, language="python",
                       formatter_style="monokai",
                       paragraph_config={"font": "Monospace",
                                         "font_size": 36})
        salida = Paragraph("1 1", "2 4", "3 9", font="Monospace",
                           font_size=36, color=GREEN)
        rotulo = Text("Salida", font_size=24, color=GRAY_B)
        derecha = VGroup(rotulo, salida).arrange(DOWN, buff=0.3)
        VGroup(listado, derecha).arrange(RIGHT, buff=1.5)
        flecha = Arrow(listado.get_right(), derecha.get_left())
        self.add(listado, flecha, derecha)
