from manim import *


def permutaciones(lista):
    """Todas las permutaciones de lista, generadas por recursión."""
    if len(lista) <= 1:
        return [lista[:]]
    resultado = []
    for i, primero in enumerate(lista):
        resto = lista[:i] + lista[i + 1:]
        # fijo uno, permuto el resto
        for p in permutaciones(resto):
            resultado.append([primero] + p)
    return resultado


class Celda(VGroup):
    """Cuadrado con un número; recuerda su valor."""

    def __init__(self, valor, lado=0.8, **kwargs):
        caja = Square(lado, fill_opacity=0.9,
                      fill_color=[BLUE_D, TEAL_D,
                                  PURPLE_D][valor - 1])
        numero = MathTex(str(valor)).move_to(caja)
        super().__init__(caja, numero, **kwargs)
        self.valor = valor


class Permutaciones(Scene):
    def construct(self):
        filas = VGroup()
        for k, p in enumerate(permutaciones([1, 2, 3])):
            fila = VGroup(*[Celda(v) for v in p])
            fila.arrange(RIGHT, buff=0)
            fila.move_to(LEFT * 2 + UP * (2.6 - 1.0 * k))
            filas.add(fila)
        cuenta = MathTex(r"3! = 3\cdot 2\cdot 1 = 6", font_size=48)
        cuenta.to_edge(RIGHT, buff=1)

        self.play(FadeIn(filas[0]))
        for previa, fila in zip(filas, filas[1:]):
            # Cada celda viaja al sitio que su valor ocupa abajo
            self.play(*[
                TransformFromCopy(c, next(d for d in fila
                                          if d.valor == c.valor),
                                  path_arc=-PI / 3)
                for c in previa], run_time=0.9)
        self.play(Write(cuenta))
        self.wait()
