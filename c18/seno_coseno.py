from manim import *


class SenoCoseno(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 2 * PI, PI / 2],
                    y_range=[-1.5, 1.5, 1],
                    x_length=10, y_length=4.5, tips=False)
        # Rótulos del eje x en múltiplos de pi: un diccionario.
        # Las cadenas se componen con Tex (modo texto): van entre $
        marcas = {PI / 2: r"$\frac{\pi}{2}$", PI: r"$\pi$",
                  3 * PI / 2: r"$\frac{3\pi}{2}$",
                  2 * PI: r"$2\pi$"}
        ejes.add_coordinates(marcas, None)  # None: los de siempre
        seno = ejes.plot(np.sin, color=BLUE)
        coseno = ejes.plot(np.cos, color=RED)
        et_seno = ejes.get_graph_label(seno, r"\sin x",
                                       x_val=PI / 2, direction=UP)
        et_coseno = ejes.get_graph_label(coseno, r"\cos x",
                                         x_val=2 * PI, direction=UR)
        self.add(ejes)
        self.play(Create(seno), Create(coseno), run_time=2)
        self.play(FadeIn(et_seno, et_coseno))
        self.wait()
