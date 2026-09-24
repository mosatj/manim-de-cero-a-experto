from manim import *

# Okabe e Ito: naranja, azul cielo y verde azulado
COLORES = ["#E69F00", "#56B4E9", "#009E73"]
FUNCIONES = [(lambda x: x, "lineal"),
             (lambda x: x**2 / 4, "cuadrática"),
             (lambda x: 2 ** (x - 1), "exponencial")]


class EtiquetasDirectas(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 5], y_range=[0, 16, 4], x_length=7,
                    y_length=5.5).shift(LEFT)
        self.play(Create(ejes))
        estilos = [{}, {"num_dashes": 40}, {"num_dashes": 15}]
        for (f, nombre), color, estilo in zip(FUNCIONES, COLORES,
                                              estilos):
            curva = ejes.plot(f, x_range=[0, 5], color=color)
            if estilo:  # además del color, distingue el trazo
                curva = DashedVMobject(curva, **estilo)
            rotulo = Text(nombre, font_size=28, color=color)
            rotulo.next_to(ejes.c2p(5, f(5)), RIGHT)
            self.play(Create(curva), FadeIn(rotulo))
