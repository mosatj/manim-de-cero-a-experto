from manim import *


class Deslizador(VGroup):
    """Control deslizante: pista, botón y valor actual."""

    def __init__(self, nombre, minimo, maximo, inicial, ancho=3,
                 color=YELLOW, **kwargs):
        super().__init__(**kwargs)
        self.min, self.max = minimo, maximo
        self.valor = ValueTracker(inicial)  # «tiene un» tracker
        self.pista = Line(ORIGIN, ancho * RIGHT, color=GREY_B)
        self.boton = Dot(radius=0.12, color=color)
        self.rotulo = MathTex(nombre + "=", font_size=36)
        self.numero = DecimalNumber(inicial, font_size=36)
        self.add(self.pista, self.rotulo, self.numero, self.boton)
        self.boton.add_updater(lambda m: m.move_to(self.posicion()))
        self.numero.add_updater(lambda m: m.set_value(self.leer()))
        self.rotulo.always.next_to(self.pista, LEFT)
        self.numero.always.next_to(self.pista, RIGHT)
        self.update()  # coloca todo desde el principio

    def leer(self):
        return self.valor.get_value()

    def posicion(self):
        t = (self.leer() - self.min) / (self.max - self.min)
        return self.pista.point_from_proportion(np.clip(t, 0, 1))

    def mover_a(self, v):
        """Animación que lleva el deslizador al valor v."""
        return self.valor.animate.set_value(v)


class ParabolaConDeslizadores(Scene):
    def construct(self):
        ejes = Axes(x_range=[-3, 3], y_range=[-2, 5], x_length=6,
                    y_length=6).to_edge(LEFT)
        a = Deslizador("a", -1, 2, 0.5).shift(RIGHT * 1.5 + UP)
        c = Deslizador("c", -2, 3, 0, color=TEAL).shift(RIGHT * 1.5)
        parabola = always_redraw(lambda: ejes.plot(
            lambda x: a.leer() * x**2 + c.leer(),
            x_range=[-3, 3], color=YELLOW))
        formula = MathTex(r"y = a x^2 + c").next_to(a, UP, buff=0.8)
        self.add(ejes, a, c, parabola, formula)
        self.play(a.mover_a(1.5))
        self.play(c.mover_a(-1.5))
        self.play(a.mover_a(-0.6), c.mover_a(2.5), run_time=2)
