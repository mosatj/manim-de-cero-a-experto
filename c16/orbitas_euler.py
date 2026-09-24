from manim import *

GM = 40.0     # intensidad de la gravedad del Sol
H = 0.02      # paso fijo de integración, en segundos


class Planeta(Dot):
    """Un punto que se mueve por gravedad, con paso fijo."""

    def __init__(self, posicion, velocidad, metodo, **kwargs):
        super().__init__(posicion, **kwargs)
        self.pos = np.array(posicion, dtype=float)
        self.vel = np.array(velocidad, dtype=float)
        self.metodo = metodo
        self.reserva = 0.0               # tiempo aún sin simular
        self.historia = [self.pos.copy()]
        self.add_updater(Planeta.avanzar)

    def aceleracion(self, p):
        return -GM * p / np.linalg.norm(p) ** 3

    def paso(self, h):
        a = self.aceleracion(self.pos)
        if self.metodo == "explícito":   # posición con v vieja
            self.pos = self.pos + h * self.vel
            self.vel = self.vel + h * a
        else:                            # semi-implícito: v nueva
            self.vel = self.vel + h * a
            self.pos = self.pos + h * self.vel

    def avanzar(self, dt):
        # dt puede valer 1/30, 1/60 o varios segundos: da igual,
        # siempre se integra con el mismo paso H
        self.reserva += dt
        while self.reserva >= H:
            self.paso(H)
            self.historia.append(self.pos.copy())
            self.reserva -= H
        self.move_to(self.pos)

    def rastro(self):
        linea = VMobject().set_points_as_corners(self.historia)
        return linea.set_stroke(self.color, 2)


class OrbitasEuler(Scene):
    def construct(self):
        v = 0.8 * np.sqrt(GM / 3)        # menos que la circular
        rojo = Planeta([3, 0, 0], [0, v, 0], "explícito", color=RED)
        verde = Planeta([3, 0, 0], [0, v, 0], "semi", color=GREEN)
        rastros = VGroup(always_redraw(rojo.rastro),
                         always_redraw(verde.rastro))
        leyenda = VGroup(Text("Euler explícito", color=RED),
                         Text("Euler semi-implícito", color=GREEN))
        leyenda.scale(0.45).arrange(DOWN, aligned_edge=LEFT)
        sol = Dot(radius=0.2, color=YELLOW)
        self.add(sol, rojo, verde, rastros, leyenda.to_corner(UL))
        self.wait(9)
