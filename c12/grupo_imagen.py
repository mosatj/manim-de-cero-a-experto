from manim import *


class GrupoImagen(Scene):
    def construct(self):
        # Imagen de 64 × 64 píxeles creada con NumPy
        x = np.linspace(0, 255, 64, dtype=np.uint8)
        pixeles = np.stack([np.tile(x, (64, 1)),
                            np.tile(x[:, None], (1, 64)),
                            np.full((64, 64), 200, np.uint8)], 2)
        imagen = ImageMobject(pixeles).scale_to_fit_height(3)
        pie = Text("ImageMobject no es un VMobject", font_size=30)
        # VGroup(imagen, pie) lanzaría TypeError: se usa Group
        ficha = Group(imagen, pie).arrange(DOWN, buff=0.4)
        marco = SurroundingRectangle(ficha, color=BLUE, buff=0.3)
        self.add(ficha, marco)
