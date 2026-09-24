from manim import *


class MarcoDeReferencia(Scene):
    def construct(self):
        # El marco visible mide frame_width x frame_height
        ancho, alto = config.frame_width, config.frame_height
        plano = NumberPlane(
            background_line_style={"stroke_opacity": 0.35})
        borde = Rectangle(width=ancho, height=alto, color=YELLOW,
                          stroke_width=8)
        self.add(plano, borde)
        # Las cuatro esquinas, con sus coordenadas redondeadas
        for esquina in [UL, UR, DL, DR]:
            punto = esquina * np.array([ancho / 2, alto / 2, 0])
            rotulo = MathTex(rf"({punto[0]:.2f},\ {punto[1]:.0f})",
                             font_size=34)
            rotulo.next_to(punto, -esquina, buff=0.15)
            self.add(Dot(punto, color=YELLOW), rotulo)
        lineas = [f"frame_width = {ancho:.4f}",
                  f"frame_height = {alto:.1f}",
                  f"pixel_width = {config.pixel_width}",
                  f"pixel_height = {config.pixel_height}",
                  f"frame_rate = {config.frame_rate:g}"]
        datos = VGroup(*[Text(t, font="Menlo", font_size=26)
                         for t in lineas])
        datos.arrange(DOWN, aligned_edge=LEFT)
        datos.add_background_rectangle(opacity=0.85, buff=0.2)
        self.add(datos)
