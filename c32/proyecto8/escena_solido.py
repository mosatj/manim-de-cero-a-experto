from manim import *
from funcion import volumen_discos
from piezas import ejes3d, perfil3d, superficie, discos_3d
from piezas import rotulo_discos, rotulo_exacto


class SolidoDeRevolucion(ThreeDScene):
    """El mismo argumento, ahora en el espacio: el perfil gira,
    nace la superficie y los discos la rellenan."""

    def fijar(self, *rotulos):
        # Rótulos fijos en pantalla, que no giran con la cámara;
        # se retiran para que aparezcan cuando toque
        self.add_fixed_in_frame_mobjects(*rotulos)
        self.remove(*rotulos)

    def construct(self):
        ejes = ejes3d()
        # Se mira casi de frente al plano del perfil (y = 0)
        self.set_camera_orientation(
            phi=72 * DEGREES, theta=-100 * DEGREES, zoom=1.05
        )
        exacto = rotulo_exacto().to_corner(UL, buff=0.35)
        rotulo = rotulo_discos(6, volumen_discos(6))
        rotulo.next_to(exacto, DOWN, buff=0.2)
        rotulo.align_to(exacto, LEFT)
        nuevo = rotulo_discos(12, volumen_discos(12))
        nuevo.move_to(rotulo).align_to(rotulo, LEFT)
        self.fijar(exacto, rotulo, nuevo)

        self.play(Create(ejes))
        self.play(Create(perfil3d(ejes)))

        # Bloque 1: el perfil gira y deja la superficie
        solido = superficie(ejes)
        self.begin_ambient_camera_rotation(rate=0.05)
        self.play(Create(solido), run_time=2.5)
        self.play(Write(exacto))

        # Bloque 2: seis discos dentro del sólido translúcido
        discos = discos_3d(ejes, 6)
        self.play(
            solido.animate.set_opacity(0.15),
            FadeIn(discos),
            Write(rotulo),
        )
        self.wait(0.5)

        # Bloque 3: doce discos: la suma se acerca al exacto
        finos = discos_3d(ejes, 12)
        self.play(
            FadeOut(discos), FadeIn(finos),
            FadeOut(rotulo), FadeIn(nuevo),
            run_time=1.5,
        )
        self.stop_ambient_camera_rotation()
        self.wait()
