from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


def trio():
    circulo = Circle(1, color=RED, fill_opacity=1)
    cuadrado = Square(1.7, color=BLUE, fill_opacity=1)
    triangulo = Triangle(color=GREEN, fill_opacity=1).scale(1.1)
    cuadrado.shift(0.7 * RIGHT)
    triangulo.shift(0.35 * RIGHT + 0.6 * DOWN)
    return circulo, cuadrado, triangulo


class OrdenDibujo(Scene):
    def construct(self):
        # Izquierda: lo último que se añade queda encima
        a, b, c = trio()
        izq = VGroup(a, b, c).shift(3.5 * LEFT)
        self.add(a, b, c)
        # Derecha: el mismo orden de add(), pero con z_index
        d, e, f = trio()
        d.set_z_index(3)     # el círculo, arriba del todo
        f.set_z_index(-1)    # el triángulo, al fondo
        der = VGroup(d, e, f).shift(3.5 * RIGHT)
        self.add(d, e, f)
        self.add(Text("add(círculo, cuadrado, triángulo)",
                      font_size=24).next_to(izq, DOWN, buff=0.6))
        self.add(Text("el mismo add() con z_index",
                      font_size=24).next_to(der, DOWN, buff=0.6))
