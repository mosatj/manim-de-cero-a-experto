from manim import *


class PlanosEncuadre(Scene):
    def construct(self):
        # La «escena completa»: unos ejes, una curva y un punto que importa
        ejes = Axes(x_range=[-4, 4, 1], y_range=[-1.5, 2.5, 1],
                    x_length=10, y_length=5, tips=False)
        curva = ejes.plot(lambda x: 0.12 * x**3 - 0.6 * x + 0.5,
                          x_range=[-3, 3.1], color=BLUE, stroke_width=5)
        punto = Dot(ejes.c2p(1.29, 0.12 * 1.29**3 - 0.6 * 1.29 + 0.5),
                    color=RED, radius=0.11)
        formula = MathTex(r"f(x)=0{,}12x^3-0{,}6x+0{,}5",
                          font_size=34).move_to([-4.0, 2.55, 0])
        self.add(ejes, curva, punto, formula)

        # Cuatro encuadres, del más abierto al más cerrado: cada uno es
        # el marco que vería la cámara (en Manim, el ancho del marco)
        anchos = [12.6, 8.0, 4.2, 1.9]
        nombres = ["plano general", "plano medio", "primer plano",
                   "detalle"]
        centros = [DOWN * 0.15, punto.get_center() + LEFT * 1.2,
                   punto.get_center() + LEFT * 0.3, punto.get_center()]
        tonos = [GREY_B, TEAL_C, GREEN_C, RED_C]
        for ancho, nombre, centro, tono in zip(anchos, nombres, centros,
                                                tonos):
            marco = Rectangle(width=ancho, height=ancho * 9 / 16,
                              color=tono, stroke_width=4).move_to(centro)
            rotulo = Text(nombre, font_size=24, color=tono)
            rotulo.next_to(marco, UP, buff=0.08).align_to(marco, LEFT)
            self.add(marco, rotulo)
