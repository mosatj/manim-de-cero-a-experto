from manim import *


class CronometradaBase(Scene):
    """Escena que anota la duración de cada play() y de cada pausa."""

    def setup(self):
        self.registro = []  # pares (es_pausa, duración en segundos)

    def play(self, *args, **kwargs):
        inicio = self.time
        super().play(*args, **kwargs)  # wait() también pasa por aquí
        es_pausa = len(args) == 1 and isinstance(args[0], Wait)
        self.registro.append((es_pausa, self.time - inicio))

    def hoja_de_tiempos(self, escala=1.0):
        total = sum(d for _, d in self.registro)
        eje = NumberLine(x_range=[0, total, 1], length=total * escala,
                         include_numbers=True, font_size=32)
        hoja, t = VGroup(eje), 0
        for es_pausa, duracion in self.registro:
            a, b = eje.n2p(t), eje.n2p(t + duracion)
            if es_pausa:
                tramo = Line(a, b, color=GRAY, stroke_width=6)
            else:
                tramo = Rectangle(width=b[0] - a[0], height=0.5,
                                  fill_color=BLUE, fill_opacity=0.85,
                                  stroke_color=WHITE, stroke_width=2)
                tramo.move_to((a + b) / 2)
            hoja.add(tramo.shift(0.6 * UP))
            t += duracion
        return hoja


class DemoCronometrada(CronometradaBase):
    def construct(self):
        circulo = Circle(radius=1.2, color=BLUE).shift(UP)
        formula = MathTex(r"A=\pi r^2").next_to(circulo, RIGHT)
        self.play(Create(circulo), run_time=2)
        self.wait()
        self.play(Write(formula), run_time=1.5)
        self.play(Indicate(formula), run_time=0.5)
        self.wait(2)
        hoja = self.hoja_de_tiempos().to_edge(DOWN, buff=0.8)
        self.add(hoja)  # se añade sin play(): no altera el registro
