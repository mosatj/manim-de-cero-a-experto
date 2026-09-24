from manim import *


def binaria_eventos(a, x):
    bajo, alto = 0, len(a) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        yield bajo, medio, alto
        if a[medio] == x:
            return
        elif a[medio] < x:
            bajo = medio + 1      # descarto la mitad izquierda
        else:
            alto = medio - 1      # descarto la mitad derecha


class BusquedaBinaria(Scene):
    def construct(self):
        a = [3, 7, 11, 15, 18, 22, 25, 30, 34, 37, 41, 46, 50, 55,
             61]
        x = 37
        celdas = VGroup(*[
            VGroup(Square(0.8), MathTex(str(v), font_size=34))
            for v in a]).arrange(RIGHT, buff=0)
        for c in celdas:
            c[1].move_to(c[0])
        indices = VGroup(*[
            Text(str(k), font_size=20, color=GREY_B)
            .next_to(c, UP, buff=0.1)
            for k, c in enumerate(celdas)])
        titulo = MathTex(rf"\text{{Buscar }} x = {x}", font_size=44)
        self.add(celdas, indices, titulo.to_edge(UP))

        def puntero(nombre, color):
            flecha = Arrow(0.5 * DOWN, 0.5 * UP, color=color,
                           buff=0)
            rotulo = Text(nombre, font_size=22, color=color)
            return VGroup(flecha, rotulo).arrange(DOWN, buff=0.05)

        punteros = [puntero("bajo", BLUE_C),
                    puntero("medio", YELLOW),
                    puntero("alto", RED_C)]
        visibles = False
        for bajo, medio, alto in binaria_eventos(a, x):
            indices_p = (bajo, medio, alto)
            destinos = [p.copy().next_to(celdas[k], DOWN, 0.1)
                        for p, k in zip(punteros, indices_p)]
            # si bajo o alto coinciden con medio, se apartan un poco
            destinos[0].shift(0.2 * LEFT * (bajo == medio))
            destinos[2].shift(0.2 * RIGHT * (alto == medio))
            apagar = [c.animate.set_opacity(0.2)
                      for k, c in enumerate(celdas)
                      if not bajo <= k <= alto]
            if not visibles:
                self.play(*[FadeIn(d) for d in destinos])
                punteros, visibles = destinos, True
            else:
                self.play(*[Transform(p, d) for p, d in
                            zip(punteros, destinos)], *apagar)
            self.play(Indicate(celdas[medio]), run_time=0.8)
        self.play(celdas[medio][0].animate.set_fill(GREEN_D, 0.8))
        self.wait()
