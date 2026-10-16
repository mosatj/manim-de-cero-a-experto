from manim import *

# El logo de Manim Community lo dibuja la propia biblioteca: ManimBanner
# combina la «M» de doble trazo con un círculo, un cuadrado y un
# triángulo. Se usa el tema claro para imprimir sus colores reales.
config.frame_height = 4.6
config.pixel_height = round(config.pixel_width * 4.6 / config.frame_width)


class LogoComunidad(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"  # el marfil del logo
        logo = ManimBanner(dark_theme=False).scale(0.9)
        self.play(logo.create())   # las tres figuras y la «M»
        self.play(logo.expand())   # se despliega el resto del nombre
        self.wait()
