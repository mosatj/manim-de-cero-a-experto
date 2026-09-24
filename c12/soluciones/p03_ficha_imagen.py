from manim import *


class FichaImagen(Scene):
    def construct(self):
        y, x = np.mgrid[0:100, 0:100]
        tablero = ((x // 20 + y // 20) % 2 * 255).astype(np.uint8)
        imagen = ImageMobject(tablero).scale_to_fit_height(3)
        pie = Text("Un tablero de 5 × 5 casillas", font_size=32)
        ficha = Group(imagen, pie).arrange(DOWN, buff=0.4)
        self.play(FadeIn(ficha, shift=UP))
        self.play(ficha.animate.scale(0.7).to_corner(UL))
        self.wait()
