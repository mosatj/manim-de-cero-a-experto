from manim import *
from componentes import par_de_marcos, rotulo
from narracion import GuionScene


class Demostracion(GuionScene):
    def construct(self):
        izquierda, derecha = par_de_marcos()
        self.decir(
            "marco",
            Create(izquierda.marco),
            LaggedStart(
                *[
                    FadeIn(t, scale=0.6)
                    for t in izquierda.triangulos
                ],
                lag_ratio=0.4,
            ),
        )

        hueco_c = izquierda.hueco_c()
        c2 = rotulo("c^2", hueco_c)
        self.decir("hueco_c", FadeIn(hueco_c), Write(c2))

        # Copia a la derecha; sus triángulos solo se trasladan
        self.play(
            TransformFromCopy(izquierda.marco, derecha.marco),
            TransformFromCopy(
                izquierda.triangulos, derecha.triangulos
            ),
        )
        self.decir(
            "mover",
            *[
                Transform(t, d)
                for t, d in zip(
                    derecha.triangulos, derecha.destinos(2)
                )
            ],
        )

        huecos = derecha.huecos_ab()
        a2 = rotulo("a^2", huecos[0])
        b2 = rotulo("b^2", huecos[1])
        self.decir("hueco_ab", FadeIn(huecos), Write(a2), Write(b2))
