from manim import *


class SumasRiemann(Scene):
    def construct(self):
        a, b = 0, 3
        f = lambda x: 2 * (x - 1)**2 - (x - 1)**3 + 3
        exacto = 45 / 4                      # ∫_0^3 f(x) dx = 11,25
        ejes = Axes(x_range=[-0.5, 3.5, 1], y_range=[0, 7, 1],
                    x_length=7, y_length=6, tips=False)
        ejes.add_coordinates(font_size=24).to_edge(LEFT, buff=0.5)
        curva = ejes.plot(f, x_range=[-0.1, 3.3], color=WHITE)

        n = ValueTracker(4)
        entero = lambda: int(round(n.get_value()))

        def suma_izquierda(k):
            dx = (b - a) / k
            return sum(f(a + i * dx) for i in range(k)) * dx

        def rectangulos_n():
            k = entero()
            dx = (b - a) / k
            # Tope b − dx/2: np.arange no añade un rectángulo de más
            return ejes.get_riemann_rectangles(
                curva, x_range=[a, b - dx / 2], dx=dx,
                input_sample_type="left", color=[BLUE, TEAL],
                fill_opacity=0.7, stroke_width=0.5)
        rectangulos = always_redraw(rectangulos_n)

        v_n = Integer(4)
        v_n.add_updater(lambda m: m.set_value(entero()))
        v_s = DecimalNumber(suma_izquierda(4), num_decimal_places=4)
        v_s.add_updater(
            lambda m: m.set_value(suma_izquierda(entero())))
        v_e = DecimalNumber(0, num_decimal_places=4, color=RED)
        v_e.add_updater(lambda m: m.set_value(
            abs(suma_izquierda(entero()) - exacto)))
        filas = VGroup(
            VGroup(MathTex("n ="), v_n),
            VGroup(MathTex(r"S_n ="), v_s),
            VGroup(MathTex(r"|S_n - I| =", color=RED), v_e))
        for fila in filas:
            fila.arrange(RIGHT)
        suma = MathTex(r"S_n=\sum_{i=0}^{n-1} f(x_i)\,\Delta x")
        panel = VGroup(suma, *filas)
        panel.arrange(DOWN, aligned_edge=LEFT)
        panel.shift(UP)
        integral = MathTex(r"I=\int_0^3 f(x)\,dx=\frac{45}{4}",
                           color=YELLOW)
        integral.next_to(panel, DOWN, buff=0.5)
        integral.align_to(panel, LEFT)
        VGroup(panel, integral).to_edge(RIGHT, buff=0.3)

        self.play(Create(ejes), Create(curva))
        self.play(FadeIn(rectangulos), Write(panel))
        self.add(curva)                     # la curva, por encima
        for k in [8, 16, 32, 64]:
            self.play(n.animate.set_value(k), run_time=1.5)
        self.play(Write(integral))
