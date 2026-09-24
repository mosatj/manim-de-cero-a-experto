"""Un cuadrado n × n construido con n capas en forma de L."""
from manim import *

if __package__:        # importado como parte del paquete
    from .estilo import ACERO, GRANATE
else:                  # ejecutado suelto, para probarlo
    from estilo import ACERO, GRANATE


class CuadradoImpares(VGroup):
    """La capa k (1, 2, …, n) tiene 2k − 1 cuadraditos."""

    def __init__(self, n, lado=0.5, colores=(ACERO, GRANATE),
                 **kwargs):
        super().__init__(**kwargs)
        for k in range(1, n + 1):
            capa = VGroup()
            for fila in range(k):
                for col in range(k):
                    if max(fila, col) == k - 1:   # borde de la L
                        celda = Square(lado, stroke_width=2,
                                       fill_opacity=0.8)
                        celda.move_to([col * lado, fila * lado, 0])
                        capa.add(celda)
            capa.set_fill(colores[(k - 1) % 2])
            capa.set_stroke(WHITE, width=2)
            self.add(capa)
        self.move_to(ORIGIN)

    def capa(self, k):
        return self[k - 1]


if __name__ == "__main__":
    cuadro = CuadradoImpares(4)
    print("celdas por capa:", [len(capa) for capa in cuadro])
    print("ancho y alto:", cuadro.width, cuadro.height)
