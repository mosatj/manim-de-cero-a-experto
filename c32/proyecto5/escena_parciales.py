from manim import *
from funcion import f, fx, fy, PUNTO
from piezas3d import (
    ejes3d,
    superficie,
    corte,
    tangente,
    plano_corte,
    COLOR_X,
    COLOR_Y,
)


class DerivadasParciales(ThreeDScene):
    def construct(self):
        a, b = PUNTO
        ejes = ejes3d()
        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-60 * DEGREES,
            zoom=1.1,
            frame_center=ejes.c2p(0, 0, 2.2),
        )
        manto = superficie(ejes, opacidad=0.4)
        punto = Dot3D(
            ejes.c2p(a, b, f(a, b)), radius=0.08, color=WHITE
        )
        self.add(ejes, manto)
        self.play(FadeIn(punto, scale=3))

        for direccion, color, valor, fila in (
            ("x", COLOR_X, fx(a, b), 0),
            ("y", COLOR_Y, fy(a, b), 1),
        ):
            plano = plano_corte(ejes, a, b, direccion, color)
            curva = corte(ejes, a, b, direccion, color)
            recta = tangente(ejes, a, b, direccion, color)
            rotulo = MathTex(
                rf"\frac{{\partial f}}{{\partial {direccion}}}"
                rf"(1,\ 0.8) = {valor:.1f}",
                color=color,
                font_size=40,
            )
            # Fijo a la pantalla, pero aún no visible
            self.add_fixed_in_frame_mobjects(rotulo)
            self.remove(rotulo)
            rotulo.to_corner(UL).shift(DOWN * 1.3 * fila)
            self.play(FadeIn(plano))
            self.play(Create(curva), run_time=1.5)
            self.play(Create(recta), Write(rotulo))
            self.play(FadeOut(plano))
