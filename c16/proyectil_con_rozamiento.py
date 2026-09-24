from manim import *

G, K, H = 9.8, 0.12, 0.002   # gravedad, rozamiento, paso fijo (s)


class Proyectil(Dot):
    def __init__(self, v0, angulo, k, origen, **kwargs):
        super().__init__(origen, **kwargs)
        self.origen, self.pos = origen, np.zeros(3)
        self.vel = v0 * rotate_vector(RIGHT, angulo)
        self.k, self.reserva, self.en_suelo = k, 0.0, False
        self.add_updater(Proyectil.avanzar)

    def paso(self, h):
        # a = g + rozamiento proporcional a |v| v (opuesto a v)
        rapidez = np.linalg.norm(self.vel)
        a = np.array([0, -G, 0]) - self.k * rapidez * self.vel
        self.vel = self.vel + h * a              # semi-implícito
        self.pos = self.pos + h * self.vel
        if self.pos[1] < 0:                      # suceso: el suelo
            self.pos[1], self.en_suelo = 0, True

    def avanzar(self, dt):
        self.reserva += dt * 0.6                 # cámara lenta
        while self.reserva >= H and not self.en_suelo:
            self.paso(H)
            self.reserva -= H
        self.move_to(self.origen + self.pos)


class ProyectilConRozamiento(Scene):
    def construct(self):
        suelo = Line(LEFT * 6.5, RIGHT * 6.5, color=GREY)
        suelo.shift(DOWN * 3)
        bolas = VGroup(*[
            Proyectil(10, 55 * DEGREES, k, suelo.get_left() + RIGHT,
                      color=color, radius=0.1)
            for k, color in [(0, BLUE), (K, YELLOW)]])
        rastros = VGroup(*[TracedPath(b.get_center, stroke_width=3,
                                      stroke_color=b.color)
                           for b in bolas])
        self.add(suelo, bolas, rastros)
        self.wait_until(lambda: all(b.en_suelo for b in bolas),
                        max_time=10)
        alcances = VGroup(*[
            DecimalNumber(b.pos[0], unit=r"\mathrm{m}",
                          unit_buff_per_font_unit=0.003,
                          color=b.color)
            .next_to(b, DOWN) for b in bolas])
        self.play(FadeIn(alcances))
