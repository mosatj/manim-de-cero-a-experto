from manim import *
from congelar import congelar


class MorfosisAlfa(Scene):
    def construct(self):
        clases = [Transform, ClockwiseTransform,
                  CounterclockwiseTransform]
        for k, clase in enumerate(clases):
            centro = np.array([-4.7 + 4.7 * k, 0, 0])
            inicio = Square(side_length=0.9, color=BLUE,
                            fill_opacity=0.7)
            inicio.move_to(centro + 1.6 * LEFT)
            fin = Circle(radius=0.5, color=YELLOW, fill_opacity=0.7)
            fin.move_to(centro + 1.6 * RIGHT)
            # Seis instantes de la misma animación (ritmo lineal)
            for alfa in [0, 0.2, 0.4, 0.6, 0.8, 1]:
                figura = inicio.copy()
                animacion = clase(figura, fin.copy(),
                                  rate_func=linear)
                congelar(self, animacion, alfa)
                if 0 < alfa < 1:
                    figura.set_opacity(0.4)
            nombre = Text(clase.__name__, font="Monospace",
                          font_size=18)
            nombre.move_to(centro + 3 * UP)
            self.add(nombre)
