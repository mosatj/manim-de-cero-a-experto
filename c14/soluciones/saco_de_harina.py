from manim import *


def area(m):
    # Área de la elipse que ocupa la pelota: pi * a * b
    return PI * m.width * m.height / 4


class SacoDeHarina(Scene):
    def construct(self):
        suelo = Line(6 * LEFT, 6 * RIGHT).shift(2.5 * DOWN)
        pelotas = VGroup(*[Circle(0.8, color=c, fill_opacity=0.6)
                           for c in (BLUE, RED)])
        pelotas.arrange(RIGHT, buff=4).shift(2 * UP)
        self.add(suelo, pelotas)
        k = 1.5                                  # cuánto se aplasta
        # Caída: termina a toda velocidad, justo al tocar el suelo
        self.play(pelotas.animate(rate_func=rush_into)
                  .shift((pelotas.get_bottom()[1] - suelo.get_y())
                         * DOWN), run_time=0.8)
        izquierda, derecha = pelotas
        self.play(
            # Se ensancha k veces y se encoge 1/k: área constante
            izquierda.animate.stretch(k, 0, about_edge=DOWN)
            .stretch(1 / k, 1, about_edge=DOWN),
            # Solo se encoge en vertical: pierde área
            derecha.animate.stretch(1 / k, 1, about_edge=DOWN),
            run_time=0.15)
        for pelota, nombre in [(izquierda, "volumen constante"),
                               (derecha, "solo aplastada")]:
            rotulo = Text(f"{nombre}\nárea = {area(pelota):.2f}",
                          font_size=28, line_spacing=0.8)
            self.add(rotulo.next_to(pelota, UP, buff=0.5))
        self.wait()
