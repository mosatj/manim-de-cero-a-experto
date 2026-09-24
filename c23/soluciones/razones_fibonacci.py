from manim import *


class RazonesFibonacci(Scene):
    def construct(self):
        fib = [1, 1]
        while len(fib) < 14:
            fib.append(fib[-1] + fib[-2])
        razones = [fib[k + 1] / fib[k] for k in range(13)]
        phi = (1 + 5 ** 0.5) / 2
        ejes = Axes(x_range=[0, 14, 2], y_range=[0.8, 2.2, 0.2],
                    x_length=10, y_length=5.5, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 26})
        linea_phi = DashedLine(ejes.c2p(0, phi), ejes.c2p(14, phi),
                               color=YELLOW)
        rotulo = MathTex(r"\varphi", color=YELLOW)
        rotulo.next_to(linea_phi, RIGHT)
        grafica = ejes.plot_line_graph(list(range(1, 14)), razones,
                                       line_color=TEAL_C)
        titulo = MathTex(r"F_{n+1}/F_n \to \varphi").to_edge(UP)
        self.add(ejes, linea_phi, rotulo, titulo)
        self.play(Create(grafica), run_time=3)
        self.wait()
