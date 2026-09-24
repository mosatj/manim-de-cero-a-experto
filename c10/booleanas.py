from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class Booleanas(Scene):
    def construct(self):
        def par():
            a = Circle(1, color=BLUE).shift(0.5 * LEFT)
            b = Square(1.7, color=RED).shift(0.5 * RIGHT)
            return a, b
        casos = [("Union", Union), ("Intersection", Intersection),
                 ("Difference", Difference),
                 ("Exclusion", Exclusion)]
        paneles = VGroup()
        for nombre, operacion in casos:
            a, b = par()
            resultado = operacion(a, b, color=YELLOW,
                                  fill_opacity=0.5)
            contornos = VGroup(a, b).set_stroke(width=2,
                                                opacity=0.6)
            rotulo = Text(f"{nombre}(a, b)", font_size=26)
            rotulo.next_to(contornos, DOWN)
            paneles.add(VGroup(resultado, contornos, rotulo))
        paneles.arrange(RIGHT, buff=0.5)
        leyenda = Text("a = círculo (azul),  b = cuadrado (rojo)",
                       font_size=26).to_edge(UP)
        self.add(paneles, leyenda)
