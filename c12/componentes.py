"""Componentes reutilizables para las escenas del capítulo 12.

Este archivo NO contiene escenas: solo clases que heredan de VGroup.
Se importa desde otras escenas con  from componentes import Tarjeta
"""
from manim import *

__all__ = ["Tarjeta", "Reloj", "Balanza", "EjeEtiquetado"]


class Tarjeta(VGroup):
    """Un título y una fórmula dentro de un marco redondeado."""

    def __init__(self, titulo, formula, color=BLUE, ancho_min=4,
                 **kwargs):
        super().__init__(**kwargs)             # primero, la madre
        self.titulo = Text(titulo, font_size=28, color=color)
        self.formula = MathTex(formula, font_size=44)
        contenido = VGroup(self.titulo, self.formula)
        contenido.arrange(DOWN, buff=0.3)
        self.marco = RoundedRectangle(
            corner_radius=0.2,
            width=max(ancho_min, contenido.width + 0.6),
            height=contenido.height + 0.6,
            stroke_color=color,
        ).set_fill(color, opacity=0.12)
        self.marco.move_to(contenido)
        self.add(self.marco, self.titulo, self.formula)

    def resaltar(self, color=YELLOW):
        """Cambia el color del marco; devuelve self."""
        self.marco.set_stroke(color, width=6)
        return self


class Reloj(VGroup):
    """Esfera con marcas y dos agujas que saben poner la hora."""

    def __init__(self, radio=2, color=WHITE, horas=12, minutos=0,
                 **kwargs):
        super().__init__(**kwargs)
        self.radio = radio
        self.esfera = Circle(radius=radio, color=color)
        self.marcas = VGroup(*[
            Line(0.85 * radio * UP, radio * UP,
                 stroke_width=6 if k % 3 == 0 else 2,
                 color=color).rotate(-k * PI/6, about_point=ORIGIN)
            for k in range(12)
        ])
        self.aguja_h = Line(ORIGIN, .5 * radio * UP, stroke_width=8,
                            color=BLUE)
        self.aguja_m = Line(ORIGIN, .8 * radio * UP, stroke_width=5,
                            color=YELLOW)
        self.eje = Dot(color=color)
        self.horas, self.minutos = 12, 0
        self.add(self.esfera, self.marcas, self.aguja_h,
                 self.aguja_m, self.eje)
        self.poner_hora(horas, minutos)

    @staticmethod
    def _angulos(h, m):
        """Ángulos de las dos agujas, desde las 12."""
        total = (h % 12) * 60 + m      # minutos desde las 12
        return -TAU * total / 720, -TAU * m / 60

    def poner_hora(self, h, m=0):
        """Coloca las agujas en h:m al instante; devuelve self."""
        centro = self.esfera.get_center()
        ang_h, ang_m = self._angulos(h, m)
        for aguja, f, a in [(self.aguja_h, 0.5, ang_h),
                                  (self.aguja_m, 0.8, ang_m)]:
            punta = centro + f * self.radio * rotate_vector(UP, a)
            aguja.put_start_and_end_on(centro, punta)
        self.horas, self.minutos = h, m
        return self

    def animar_hora(self, h, m=0, **kwargs):
        """Devuelve la animación que lleva las agujas a h:m."""
        antes = (self.horas % 12) * 60 + self.minutos
        despues = (h % 12) * 60 + m
        pasados = (despues - antes) % 720   # siempre hacia delante
        c = self.esfera.get_center()
        self.horas, self.minutos = h, m
        return AnimationGroup(
            Rotate(self.aguja_m, -TAU * pasados/60, about_point=c),
            Rotate(self.aguja_h, -TAU * pasados/720, about_point=c),
            **kwargs,
        )


class Balanza(VGroup):
    """Balanza de brazos: un fulcro y un brazo con dos platillos."""

    def __init__(self, largo=6, color=GRAY_B, **kwargs):
        super().__init__(**kwargs)
        self.fulcro = Triangle(color=color, fill_opacity=1)
        arriba = self.fulcro.scale(0.5).get_top()
        self.brazo = Line(arriba + largo / 2 * LEFT,
                          arriba + largo / 2 * RIGHT,
                          stroke_width=6, color=color)
        self.platos = VGroup(*[
            Rectangle(width=1.6, height=0.12, color=color,
                      fill_opacity=1).next_to(extremo, UP, buff=0)
            for extremo in self.brazo.get_start_and_end()
        ])
        self.cargas = VGroup(VGroup(), VGroup())   # izq. y der.
        self.movil = VGroup(self.brazo, self.platos, self.cargas)
        self.angulo = 0
        self.add(self.fulcro, self.movil)

    @property
    def pivote(self):
        """Punto de giro, calculado cada vez: sigue al fulcro."""
        return self.fulcro.get_top()

    def poner(self, lado, objeto):
        """Pone un objeto en el platillo 0 (izq.) o 1 (der.)."""
        pila = self.cargas[lado]
        base = pila if len(pila) else self.platos[lado]
        objeto.next_to(base, UP, buff=0.05)
        pila.add(objeto)
        return self

    def animar_inclinacion(self, angulo, **kwargs):
        """Gira la parte móvil hasta el ángulo dado (radianes)."""
        giro = angulo - self.angulo
        self.angulo = angulo
        return Rotate(self.movil, giro, about_point=self.pivote,
                      **kwargs)


class EjeEtiquetado(VGroup):
    """Recta numérica con nombre y marcas con rótulo."""

    def __init__(self, x_min=-5, x_max=5, nombre="x", **kwargs):
        super().__init__(**kwargs)
        self.recta = NumberLine(x_range=[x_min, x_max, 1],
                                length=x_max - x_min,
                                include_numbers=True, font_size=28)
        self.nombre = MathTex(nombre).next_to(self.recta, RIGHT)
        self.marcas = VGroup()
        self.add(self.recta, self.nombre, self.marcas)

    def marcar(self, x, rotulo, color=YELLOW):
        """Añade un punto en x con su rótulo; devuelve self."""
        punto = Dot(self.recta.n2p(x), color=color)
        texto = MathTex(rotulo, color=color, font_size=36)
        texto.next_to(punto, UP, buff=0.25)
        self.marcas.add(VGroup(punto, texto))
        return self
