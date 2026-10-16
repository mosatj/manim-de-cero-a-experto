from manim import *

PIEDRA = "#8A857C"   # gris medio: se ve sobre negro y sobre blanco


class FiguraDerivada(Scene):
    """Una figura pensada para un documento: sin animación, con
    rótulos en LaTeX y colores de tono medio, que se leen igual
    sobre el fondo negro de Manim y sobre el papel blanco."""

    def construct(self):
        ejes = Axes(
            x_range=[0, 4, 1], y_range=[0, 4, 1],
            x_length=7, y_length=4.5, tips=False,
            axis_config={
                "include_numbers": True, "color": PIEDRA,
                "decimal_number_config": {"color": PIEDRA,
                                          "num_decimal_places": 0},
            },
        )
        f = lambda x: x**2 / 4
        curva = ejes.plot(f, x_range=[0, 3.8], color="#4F7C99")
        a = 2
        pendiente = a / 2            # f'(x) = x/2
        tangente = ejes.plot(
            lambda x: f(a) + pendiente * (x - a),
            x_range=[0.6, 3.6], color="#B04A5A",
        )
        punto = Dot(ejes.c2p(a, f(a)), color="#B04A5A")
        rotulo_f = MathTex(r"f(x)=\tfrac{x^2}{4}", color="#4F7C99")
        rotulo_f.next_to(ejes.c2p(3.4, f(3.4)), LEFT, buff=0.4)
        rotulo_t = MathTex(r"f'(2)=1", color="#B04A5A")
        rotulo_t.next_to(punto, DOWN + RIGHT, buff=0.3)
        self.add(ejes, curva, tangente, punto, rotulo_f, rotulo_t)
