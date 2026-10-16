from manim import *
from pygments.token import Comment, Keyword

# Los colores los decide Pygments: se hereda un estilo
Base = Code.get_pygments_style("monokai")


class EstiloLibro(Base):
    background_color = "#0B2A3C"
    line_number_color = "#6F8796"
    styles = {**Base.styles,
              Keyword: "bold #6FC3E8",
              Comment: "italic #E0708F"}


class CodigoEstilo(Scene):
    def construct(self):
        listado = Code(
            code_file="formulas_alineadas.py",   # el archivo real
            formatter_style=EstiloLibro,
            line_numbers_from=1,
            paragraph_config={"font": "Monospace", "font_size": 20},
        ).scale_to_fit_height(7)
        self.add(listado)
