from manim import *


class CuadradoTrinomio(Scene):
    def construct(self):
        lados = {"a": 2.4, "b": 1.5, "c": 0.9}
        color = {"aa": "#e63946", "bb": "#2a9d8f", "cc": "#457b9d",
                 "ab": "#f4a261", "ac": "#48cae4", "bc": "#e9c46a"}
        letras = "abc"
        piezas = {}                    # (fila, columna) -> pieza
        y = 0
        for fila in letras:            # de arriba hacia abajo
            x = 0
            for col in letras:
                clave = "".join(sorted(col + fila))   # "ba" = "ab"
                ancho, alto = lados[col], lados[fila]
                caja = Rectangle(width=ancho, height=alto,
                                 fill_color=color[clave],
                                 fill_opacity=0.9, stroke_width=2,
                                 stroke_color=WHITE)
                caja.move_to([x + ancho / 2, y - alto / 2, 0])
                nombre = (f"{clave[0]}^2" if clave[0] == clave[1]
                          else clave)
                texto = MathTex(nombre, color=BLACK).move_to(caja)
                piezas[fila, col] = VGroup(caja, texto)
                x += ancho
            y -= lados[fila]
        cuadrado = VGroup(*piezas.values()).move_to(UP * 0.7)
        llaves = VGroup(
            *[BraceLabel(piezas["c", k], k, DOWN) for k in letras],
            *[BraceLabel(piezas[k, "a"], k, LEFT) for k in letras])

        formula = MathTex("(a+b+c)^2", "=", "a^2", "+", "b^2", "+",
                          "c^2", "+", "2ab", "+", "2bc", "+", "2ca")
        formula.to_edge(DOWN, buff=0.35)
        # índice de cada término dentro de la fórmula
        terminos = {"aa": 2, "bb": 4, "cc": 6,
                    "ab": 8, "bc": 10, "ac": 12}

        marco = Square(sum(lados.values())).move_to(cuadrado)
        self.play(Create(marco), FadeIn(llaves), Write(formula[:2]))
        for clave, indice in terminos.items():
            iguales = [p for (f, c), p in piezas.items()
                       if "".join(sorted(f + c)) == clave]
            self.play(*[DrawBorderThenFill(p) for p in iguales],
                      run_time=0.8)
            rotulos = VGroup(*[p[1] for p in iguales])
            self.play(TransformFromCopy(rotulos, formula[indice]),
                      FadeIn(formula[indice - 1]), run_time=0.8)
        self.play(Circumscribe(formula, color=YELLOW))
        self.wait()
