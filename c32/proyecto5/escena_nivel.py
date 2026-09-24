from manim import *
from funcion import NIVELES
from piezas3d import ejes3d, superficie, curva_nivel


class CurvasDeNivel(ThreeDScene):
    def construct(self):
        ejes = ejes3d()
        self.set_camera_orientation(
            phi=65 * DEGREES,
            theta=-55 * DEGREES,
            zoom=1.1,
            frame_center=ejes.c2p(0, 0, 2.2),
        )
        titulo = MathTex(
            r"z = 4 - \tfrac{x^2}{2} - y^2", font_size=40
        )
        self.add_fixed_in_frame_mobjects(titulo)
        self.remove(titulo)  # aparecerá con Write
        titulo.to_corner(UL)
        manto = superficie(ejes)
        self.play(Create(ejes), Write(titulo))
        self.play(Create(manto), run_time=2)

        # Cortes horizontales z = c sobre la superficie...
        en_superficie = VGroup(
            *[curva_nivel(ejes, c) for c in NIVELES]
        )
        self.play(
            LaggedStart(
                *[Create(c) for c in en_superficie], lag_ratio=0.3
            )
        )
        # ...y su sombra en z = 0: el mapa de curvas de nivel
        sombras = VGroup(
            *[curva_nivel(ejes, c, altura=0) for c in NIVELES]
        )
        self.play(
            *[
                TransformFromCopy(c, s)
                for c, s in zip(en_superficie, sombras)
            ],
            run_time=2,
        )
        # Vista cenital: el mapa topográfico. Se retiran las curvas
        # altas: la perspectiva las vería mayores que sus sombras
        self.move_camera(
            phi=0,
            theta=-90 * DEGREES,
            zoom=1.3,
            frame_center=ORIGIN,
            run_time=2,
            added_anims=[
                FadeOut(en_superficie),
                manto.animate.set_opacity(0.12),
            ],
        )
