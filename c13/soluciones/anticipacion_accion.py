from manim import *


class AnticipacionAccion(Scene):
    def construct(self):
        meta = Line(2.5 * UP, 2.5 * DOWN, color=GRAY_B)
        meta.shift(5 * RIGHT)
        bola = Dot([-4, 1, 0], radius=0.3, color=BLUE)
        testigo = Dot([-4, -1, 0], radius=0.3, color=GRAY_B)
        rotulos = VGroup(
            Text("anticipación, acción, reacción", font_size=28)
            .next_to(bola, UP, 0.4, aligned_edge=LEFT),
            Text("lineal", font_size=28)
            .next_to(testigo, UP, 0.4, aligned_edge=LEFT))
        self.add(meta, bola, testigo, rotulos)
        x0, x1 = -4, 4.4    # posiciones inicial y final
        t1, t2 = 0.6, 0.5   # anticipación lenta, acción rápida
        x_medio = x0 + (x1 - x0) * t1 / (t1 + t2)
        # 1. Anticipación: la bola retrocede despacio y suave;
        #    el testigo avanza a velocidad constante
        self.play(bola.animate(rate_func=smooth).shift(0.6 * LEFT),
                  testigo.animate(rate_func=linear).set_x(x_medio),
                  run_time=t1)
        # 2. Acción y 3. reacción: sale disparada, se pasa, vuelve
        rebote = rate_functions.ease_out_back
        self.play(bola.animate(rate_func=rebote).set_x(x1),
                  testigo.animate(rate_func=linear).set_x(x1),
                  run_time=t2)
        self.wait()
