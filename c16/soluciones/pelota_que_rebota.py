from manim import *

G, E, H = 9.8, 0.8, 0.001   # gravedad, restitución, paso fijo


class PelotaQueRebota(Scene):
    def construct(self):
        suelo = -3
        pelota = Dot([-5.5, 3, 0], radius=0.15, color=YELLOW)
        pelota.vel = np.array([1.6, 0, 0])
        pelota.reserva = 0.0

        def avanzar(m, dt):
            m.reserva += dt
            while m.reserva >= H:
                m.vel = m.vel + H * np.array([0, -G, 0])
                m.shift(H * m.vel)
                if m.get_y() < suelo:              # evento: choque
                    m.set_y(suelo)
                    m.vel[1] = -E * m.vel[1]      # pierde el 20 %
                m.reserva -= H

        pelota.add_updater(avanzar)
        rastro = TracedPath(pelota.get_center, stroke_color=YELLOW)
        piso = Line([-6.5, suelo, 0], [6.5, suelo, 0])
        self.add(piso, pelota, rastro)
        self.wait_until(lambda: pelota.get_x() > 5.5, max_time=15)
