from manim import *


class PascalModuloDos(Scene):
    def construct(self):
        n_filas, lado = 32, 0.22
        fila = [1]
        celdas = VGroup()
        for i in range(n_filas):
            for j, valor in enumerate(fila):
                c = Square(lado, stroke_width=0,
                           fill_opacity=1 if valor % 2 else 0.12,
                           fill_color=(YELLOW if valor % 2
                                       else GREY_D))
                c.move_to([(j - i / 2) * lado, -i * lado, 0])
                celdas.add(c)
            # Siguiente fila: solo importa la paridad (suma mód. 2)
            medio = [(a + b) % 2 for a, b in zip(fila, fila[1:])]
            fila = [1] + medio + [1]
        celdas.center()
        self.play(LaggedStart(*[FadeIn(c) for c in celdas],
                              lag_ratio=0.002), run_time=4)
        self.wait()
