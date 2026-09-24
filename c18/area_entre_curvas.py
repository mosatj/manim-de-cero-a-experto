from manim import *


class AreaEntreCurvas(Scene):
    def construct(self):
        ejes = Axes(x_range=[0, 4.5, 1], y_range=[0, 4.5, 1],
                    x_length=6, y_length=6, tips=False,
                    axis_config={"include_numbers": True,
                                 "font_size": 24})
        raiz = ejes.plot(lambda x: 2 * np.sqrt(x), x_range=[0, 4.5],
                         color=BLUE)
        recta = ejes.plot(lambda x: x, x_range=[0, 4.5], color=RED)
        # Región entre las curvas: bounded_graph es la de abajo
        region = ejes.get_area(raiz, x_range=(0, 4),
                               bounded_graph=recta, color=BLUE,
                               opacity=0.35)
        # Rectángulos de Riemann bajo la raíz, en el punto medio
        rects = ejes.get_riemann_rectangles(
            raiz, x_range=[0, 4], dx=0.5,
            input_sample_type="center", color=[BLUE_E, BLUE_B],
            fill_opacity=0.6, stroke_width=1)
        grupo_izq = VGroup(ejes, raiz, recta, region)
        grupo_der = VGroup(ejes.copy(), raiz.copy(), rects)
        grupo_der.next_to(grupo_izq, RIGHT, buff=1)
        todo = VGroup(grupo_izq, grupo_der)
        todo.center().to_edge(DOWN, buff=0.4)
        area = MathTex(r"\int_0^4 \left(2\sqrt{x}-x\right)dx"
                       r"=\tfrac{8}{3}", font_size=34)
        area.next_to(grupo_izq, UP, buff=0.3)
        suma = MathTex(r"\sum f(x_k^{*})\,\Delta x,\ \Delta x=0.5",
                       font_size=34)
        suma.next_to(grupo_der, UP, buff=0.3)
        self.add(grupo_izq[:3], grupo_der[:2])
        self.play(FadeIn(region), Create(rects, lag_ratio=0.2))
        self.play(Write(area), Write(suma))
        self.wait()
