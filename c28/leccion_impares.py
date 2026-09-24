from manim import *
from impares import escuadra
from guion_impares import GUION, duracion
from subtitulos import repartir


class LeccionImpares(Scene):
    def empezar(self, bloque):
        """Abre una sección y programa los subtítulos del bloque."""
        self.next_section(bloque["bloque"])
        self.inicio_bloque = self.time
        for ini, fin, texto in repartir(bloque["voz"], 0,
                                        duracion(bloque) - 1):
            self.add_subcaption(texto, duration=fin - ini, offset=ini)

    def terminar(self, bloque):
        """Espera lo que falte para que la imagen dure lo que la voz."""
        usado = self.time - self.inicio_bloque
        self.wait(max(0.5, duracion(bloque) - usado))

    def construct(self):
        gancho, pregunta, construccion, generalizacion, cierre = GUION

        self.empezar(gancho)
        suma = MathTex("1+3+5+7", "=", r"\text{?}", font_size=80)
        suma.to_edge(UP).set_color_by_tex("?", YELLOW)
        self.play(Write(suma))
        self.terminar(gancho)

        self.empezar(pregunta)
        resultado = MathTex("16", font_size=80, color=YELLOW)
        resultado.next_to(suma[1], RIGHT)
        self.play(Transform(suma[2], resultado))
        self.terminar(pregunta)

        self.empezar(construccion)
        piezas = VGroup(*[escuadra(k, 0.6) for k in range(1, 5)])
        piezas.move_to(0.4 * DOWN)
        for pieza in piezas:  # un impar cada vez (segmentación)
            self.play(FadeIn(pieza, shift=0.3 * UR), run_time=0.8)
        self.terminar(construccion)

        self.empezar(generalizacion)
        formula = MathTex(r"1+3+\cdots+(2n-1)=n^2", font_size=60)
        formula.to_edge(DOWN)
        llave = Brace(piezas, RIGHT)
        lado = llave.get_tex("n=4")
        self.play(GrowFromCenter(llave), Write(lado))
        self.play(TransformFromCopy(suma, formula))
        self.terminar(generalizacion)

        self.empezar(cierre)
        self.play(Create(SurroundingRectangle(formula, color=YELLOW)))
        self.terminar(cierre)
