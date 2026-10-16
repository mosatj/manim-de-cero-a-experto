from manim import *
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(3)
MUESTRA = rng.normal(0, 1, 500)


class HistogramaPatches(Scene):
    def construct(self):
        # matplotlib decide los intervalos y las alturas
        alturas, bordes, barras = plt.hist(MUESTRA, bins=14)
        ejes = Axes(x_range=[-4, 4, 1], y_range=[0, 120, 20],
                    x_length=10, y_length=5, tips=False)
        rectangulos = VGroup()
        for barra in barras:          # cada patch es un Rectangle
            x0, y0 = barra.get_x(), 0
            x1 = x0 + barra.get_width()
            y1 = barra.get_height()
            r = Polygon(ejes.c2p(x0, y0), ejes.c2p(x1, y0),
                        ejes.c2p(x1, y1), ejes.c2p(x0, y1),
                        fill_color=BLUE_C, fill_opacity=0.7,
                        stroke_color=WHITE, stroke_width=1)
            rectangulos.add(r)
        self.add(ejes)
        self.play(LaggedStart(*[GrowFromEdge(r, DOWN)
                                for r in rectangulos],
                              lag_ratio=0.1))
        self.add(Text(f"{len(barras)} intervalos, "
                      f"{int(alturas.sum())} datos",
                      font_size=26).to_edge(DOWN))
        self.wait()
