from manim import *

# Posiciones de los puntos (en una cara de lado 2) para cada valor
PUNTOS = {
    1: [(0, 0)],
    2: [(-1, 1), (1, -1)],
    3: [(-1, 1), (0, 0), (1, -1)],
    4: [(-1, 1), (1, 1), (-1, -1), (1, -1)],
    5: [(-1, 1), (1, 1), (0, 0), (-1, -1), (1, -1)],
    6: [(-1, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (1, -1)],
}


class Dado(VGroup):
    def __init__(self, valor=1, lado=2, **kwargs):
        super().__init__(**kwargs)
        self.lado = lado
        self.cara = RoundedRectangle(corner_radius=0.25 * lado,
                                     width=lado, height=lado)
        self.puntos = VGroup()
        self.add(self.cara, self.puntos)
        self.mostrar(valor)

    def mostrar(self, valor):
        """Muestra los puntos del valor pedido; devuelve self."""
        centro, paso = self.cara.get_center(), 0.3 * self.lado
        nuevos = [Dot(centro + paso * (x * RIGHT + y * UP),
                      radius=0.08 * self.lado)
                  for x, y in PUNTOS[valor]]
        self.puntos.become(VGroup(*nuevos))
        self.valor = valor
        return self


class EscenaDado(Scene):
    def construct(self):
        dados = VGroup(*[Dado(v, lado=1.6) for v in range(1, 7)])
        self.add(dados.arrange(RIGHT, buff=0.4))
