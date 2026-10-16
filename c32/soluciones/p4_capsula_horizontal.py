import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent  # codigo/c32
sys.path.insert(0, str(RAIZ / "proyecto4"))
import formato_horizontal as fv  # el único cambio de importación
from manim import *
from componentes import (
    CirculoUnitario,
    COLOR_SEN,
    COLOR_COS,
    COLOR_UNO,
)

MOSTRAR_GUIAS = False  # True mientras se compone

# Ejercicio 32.13: la cápsula del proyecto 4 en 16:9. El código es el de
# capsula.py; solo cambia la composición, que no puede automatizarse:
# con 9 unidades de alto, el texto va a la izquierda y la circunferencia
# a la derecha.
IZQUIERDA = LEFT * 3.9
DERECHA = RIGHT * 3.6


class CapsulaHorizontal(Scene):
    def construct(self):
        if MOSTRAR_GUIAS:
            self.add(fv.zona_segura())
        # 1. Gancho: la pregunta, arriba a la izquierda
        gancho = fv.arriba(
            fv.lineas("¿Por qué siempre", "da 1?", tam=fv.TAM_GANCHO)
        ).shift(IZQUIERDA)
        identidad = MathTex(
            r"\sin^2\theta", "+", r"\cos^2\theta", "=", "1",
            font_size=72,
        )
        identidad.next_to(gancho, DOWN, buff=0.6)
        identidad[0].set_color(COLOR_SEN)
        identidad[2].set_color(COLOR_COS)
        identidad[4].set_color(COLOR_UNO)
        self.play(Write(gancho), run_time=1)
        self.play(Write(identidad), run_time=1.5)

        # 2. Desarrollo: el triángulo dentro de la circunferencia
        unitario = CirculoUnitario(r=3.0).shift(DERECHA)
        self.play(Create(unitario.circulo), Create(unitario.ejes))
        self.play(FadeIn(unitario.triangulo))
        self.add(unitario)
        nombres = always_redraw(
            lambda: VGroup(
                MathTex(
                    r"\cos\theta", color=COLOR_COS, font_size=fv.TAM_TEXTO
                ).next_to(unitario.triangulo[0], DOWN),
                MathTex(
                    r"\sin\theta", color=COLOR_SEN, font_size=fv.TAM_TEXTO
                ).next_to(unitario.triangulo[1], RIGHT),
                MathTex(
                    "1", color=COLOR_UNO, font_size=fv.TAM_TEXTO
                ).move_to(unitario.triangulo[2].get_center() + 0.4 * UL),
            )
        )
        self.play(FadeIn(nombres))
        self.play(unitario.theta.animate.set_value(2 * PI / 5), run_time=2)
        self.play(unitario.theta.animate.set_value(PI / 4), run_time=1.5)

        # 3. Cierre: la moraleja, bajo la identidad (columna izquierda)
        cierre = fv.lineas("Es Pitágoras con", "hipotenusa 1")
        cierre.next_to(identidad, DOWN, buff=0.9)
        self.play(Circumscribe(identidad, color=COLOR_UNO), Write(cierre))
        self.wait()
