from manim import *


class PlanoSimulado(VGroup):
    """Imita un plano de cámara: docente ante la pizarra.

    Solo sirve para revisar rótulos y transiciones; en el montaje
    real, debajo del clip transparente va la grabación.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        fondo = FullScreenRectangle(fill_color="#56636B",
                                    fill_opacity=1, stroke_width=0)
        pizarra = Rectangle(width=7.4, height=4.2,
                            fill_color="#2F4A40", fill_opacity=1,
                            stroke_color="#7A6448", stroke_width=10)
        pizarra.move_to([2.4, 1.0, 0])
        tiza = MathTex(r"\int_0^1 x^2\,dx=\frac{1}{3}",
                       font_size=60, color="#D9D4C7")
        tiza.move_to(pizarra)
        cabeza = Circle(radius=0.8, fill_color="#8C7468",
                        fill_opacity=1, stroke_width=0)
        cabeza.move_to([-3.8, 0.9, 0])
        cuerpo = Ellipse(width=3.8, height=4.4,
                         fill_color="#A7B1B8", fill_opacity=1,
                         stroke_width=0)
        cuerpo.move_to([-3.8, -2.9, 0])
        aviso = Text("grabación simulada", font_size=32,
                     color="#C9D1D6").to_corner(UR, buff=0.5)
        self.add(fondo, pizarra, tiza, cuerpo, cabeza, aviso)
