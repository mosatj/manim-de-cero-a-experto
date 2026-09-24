import formato_vertical as fv  # primero: fija el formato 9:16
from manim import *
from componentes import (
    CirculoUnitario,
    COLOR_SEN,
    COLOR_COS,
    COLOR_UNO,
)

MOSTRAR_GUIAS = False  # True mientras se compone


class CapsulaIdentidad(Scene):
    def construct(self):
        if MOSTRAR_GUIAS:
            self.add(fv.zona_segura())
        # 1. Gancho (0-3 s): una pregunta en letras grandes
        gancho = fv.arriba(
            fv.lineas(
                "¿Por qué siempre", "da 1?", tam=fv.TAM_GANCHO
            )
        )
        identidad = MathTex(
            r"\sin^2\theta",
            "+",
            r"\cos^2\theta",
            "=",
            "1",
            font_size=72,
        )
        identidad.next_to(gancho, DOWN, buff=0.6)
        identidad[0].set_color(COLOR_SEN)
        identidad[2].set_color(COLOR_COS)
        identidad[4].set_color(COLOR_UNO)
        self.play(Write(gancho), run_time=1)
        self.play(Write(identidad), run_time=1.5)

        # 2. Desarrollo: el triángulo dentro de la circunferencia
        unitario = CirculoUnitario(r=2.8).shift(DOWN * 0.5)
        self.play(Create(unitario.circulo), Create(unitario.ejes))
        self.play(FadeIn(unitario.triangulo))
        self.add(unitario)
        nombres = always_redraw(
            lambda: VGroup(
                MathTex(
                    r"\cos\theta",
                    color=COLOR_COS,
                    font_size=fv.TAM_TEXTO,
                ).next_to(unitario.triangulo[0], DOWN),
                MathTex(
                    r"\sin\theta",
                    color=COLOR_SEN,
                    font_size=fv.TAM_TEXTO,
                ).next_to(unitario.triangulo[1], RIGHT),
                MathTex(
                    "1", color=COLOR_UNO, font_size=fv.TAM_TEXTO
                ).move_to(
                    unitario.triangulo[2].get_center() + 0.4 * UL
                ),
            )
        )
        self.play(FadeIn(nombres))
        # El ángulo cambia y la hipotenusa sigue midiendo 1
        self.play(
            unitario.theta.animate.set_value(2 * PI / 5), run_time=2
        )
        self.play(
            unitario.theta.animate.set_value(PI / 4), run_time=1.5
        )

        # 3. Cierre: Pitágoras en el triángulo y la moraleja
        cierre = fv.lineas("Es Pitágoras con", "hipotenusa 1")
        cierre.to_edge(DOWN, buff=fv.MARGEN_ABAJO)
        self.play(
            Circumscribe(identidad, color=COLOR_UNO), Write(cierre)
        )
