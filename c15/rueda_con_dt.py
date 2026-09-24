from manim import *


class RuedaConDt(Scene):
    def construct(self):
        radios = VGroup(*[
            Line(ORIGIN, 2 * rotate_vector(RIGHT, k * TAU / 8))
            for k in range(8)
        ]).set_stroke(GREY_B, 2)
        marca = Dot(2 * RIGHT, radius=0.14, color=RED)
        rueda = VGroup(Circle(radius=2, color=BLUE), radios, marca)

        omega = PI / 2  # rad/s: un cuarto de vuelta por segundo

        def girar(m, dt):  # el nombre «dt» es obligatorio
            m.rotate(omega * dt, about_point=ORIGIN)

        rueda.add_updater(girar)
        self.add(rueda)
        self.wait(1)               # gira 1 s
        rueda.suspend_updating()   # congelada
        self.wait(1)
        rueda.resume_updating()    # vuelve a girar
        self.wait(1)
        rueda.remove_updater(girar)  # se detiene para siempre
        self.wait(0.5)

        # Comprobación: 2 s de giro efectivo = 2 * 90° = 180°
        arco = Arc(radius=2.5, angle=PI, color=YELLOW)
        rotulo = MathTex(r"\omega\,t = 180^\circ", color=YELLOW)
        rotulo.next_to(arco, UP)
        self.play(Create(arco), Write(rotulo))
