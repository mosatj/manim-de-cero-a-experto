from manim import *


class RiemannRaiz(Scene):
    def construct(self):
        f = np.sqrt
        n, a, b = 10, 0, 4
        dx = (b - a) / n
        paneles = VGroup()
        tipos = [("left", "izquierda"), ("center", "medio"),
                 ("right", "derecha")]
        for tipo, nombre in tipos:
            ejes = Axes(x_range=[0, 4, 1], y_range=[0, 2, 1],
                        x_length=3.8, y_length=2.6, tips=False)
            curva = ejes.plot(f, x_range=[0, 4], color=WHITE)
            rects = ejes.get_riemann_rectangles(
                curva, x_range=[a, b - dx / 2], dx=dx,
                input_sample_type=tipo, fill_opacity=0.7)
            desfase = {"left": 0, "center": 0.5, "right": 1}[tipo]
            puntos = [a + (i + desfase) * dx for i in range(n)]
            suma = sum(f(x) for x in puntos) * dx
            rotulo = MathTex(rf"\text{{{nombre}}}:\ {suma:.4f}",
                             font_size=30).next_to(ejes, DOWN)
            paneles.add(VGroup(ejes, rects, curva, rotulo))
        paneles.arrange(RIGHT, buff=0.5)
        exacto = MathTex(
            r"\int_0^4\sqrt{x}\,dx=\frac{16}{3}\approx 5.3333",
                         color=YELLOW).to_edge(UP)
        self.add(paneles, exacto)
