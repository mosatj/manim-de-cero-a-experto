from manim import *


class Resorte(VMobject):
    """Muelle en zigzag entre dos puntos, con `vueltas` espiras."""

    def __init__(self, inicio=LEFT, fin=RIGHT, vueltas=8, ancho=.35,
                 extremo=0.25, **kwargs):
        # ¡Antes de super()!: __init__ llamará a generate_points()
        self.inicio, self.fin = np.array(inicio), np.array(fin)
        self.vueltas, self.ancho = vueltas, ancho
        self.extremo = extremo
        super().__init__(**kwargs)

    def generate_points(self):
        eje = self.fin - self.inicio
        largo = np.linalg.norm(eje)
        u = eje / largo                       # dirección del muelle
        n = np.array([-u[1], u[0], 0])        # normal (girada 90°)
        e = min(self.extremo, largo / 4)      # tramos rectos
        vertices = [self.inicio, self.inicio + e * u]
        pasos = 2 * self.vueltas
        for k in range(pasos):
            s = e + (k + 0.5) * (largo - 2 * e) / pasos
            lado = self.ancho if k % 2 == 0 else -self.ancho
            vertices.append(self.inicio + s * u + lado * n)
        vertices += [self.fin - e * u, self.fin]
        self.set_points_as_corners(vertices)
        return self

    def poner_extremos(self, inicio, fin):
        """Regenera la geometría con otros extremos (updaters)."""
        self.inicio, self.fin = np.array(inicio), np.array(fin)
        self.clear_points()
        self.generate_points()
        return self


class EscenaResorte(Scene):
    def construct(self):
        pared = Line(UP * 1.2, DOWN * 1.2, stroke_width=6)
        pared.shift(LEFT * 5)
        suelo = Line([-5, -0.6, 0], [5, -0.6, 0], color=GRAY)
        bloque = Square(1.2, color=BLUE, fill_opacity=0.7)
        bloque.next_to(suelo, UP, buff=0).shift(RIGHT * 1)
        resorte = Resorte(pared.get_center(), bloque.get_left(),
                          color=YELLOW, stroke_width=4)
        resorte.add_updater(lambda r: r.poner_extremos(
            pared.get_center(), bloque.get_left()))
        self.add(pared, suelo, bloque, resorte)
        # Oscilación amortiguada: x(t) = A e^(-0.3 t) cos(3 t)
        reloj = ValueTracker(0)
        x0 = bloque.get_x()
        bloque.add_updater(lambda b: b.set_x(
            x0 + 2.2 * np.exp(-0.3 * reloj.get_value())
            * np.cos(3 * reloj.get_value())))
        self.play(reloj.animate.set_value(4.9), run_time=4.9,
                  rate_func=linear)
        self.wait()
