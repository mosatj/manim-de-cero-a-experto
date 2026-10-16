from manim import *

# Pregunta antes de respuesta: con Manim Slides bastaría heredar de
# Slide y cambiar cada next_section por next_slide


def f(x):
    return 0.3 * x**2 + 0.5


class PrediccionSecante(Scene):
    def construct(self):
        self.next_section("pregunta")
        pregunta = Text("Si Q se acerca a P, ¿a qué recta tiende "
                        "la secante PQ?", font_size=32)
        pregunta.to_edge(UP)
        opciones = VGroup(*[Text(t, font_size=32) for t in (
            "A. a una vertical", "B. a una horizontal",
            "C. a la tangente en P")])
        opciones.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        opciones.to_edge(LEFT, buff=0.6).shift(0.3 * DOWN)
        self.play(FadeIn(pregunta), LaggedStart(
            *[FadeIn(o) for o in opciones], lag_ratio=0.4))
        self.wait(2)  # en el aula: espera las respuestas

        self.next_section("respuesta")
        ejes = Axes(x_range=[0, 4, 1], y_range=[0, 5, 1],
                    x_length=5.6, y_length=4.6, tips=False)
        ejes.to_edge(RIGHT, buff=0.5).shift(0.5 * DOWN)
        curva = ejes.plot(f, x_range=[0, 3.7], color=BLUE_D)
        xp = 1.5
        punto_p = Dot(ejes.c2p(xp, f(xp)))
        etiqueta = Text("P", font_size=32).next_to(punto_p, UL, 0.1)

        def recta(m, color=GRAY):
            a, b = xp - 0.8, xp + 2.3  # tramo visible de la recta
            inicio = ejes.c2p(a, f(xp) + m * (a - xp))
            fin = ejes.c2p(b, f(xp) + m * (b - xp))
            return Line(inicio, fin, color=color)

        self.play(Create(ejes), Create(curva),
                  FadeIn(punto_p, etiqueta))
        for xq in (3.5, 2.9, 2.4, 2.0, 1.7):
            q = Dot(ejes.c2p(xq, f(xq)), color=GREEN_D)
            secante = recta((f(xq) - f(xp)) / (xq - xp))
            self.play(Create(secante), FadeIn(q), run_time=0.6)
            # La secante deja rastro: se compara con las anteriores
            self.play(secante.animate.set_stroke(opacity=0.35),
                      FadeOut(q), run_time=0.3)
        tangente = recta(0.6 * xp, color=RED_D)  # pendiente f'(xp)
        marco = SurroundingRectangle(opciones[2], color=RED_D)
        self.play(Create(tangente), Create(marco))
        self.wait()
