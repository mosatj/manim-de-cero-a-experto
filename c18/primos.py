from manim import *


def contar_primos(n_max):
    """pi(n) para n = 0..n_max con la criba de Eratóstenes."""
    es_primo = [False, False] + [True] * (n_max - 1)
    for p in range(2, int(n_max ** 0.5) + 1):
        if es_primo[p]:
            for multiplo in range(p * p, n_max + 1, p):
                es_primo[multiplo] = False
    conteo, total = [], 0
    for n in range(n_max + 1):
        total += es_primo[n]
        conteo.append(total)
    return conteo


class Primos(Scene):
    def construct(self):
        N = 100
        pi_n = contar_primos(N)
        ejes = Axes(x_range=[0, N, 10], y_range=[0, 30, 5],
                    x_length=10, y_length=5.5, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24,
                                 "stroke_color": GRAY_B})
        # Datos: una poligonal escalonada (un escalón por primo)
        xs, ys = [], []
        for n in range(1, N + 1):
            xs += [n, n]
            ys += [pi_n[n - 1], pi_n[n]]
        datos = ejes.plot_line_graph(xs, ys, line_color=YELLOW,
                                     add_vertex_dots=False,
                                     stroke_width=3)
        modelo = ejes.plot(lambda x: x / np.log(x), x_range=[2, N],
                           color=BLUE)
        # Rótulos directos, junto a cada curva (sin leyenda aparte)
        et_datos = MathTex(r"\pi(n)", color=YELLOW, font_size=36)
        et_datos.next_to(ejes.c2p(N, pi_n[N]), UP, buff=0.15)
        et_modelo = MathTex(r"\frac{n}{\ln n}", color=BLUE,
                            font_size=36)
        et_modelo.next_to(ejes.c2p(N, N / np.log(N)), RIGHT, 0.15)
        titulo = Text("Primos menores o iguales que n",
                      font_size=30)
        titulo.to_edge(UP, buff=0.3)
        self.add(ejes, titulo)
        self.play(Create(datos), run_time=3, rate_func=linear)
        self.play(Create(modelo), FadeIn(et_datos, et_modelo))
        self.wait()
