from manim import *


class SuperficieConCurvas(VGroup):
    """Componente: superficie z = f(x, y) y sus curvas de nivel."""

    def __init__(self, ejes, f, niveles, rango=(-3, 3), **kwargs):
        super().__init__(**kwargs)
        self.ejes, self.f = ejes, f
        self.superficie = ejes.plot_surface(
            f, u_range=rango, v_range=rango, resolution=(20, 20),
            fill_opacity=0.6, checkerboard_colors=[TEAL_D, TEAL_E])
        self.altas = VGroup(*[self._curva(c, c, rango)
                              for c in niveles])
        self.bajas = VGroup(*[self._curva(c, 0, rango)
                              for c in niveles])
        self.add(self.superficie, self.altas)

    def _curva(self, c, altura, rango):
        curva = ImplicitFunction(lambda x, y: self.f(x, y) - c,
                                 x_range=rango, y_range=rango)
        curva.apply_function(
            lambda p: self.ejes.c2p(p[0], p[1], altura))
        return curva.set_stroke(YELLOW, 3)

    def proyectar(self, **kwargs):
        """Animación: las curvas bajan hasta el plano z = 0."""
        return ReplacementTransform(self.altas, self.bajas,
                                    **kwargs)


class UsoDelComponente(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3],
                          z_range=[0, 3], x_length=6, y_length=6,
                          z_length=3)
        cerro = SuperficieConCurvas(
            ejes, lambda x, y: 2.5 * np.exp(-(x**2 + y**2) / 3),
            niveles=[0.5, 1, 1.5, 2])
        self.set_camera_orientation(phi=65 * DEGREES,
                                    theta=-60 * DEGREES)
        self.add(ejes, cerro)
        self.play(cerro.proyectar(run_time=2))
