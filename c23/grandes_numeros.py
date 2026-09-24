from manim import *


class GrandesNumeros(Scene):
    def construct(self):
        rng = np.random.default_rng(11)
        n_max = 500
        caras = rng.integers(0, 2, n_max)      # 1 = cara, 0 = sello
        n = np.arange(1, n_max + 1)
        proporcion = np.cumsum(caras) / n    # frecuencia acumulada

        ejes = Axes(
            x_range=[0, n_max, 100], y_range=[0, 1, 0.25],
            x_length=10, y_length=5, tips=False,
            axis_config={"include_numbers": True, "font_size": 26},
        ).shift(0.3 * DOWN)
        rotulos = ejes.get_axis_labels(
            MathTex("n", font_size=34),
            Tex("caras$/n$", font_size=34))
        teorico = DashedLine(ejes.c2p(0, 0.5), ejes.c2p(n_max, 0.5),
                             color=YELLOW)
        curva = ejes.plot_line_graph(n, proporcion,
                                     line_color=TEAL_C,
                                     add_vertex_dots=False,
                                     stroke_width=3)
        titulo = Tex("Ley de los grandes números",
                     font_size=42).to_edge(UP)

        self.add(ejes, rotulos, titulo)
        self.play(Create(teorico))
        self.play(Create(curva), run_time=4, rate_func=linear)
        final = MathTex(rf"\frac{{{caras.sum()}}}{{{n_max}}} = "
                        rf"{proporcion[-1]:.3f}", font_size=38)
        final.next_to(ejes.c2p(n_max, 0.5), UP + LEFT, buff=0.4)
        self.play(Write(final))
