from manim import *


class BajarYDesaparecer(Animation):
    """Inversa de SubirYAparecer: cada pieza baja y se desvanece."""

    def __init__(self, mob, altura=0.4, lag_ratio=0.08, **kwargs):
        super().__init__(mob, lag_ratio=lag_ratio, remover=True,
                         **kwargs)
        self.altura = altura

    def interpolate_submobject(self, sub, sub_inicial, alpha):
        sub.points = sub_inicial.points + alpha * self.altura * DOWN
        sub.set_fill(
            opacity=(1 - alpha) * sub_inicial.get_fill_opacity())
        sub.set_stroke(
            opacity=(1 - alpha) * sub_inicial.get_stroke_opacity())


class EscenaBajar(Scene):
    def construct(self):
        adios = Text("Hasta la próxima", font_size=64)
        queda = Text("(esta línea se queda)", font_size=32)
        VGroup(adios, queda).arrange(DOWN, buff=0.8)
        self.add(adios, queda)
        self.play(BajarYDesaparecer(adios), run_time=1.5)
        # remover=True: al terminar, adios ya no está en la escena
        assert adios not in self.mobjects
        self.wait()
