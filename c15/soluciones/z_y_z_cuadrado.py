from manim import *


class ZYZCuadrado(Scene):
    def construct(self):
        plano = ComplexPlane(x_range=[-4, 4], y_range=[-3, 3])
        plano.add_coordinates()
        z = ComplexValueTracker(1)
        punto = always_redraw(lambda: Dot(
            plano.n2p(z.get_value()), color=YELLOW))
        cuadrado = always_redraw(lambda: Dot(
            plano.n2p(z.get_value() ** 2), color=RED))
        rastro = TracedPath(cuadrado.get_center, stroke_color=RED)
        self.add(plano, rastro, punto, cuadrado)
        # Recorremos un arco de la circunferencia de radio 1.5
        for angulo in np.linspace(0, PI / 2, 10)[1:]:
            destino = 1.5 * np.exp(1j * angulo)
            self.play(z.animate.set_value(destino), run_time=0.3,
                      rate_func=linear)
