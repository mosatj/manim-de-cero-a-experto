from manim import *


class DibujarConLapiz(Animation):
    """Como Create, pero con un «lápiz» luminoso en la punta."""

    def __init__(self, curva, color_lapiz=YELLOW, quitar_lapiz=True,
                 **kwargs):
        self.curva = curva
        self.lapiz = Dot(radius=0.09, color=color_lapiz)
        self.halo = Dot(radius=0.22, color=color_lapiz,
                        fill_opacity=0.3)
        self.quitar_lapiz = quitar_lapiz
        # El mobject de la animación es el grupo curva + lápiz
        grupo = VGroup(curva, self.halo, self.lapiz)
        super().__init__(grupo, introducer=True, **kwargs)

    def interpolate_mobject(self, alpha):
        t = self.rate_func(alpha)
        curva_inicial = self.starting_mobject[0]
        self.curva.pointwise_become_partial(curva_inicial, 0, t)
        punta = curva_inicial.point_from_proportion(t)
        self.lapiz.move_to(punta)
        self.halo.move_to(punta)

    def clean_up_from_scene(self, scene):
        super().clean_up_from_scene(scene)
        if self.quitar_lapiz:
            scene.remove(self.mobject)  # quita el grupo completo...
            scene.add(self.curva)        # ...y deja solo la curva


class EscenaLapiz(Scene):
    def construct(self):
        corazon = ParametricFunction(
            lambda t: 0.18 * np.array([
                16 * np.sin(t) ** 3,
                13 * np.cos(t) - 5 * np.cos(2 * t)
                - 2 * np.cos(3 * t) - np.cos(4 * t),
                0]),
            t_range=[0, TAU], color=RED)
        corazon.shift(LEFT * 3.2)
        espiral = ParametricFunction(
            lambda t: .28 * t * np.array([np.cos(t), np.sin(t), 0]),
            t_range=[0, 4 * PI], color=BLUE)
        espiral.shift(RIGHT * 3.2)
        self.play(DibujarConLapiz(corazon), run_time=3)
        # El segundo lápiz se queda en la punta (último fotograma)
        self.play(DibujarConLapiz(espiral, quitar_lapiz=False),
                  run_time=3, rate_func=linear)
        self.wait()
