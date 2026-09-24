from manim import *

# Componentes gráficos de la lección (sin escenas): los importan el
# storyboard, la lección completa y la versión vertical.
# Tonos de luminosidad media: se leen sobre negro y también impresos
COLORES = [BLUE_D, TEAL_D, GREEN_D, GOLD_D, RED_D, PURPLE_D]


def escuadra(k, lado=0.42, color=None):
    """El k-ésimo impar, 2k - 1, como una escuadra de celdas."""
    color = color or COLORES[(k - 1) % len(COLORES)]
    celdas = [(k - 1, j) for j in range(k)] + [(i, k - 1)
                                              for i in range(k - 1)]
    return VGroup(*[
        Square(lado * 0.86, stroke_width=0, fill_color=color,
               fill_opacity=1).move_to([i * lado, j * lado, 0])
        for i, j in celdas
    ])


def cuadrado_de_escuadras(n, lado=0.42):
    """n escuadras encajadas: un cuadrado de n × n celdas."""
    grupo = VGroup(*[escuadra(k, lado) for k in range(1, n + 1)])
    return grupo.move_to(ORIGIN)

