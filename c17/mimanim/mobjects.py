"""Mobjects propios de mimanim (capítulo 17)."""
from manim import *

__all__ = ["Resorte", "Medidor"]


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


class Medidor(VGroup):
    """Barra de progreso con su porcentaje; valor entre 0 y 100."""

    def __init__(self, valor=0, ancho=8, alto=0.5, color=GREEN,
                 **kwargs):
        super().__init__(**kwargs)
        self.ancho, self.valor = ancho, valor
        self.marco = RoundedRectangle(corner_radius=alto / 2,
                                      width=ancho, height=alto,
                                      color=GRAY_B)
        self.barra = Rectangle(width=ancho, height=alto * 0.7,
                               stroke_width=0, fill_color=color,
                               fill_opacity=1)
        self.cifra = DecimalNumber(valor, num_decimal_places=0,
                                   unit=r"\%", font_size=40)
        self.add(self.marco, self.barra, self.cifra)
        self._colocar()

    def _colocar(self):
        # Todo se deduce de self.valor: dibujar = función del estado
        izquierda = self.marco.get_left() + RIGHT * 0.1
        largo = max(self.valor / 100 * (self.ancho - 0.2), 1e-3)
        self.barra.stretch_to_fit_width(largo)
        self.barra.move_to(izquierda, aligned_edge=LEFT)
        self.cifra.set_value(self.valor)
        self.cifra.next_to(self.marco, RIGHT, buff=0.3)
        return self

    def fijar_valor(self, valor):
        self.valor = valor
        return self._colocar()

    @override_animate(fijar_valor)
    def _animar_fijar_valor(self, valor, anim_args=None):
        # medidor.animate.fijar_valor(v) llega aquí
        inicio = self.valor
        def paso(m, a):
            m.fijar_valor(interpolate(inicio, valor, a))
        return UpdateFromAlphaFunc(self, paso, **(anim_args or {}))
