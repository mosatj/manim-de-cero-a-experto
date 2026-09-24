from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class SvgImagen(Scene):
    def construct(self):
        # Un SVG se convierte en VMobjects: se puede recolorear
        hoja = SVGMobject("recursos/hoja.svg", height=3)
        otra = hoja.copy().set_fill(GOLD).rotate(-30 * DEGREES)
        svgs = VGroup(hoja, otra).arrange(RIGHT, buff=0.6)
        # Una imagen de mapa de bits creada con NumPy (sin archivo)
        x = np.linspace(0, 1, 200)
        tono = np.uint8(255 * np.outer(x, x[::-1]))
        pixeles = np.dstack([tono, 255 - tono,
                             np.full_like(tono, 200)])
        imagen = ImageMobject(pixeles).set(height=3)
        todo = Group(svgs, imagen).arrange(RIGHT, buff=1)
        self.add(todo)
        self.add(Text("SVGMobject", font_size=28)
                 .next_to(svgs, DOWN),
                 Text("ImageMobject", font_size=28)
                 .next_to(imagen, DOWN))
