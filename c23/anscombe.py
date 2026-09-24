from manim import *


class CuartetoAnscombe(Scene):
    def construct(self):
        datos = np.loadtxt("datos/anscombe.csv", delimiter=",",
                           skiprows=1)
        paneles = VGroup()
        for i in range(4):
            x, y = datos[:, 2 * i], datos[:, 2 * i + 1]
            m, b = np.polyfit(x, y, 1)
            ejes = Axes(x_range=[2, 20, 4], y_range=[2, 14, 4],
                        x_length=5, y_length=2.6, tips=False,
                        axis_config={"include_numbers": True,
                                     "font_size": 20})
            nube = VGroup(*[Dot(ejes.c2p(a, c), radius=0.055,
                                color=TEAL_B)
                            for a, c in zip(x, y)])
            recta = ejes.plot(lambda t: m * t + b, x_range=[3, 20],
                              color=YELLOW, stroke_width=3)
            nombre = Tex(["I", "II", "III", "IV"][i], font_size=30)
            nombre.next_to(ejes.c2p(2, 14), RIGHT, buff=0.35)
            paneles.add(VGroup(ejes, nube, recta, nombre))
        paneles.arrange_in_grid(2, 2, buff=(0.8, 0.5))
        paneles.to_edge(DOWN, buff=0.3)
        resumen = MathTex(
            r"\bar x = 9,\quad \bar y \approx 7{,}50,\quad "
            r"y \approx 3 + 0{,}5\,x,\quad r \approx 0{,}82",
            font_size=34).to_edge(UP, buff=0.3)

        self.play(Write(resumen))
        for ejes, nube, recta, nombre in paneles:
            self.play(Create(ejes), FadeIn(nombre), run_time=0.6)
            puntos = [GrowFromCenter(p) for p in nube]
            self.play(LaggedStart(*puntos, lag_ratio=0.08),
                      run_time=0.8)
            self.play(Create(recta), run_time=0.6)
        self.wait()
