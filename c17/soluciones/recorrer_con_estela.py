from manim import *


class RecorrerConEstela(Animation):
    """Un punto recorre `camino` con una estela de longitud fija."""

    def __init__(self, punto, camino, estela=0.15, **kwargs):
        self.punto, self.camino, self.estela = punto, camino, estela
        self.rastro = camino.copy().set_stroke(width=6, opacity=1)
        grupo = VGroup(self.rastro, punto)
        super().__init__(grupo, introducer=True, **kwargs)

    def interpolate_mobject(self, alpha):
        t = self.rate_func(alpha)
        self.punto.move_to(self.camino.point_from_proportion(t))
        # La estela es el tramo [t - estela, t] del camino original
        self.rastro.pointwise_become_partial(
            self.camino, max(0, t - self.estela), t)

    def clean_up_from_scene(self, scene):
        super().clean_up_from_scene(scene)
        scene.remove(self.rastro)       # solo queda el punto


class EscenaEstela(Scene):
    def construct(self):
        lemniscata = ParametricFunction(
            lambda t: 3 * np.array(
                [np.cos(t), np.sin(t) * np.cos(t), 0])
            / (1 + np.sin(t) ** 2),
            t_range=[0, TAU], color=GRAY, stroke_opacity=0.4)
        punto = Dot(color=YELLOW, radius=0.12)
        self.add(lemniscata)
        camino = lemniscata.copy().set_color(BLUE)
        self.play(RecorrerConEstela(punto, camino, estela=0.2),
                  run_time=4, rate_func=linear)
        # Último fotograma: la animación congelada al 70 %
        anim2 = RecorrerConEstela(punto, lemniscata.copy()
                                  .set_color(BLUE), estela=0.2)
        anim2._setup_scene(self)
        anim2.begin()
        anim2.interpolate(0.7)
