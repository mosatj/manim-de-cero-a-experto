from manim import *


class CribaEratostenes(Scene):
    def construct(self):
        celdas = VGroup()
        for n in range(1, 101):
            caja = Square(0.62, stroke_width=1.5,
                          stroke_color=GREY_B)
            texto = Text(str(n), font_size=20).move_to(caja)
            celdas.add(VGroup(caja, texto))
        celdas.arrange_in_grid(10, 10, buff=0)
        celdas.to_edge(LEFT, buff=0.7)
        colores = {2: BLUE_D, 3: GREEN_D, 5: PURPLE_D, 7: MAROON_D}
        rotulo = Tex("Criba de Eratóstenes", font_size=40)
        paso = MathTex(r"\text{primo } p", font_size=40)
        panel = VGroup(rotulo, paso).arrange(DOWN, buff=0.5)
        panel.to_edge(RIGHT, buff=0.8)
        self.add(celdas, panel)

        def tachar(n, tono):    # devuelve la animación de tachar
            caja, texto = celdas[n - 1]
            return AnimationGroup(caja.animate.set_fill(tono, 0.55),
                                  texto.animate.set_opacity(0.35))

        tachado = {1}
        self.play(tachar(1, GREY_D))
        for p in [2, 3, 5, 7]:                 # basta llegar a √100
            multiplos = [m for m in range(p * p, 101, p)
                         if m not in tachado]
            tachado.update(multiplos)
            nuevo = MathTex(rf"p = {p}:\ \text{{tacho }} {p * p},\,"
                            rf"{p * p + p},\ldots", font_size=40,
                            color=colores[p]).move_to(paso)
            self.play(
                Transform(paso, nuevo),
                Circumscribe(celdas[p - 1], color=colores[p]),
                LaggedStart(*[tachar(m, colores[p])
                              for m in multiplos], lag_ratio=0.1),
                run_time=2.5,
            )
        primos = [n for n in range(2, 101) if n not in tachado]
        final = MathTex(rf"\text{{quedan {len(primos)} primos}}",
                        font_size=40, color=YELLOW).move_to(paso)
        self.play(
            Transform(paso, final),
            *[celdas[n - 1][0].animate.set_fill(YELLOW, 0.35)
              for n in primos],
        )
        self.wait()
