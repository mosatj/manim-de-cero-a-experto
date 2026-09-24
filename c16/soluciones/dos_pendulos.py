from manim import *

G, L, H = 9.8, 2.5, 0.001


class DosPendulos(Scene):
    def construct(self):
        reloj = ValueTracker(0)
        pendulos = VGroup()
        for grados, x, color in [(30, -3, BLUE), (150, 3, YELLOW)]:
            pivote = np.array([x, 2.5, 0])
            p = VGroup(Line(pivote, pivote + L * DOWN, color=color),
                       Dot(pivote + L * DOWN, radius=0.16,
                           color=color))
            p.theta, p.omega = grados * DEGREES, 0.0
            p.reserva, p.pivote = 0.0, pivote

            def avanzar(m, dt):
                m.reserva += dt
                while m.reserva >= H:
                    m.omega -= H * G / L * np.sin(m.theta)
                    m.theta += H * m.omega
                    m.reserva -= H
                extremo = m.pivote + L * np.array(
                    [np.sin(m.theta), -np.cos(m.theta), 0])
                m[0].put_start_and_end_on(m.pivote, extremo)
                m[1].move_to(extremo)

            p.add_updater(avanzar, call_updater=True)
            pendulos.add(p)
        reloj.add_updater(lambda m, dt: m.increment_value(dt))
        rotulos = VGroup(MathTex(r"30^\circ").move_to([-3, 3.4, 0]),
                         MathTex(r"150^\circ").move_to([3, 3.4, 0]))
        self.add(reloj, pendulos, rotulos)
        # Dos períodos del pequeño; el grande va muy retrasado
        T0 = TAU * np.sqrt(L / G)
        self.wait_until(lambda: reloj.get_value() >= 2 * T0)
