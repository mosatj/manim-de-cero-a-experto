from manim import *


class EspiralFibonacci(Scene):
    def construct(self):
        fib = [1, 1]
        while len(fib) < 8:
            fib.append(fib[-1] + fib[-2])   # 1, 1, 2, 3, 5, ..., 21
        # Cada cuadrado se pega al grupo en una dirección que
        # gira; su arco es un cuarto de circunferencia centrado
        # en una esquina: (dirección, esquina, ángulo inicial)
        pasos = [(DOWN, UR, PI), (RIGHT, UL, -PI / 2),
                 (UP, DL, 0), (LEFT, DR, PI / 2)]
        cuadrados, arcos, numeros = VGroup(), VGroup(), VGroup()
        for k, lado in enumerate(fib):
            direccion, esquina, angulo = pasos[k % 4]
            relleno = interpolate_color(BLUE_E, TEAL_C, k / 8)
            c = Square(lado, stroke_color=WHITE, stroke_width=2,
                       fill_color=relleno, fill_opacity=0.8)
            if k > 0:
                c.next_to(cuadrados, direccion, buff=0)
            cuadrados.add(c)
            arcos.add(Arc(radius=lado, start_angle=angulo,
                          angle=PI / 2, color=YELLOW,
                          arc_center=c.get_corner(esquina)))
            n = MathTex(str(lado))
            n.scale_to_fit_height(min(0.3 * lado, 2.5)).move_to(c)
            numeros.add(n)
        todo = VGroup(cuadrados, numeros, arcos)
        todo.scale_to_fit_height(5).center().to_edge(LEFT, buff=0.6)
        arcos.set_stroke(width=6)

        for c, n in zip(cuadrados, numeros):
            self.play(GrowFromCenter(c), FadeIn(n), run_time=0.5)
        self.play(Create(arcos, lag_ratio=1), run_time=3,
                  rate_func=linear)
        razon = MathTex(rf"\frac{{{fib[-1]}}}{{{fib[-2]}}} \approx "
                        rf"{fib[-1] / fib[-2]:.4f}", font_size=44)
        phi = MathTex(r"\varphi = \frac{1+\sqrt5}{2}\approx 1.6180",
                      font_size=44, color=YELLOW)
        texto = VGroup(razon, phi).arrange(DOWN, buff=0.6)
        texto.to_edge(RIGHT, buff=0.6)
        self.play(Write(razon), Write(phi))
        self.wait()
