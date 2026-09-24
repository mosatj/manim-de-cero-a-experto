from manim import *


class RaicesUnidad(Scene):
    def construct(self):
        n = 7
        raices = np.exp(2j * np.pi * np.arange(n) / n)   # complejos
        radio = 2.8
        # Cada complejo z = x + iy es el punto (x, y, 0) del plano
        puntos = [radio * np.array([z.real, z.imag, 0])
                  for z in raices]
        circulo = Circle(radius=radio, color=GREY_B, stroke_width=2)
        poligono = Polygon(*puntos, color=YELLOW, fill_opacity=0.15)
        radios = VGroup(*[Line(ORIGIN, p, color=BLUE)
                          for p in puntos])
        puntos_m = VGroup(*[Dot(p, color=YELLOW) for p in puntos])
        rotulo = MathTex(r"z^7 = 1").to_corner(UL)
        self.add(circulo)
        self.play(Create(radios), FadeIn(puntos_m))
        self.play(Create(poligono), Write(rotulo))
