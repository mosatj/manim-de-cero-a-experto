from manim import *
from componentes import EjeEtiquetado


class EjeEscena(Scene):
    def construct(self):
        eje = EjeEtiquetado(-4, 4, nombre="x").scale(1.5)
        eje.marcar(-np.sqrt(2), r"-\sqrt{2}", BLUE)
        eje.marcar(np.pi / 2, r"\tfrac{\pi}{2}", GREEN)
        eje.marcar(np.e, "e")                  # color por defecto
        self.play(Create(eje.recta), Write(eje.nombre))
        marcas = [FadeIn(m, shift=DOWN) for m in eje.marcas]
        self.play(LaggedStart(*marcas, lag_ratio=0.4))
        self.wait()
