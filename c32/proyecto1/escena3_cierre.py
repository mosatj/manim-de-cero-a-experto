from manim import *
from estilo import COLOR_A, COLOR_B, COLOR_C
from componentes import par_de_marcos, rotulo
from narracion import GuionScene


class Cierre(GuionScene):
    def construct(self):
        # La escena empieza donde terminó la anterior (mismo estado)
        izquierda, derecha = par_de_marcos()
        derecha.triangulos.become(derecha.destinos(2))
        hueco_c, huecos = izquierda.hueco_c(), derecha.huecos_ab()
        self.add(
            izquierda,
            derecha,
            hueco_c,
            huecos,
            rotulo("c^2", hueco_c),
            rotulo("a^2", huecos[0]),
            rotulo("b^2", huecos[1]),
        )

        igual = MathTex("=", font_size=96).move_to(UP * 0.5)
        resultado = MathTex(
            "c^2", "=", "a^2", "+", "b^2", font_size=72
        ).to_edge(UP, buff=0.3)
        for i, color in ((0, COLOR_C), (2, COLOR_A), (4, COLOR_B)):
            resultado[i].set_color(color)
        marco = SurroundingRectangle(
            resultado, color=WHITE, buff=0.2
        )
        self.decir(
            "conclusion",
            Write(igual),
            Write(resultado),
            Create(marco),
        )
