from manim import *

COLORES = ["#4F7C99", "#8E2130", "#0B2A3C"]


class Cortinilla(Scene):
    """Transición de marca: tapa el cuadro entero y lo destapa."""
    marca = "Cálculo I"
    hasta_el_corte = False  # True: se detiene con el cuadro tapado

    def construct(self):
        bandas = VGroup(*[
            Rectangle(width=6, height=12, fill_color=c,
                      fill_opacity=1, stroke_width=0)
            for c in COLORES]).arrange(RIGHT, buff=-0.6)
        bandas.rotate(-12 * DEGREES)
        recorrido = 24 * RIGHT
        bandas.shift(-recorrido)  # fuera del cuadro, a la izquierda
        rotulo = Text(self.marca, font_size=96, weight=BOLD,
                      color="#E9F2F7")
        # La banda delantera (la de la derecha) llega primero
        self.play(LaggedStart(
            *[b.animate(rate_func=rush_from).shift(recorrido)
              for b in reversed(bandas)], lag_ratio=0.25),
            run_time=0.7)
        inicio = self.time  # desde aquí, el cuadro está tapado
        self.play(FadeIn(rotulo, scale=0.8), run_time=0.25)
        if self.hasta_el_corte:
            self.mostrar_corte(inicio)
            return
        self.wait(0.3)
        self.play(FadeOut(rotulo), run_time=0.25)
        fin = self.time
        logger.info(f"Cuadro tapado de {inicio:.2f} a {fin:.2f} s")
        self.play(LaggedStart(
            *[b.animate(rate_func=rush_into).shift(recorrido)
              for b in reversed(bandas)], lag_ratio=0.25),
            run_time=0.7)

    def mostrar_corte(self, inicio):
        nota = Text(f"tapado desde t = {inicio:.2f} s: corta aquí",
                    font_size=34, color="#E9F2F7")
        self.add(nota.to_edge(DOWN, buff=0.6))


class CortinillaMuestra(Cortinilla):
    """Para el libro: el instante en que el cuadro está tapado."""
    hasta_el_corte = True
