from manim import *


def formula_con_leyenda(tex, significados, **kwargs):
    """Colorea cada símbolo; devuelve fórmula y leyenda."""
    colores = [YELLOW, BLUE, GREEN, RED, PURPLE]
    mapa = {s: c for s, c in zip(significados, colores)}
    formula = MathTex(tex, tex_to_color_map=mapa, **kwargs)
    filas = VGroup()
    for simbolo, texto in significados.items():
        fila = VGroup(MathTex(simbolo, color=mapa[simbolo]),
                      Text(texto, font_size=28))
        filas.add(fila.arrange(RIGHT, buff=0.3))
    filas.arrange(DOWN, aligned_edge=LEFT)
    return VGroup(formula, filas).arrange(DOWN, buff=0.8)


class Leyenda(Scene):
    def construct(self):
        newton = formula_con_leyenda(
            r"F = m\,a",
            {"F": "fuerza (N)", "m": "masa (kg)",
             "a": "aceleración (m/s²)"},
            font_size=96,
        )
        self.add(newton)
