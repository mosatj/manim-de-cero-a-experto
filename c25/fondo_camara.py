from manim import *


class FondoCamara(Scene):
    def construct(self):
        # La cámara es un atributo de la escena
        self.camera.background_color = "#0B2A3C"
        ancho = config.frame_width           # 14,22 unidades
        alto = config.frame_height           # 8 unidades
        medida = MathTex(rf"{ancho:.2f} \times {alto:.0f}",
                         font_size=72)
        self.add(medida)
        for esquina in [UL, UR, DL, DR]:
            p = esquina * np.array([ancho / 2, alto / 2, 0])
            punto = Dot(p, color=YELLOW)
            texto = MathTex(rf"({p[0]:.2f},\ {p[1]:.0f})",
                            font_size=36)
            texto.next_to(punto, -esquina)  # hacia dentro
            self.add(punto, texto)
