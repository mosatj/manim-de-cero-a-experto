from manim import *

G, L, H = 9.8, 3.0, 0.001    # m/s², longitud (m), paso fijo (s)


class Pendulo(VGroup):
    """Varilla y lenteja; theta se mide desde la vertical."""

    def __init__(self, theta0, pivote, color, lineal=False):
        super().__init__()
        self.theta, self.omega, self.t = theta0, 0.0, 0.0
        self.theta0, self.pivote = theta0, pivote
        self.lineal = lineal
        self.varilla = Line(pivote, pivote + L * DOWN, color=color)
        self.lenteja = Dot(radius=0.18, color=color)
        self.add(self.varilla, self.lenteja)
        self.reserva = 0.0
        self.add_updater(Pendulo.avanzar, call_updater=True)

    def extremo(self):
        return self.pivote + L * np.array(
            [np.sin(self.theta), -np.cos(self.theta), 0])

    def avanzar(self, dt):
        self.reserva += dt
        while self.reserva >= H:
            if self.lineal:      # péndulo ideal: fórmula exacta
                w = np.sqrt(G / L)
                self.theta = self.theta0 * np.cos(w * (self.t + H))
            else:                # péndulo real: Euler semi-impl.
                self.omega -= H * G / L * np.sin(self.theta)
                self.theta += H * self.omega
            self.t += H
            self.reserva -= H
        fin = self.extremo()
        self.varilla.put_start_and_end_on(self.pivote, fin)
        self.lenteja.move_to(fin)


class PenduloNoLineal(Scene):
    def construct(self):
        pivote = UP * 1.3
        real = Pendulo(120 * DEGREES, pivote, YELLOW)
        ideal = Pendulo(120 * DEGREES, pivote, GREY_B, lineal=True)
        ideal.set_opacity(0.5)
        rastro = TracedPath(real.lenteja.get_center,
                            stroke_color=YELLOW,
                            dissipating_time=0.8)
        reloj = DecimalNumber(0, unit=r"\mathrm{s}",
                              unit_buff_per_font_unit=0.003)
        reloj.to_corner(UR)
        reloj.add_updater(lambda m: m.set_value(real.t))
        self.add(Dot(pivote), ideal, real, rastro, reloj)
        for fin in [2, 4, 6]:
            self.wait_until(lambda: real.t >= fin)
