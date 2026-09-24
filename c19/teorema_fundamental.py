from manim import *


class TeoremaFundamental(Scene):
    def construct(self):
        f = np.cos
        F = np.sin                  # F(x) = ∫_0^x cos t dt = sen x
        arriba = Axes(x_range=[0, 6.5, 1], y_range=[-1.5, 1.5, 1],
                      x_length=9, y_length=3, tips=False)
        arriba.add_coordinates(font_size=20)
        abajo = arriba.copy()
        paneles = VGroup(arriba, abajo).arrange(DOWN, buff=0.7)
        paneles.shift(1.8 * RIGHT)
        curva = arriba.plot(f, x_range=[0, 6.5], color=BLUE)
        nom_f = MathTex(r"f(t)=\cos t", color=BLUE)
        nom_F = MathTex(r"F(x)=\int_0^x f(t)\,dt", color=GREEN)
        nom_f.scale(0.7).next_to(arriba, LEFT, buff=0.2)
        nom_F.scale(0.7).next_to(abajo, LEFT, buff=0.2)

        x = ValueTracker(0.01)
        # Área con signo: azul donde f > 0, rojo donde f < 0
        cortes = [0, PI / 2, 3 * PI / 2, 6.5]
        def area():
            trozos = VGroup()
            for i in range(3):
                izq = cortes[i]
                der = min(cortes[i + 1], x.get_value())
                if der > izq + 1e-3:
                    trozos.add(arriba.get_area(
                        curva, x_range=[izq, der], opacity=0.5,
                        color=RED if i == 1 else BLUE))
            return trozos
        sombra = always_redraw(area)
        borde = always_redraw(lambda: arriba.get_vertical_line(
            arriba.i2gp(x.get_value(), curva), color=YELLOW))

        rastro = always_redraw(lambda: abajo.plot(
            F, x_range=[0, x.get_value()], color=GREEN))
        punto = always_redraw(lambda: Dot(
            abajo.c2p(x.get_value(), F(x.get_value())), color=RED))
        # Pendiente de F en x = altura de f en x  (F' = f)
        def tangente():
            x0 = x.get_value()
            p = abajo.c2p(x0, F(x0))
            d = abajo.c2p(x0 + 1, F(x0) + f(x0)) - p
            d = 0.8 * d / np.linalg.norm(d)
            return Line(p - d, p + d, color=YELLOW)
        tang = always_redraw(tangente)
        tfc = MathTex(r"F'(x)=f(x)", color=YELLOW)
        tfc.next_to(nom_F, DOWN, buff=0.5)

        self.play(Create(arriba), Create(abajo), Create(curva),
                  Write(nom_f), Write(nom_F))
        self.add(sombra, borde, rastro, punto, tang)
        self.play(x.animate.set_value(PI / 2), run_time=2,
                  rate_func=linear)
        self.play(x.animate.set_value(3 * PI / 2), run_time=3,
                  rate_func=linear)
        self.play(x.animate.set_value(5.6), run_time=2,
                  rate_func=linear)
        self.play(Write(tfc))
