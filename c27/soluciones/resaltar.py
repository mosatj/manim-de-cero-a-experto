from manim import *


def enfocar(foco, contexto, atenuacion=0.7):
    """Animaciones que destacan `foco` y atenúan el `contexto`."""
    resto = VGroup(*[m for m in contexto if m is not foco])
    for m in contexto:
        m.save_state()  # para poder volver después con Restore
    return [resto.animate.fade(atenuacion),
            Indicate(foco, color=YELLOW)]


def restaurar(contexto):
    return [Restore(m) for m in contexto]


class Resaltar(Scene):
    def construct(self):
        pasos = VGroup(*[MathTex(t, font_size=56) for t in
                         (r"3x-5=10", r"3x=15", r"x=5")]).arrange(DOWN)
        self.play(Write(pasos))
        self.play(*enfocar(pasos[1], pasos))
        self.play(*restaurar(pasos))
        self.play(*enfocar(pasos[2], pasos, atenuacion=0.5))
