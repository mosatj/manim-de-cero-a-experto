from manim import *

FUENTE = '''def factorial(n):
    """Producto 1·2·…·n."""
    resultado = 1
    for k in range(2, n + 1):
        resultado *= k
    return resultado'''


class CodigoPantalla(Scene):
    def construct(self):
        listado = Code(
            code_string=FUENTE,
            language="python",
            formatter_style="monokai",
            background="window",          # ventana con tres botones
            paragraph_config={"font": "Monospace", "font_size": 28},
        )
        self.play(FadeIn(listado))
        # code_lines es un Paragraph: una línea por submobject
        linea = listado.code_lines[3]
        marco = SurroundingRectangle(linea, color=YELLOW, buff=0.08)
        self.play(Create(marco))
        self.wait()
