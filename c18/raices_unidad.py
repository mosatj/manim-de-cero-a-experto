from manim import *


class RaicesUnidad(Scene):
    def construct(self):
        plano = ComplexPlane(x_range=[-2, 2, 1], y_range=[-2, 2, 1],
                             x_length=6.5, y_length=6.5)
        plano.add_coordinates(-2, -1, 1, 2)      # eje real
        # Eje imaginario con rótulos a medida: i en lugar de 1i
        imaginarios = [(2, "2i"), (1, "i"), (-1, "-i"), (-2, "-2i")]
        for k, texto in imaginarios:
            rotulo_k = MathTex(texto, font_size=24)
            lado = UR if k > 0 else DR
            rotulo_k.next_to(plano.n2p(k * 1j), lado, buff=0.08)
            plano.add(rotulo_k)
        n = 6
        raices = [np.exp(2j * PI * k / n) for k in range(n)]
        # n2p (number_to_point) acepta números complejos
        puntos = VGroup(*[Dot(plano.n2p(z), color=YELLOW)
                          for z in raices])
        poligono = Polygon(*[plano.n2p(z) for z in raices],
                           color=YELLOW, stroke_width=2)
        circulo = Circle(radius=plano.get_x_unit_size(), color=BLUE)
        circulo.move_to(plano.n2p(0))
        rotulo = MathTex(r"z^6=1", font_size=44).to_corner(UL)
        self.add(plano, circulo, rotulo)
        self.play(LaggedStart(*[GrowFromCenter(p) for p in puntos],
                              lag_ratio=0.2))
        self.play(Create(poligono))
        self.wait()
