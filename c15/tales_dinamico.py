from manim import *


class TalesDinamico(Scene):
    def construct(self):
        R = 2.6
        circulo = Circle(radius=R, color=GREY_B).shift(LEFT * 1.5)
        A = circulo.point_at_angle(PI)
        B = circulo.point_at_angle(0)
        ang = ValueTracker(115)  # ángulo de C, en grados

        def punto_c():
            return circulo.point_at_angle(ang.get_value() * DEGREES)

        tri = always_redraw(lambda: Polygon(
            A, B, punto_c(), color=BLUE, fill_opacity=0.15))
        angulo = always_redraw(lambda: Angle(
            Line(punto_c(), A), Line(punto_c(), B), radius=0.45,
            elbow=True, color=YELLOW))
        C = always_redraw(lambda: Dot(punto_c(), color=YELLOW))

        def medida():  # el ángulo ACB medido con vectores
            u, v = A - punto_c(), B - punto_c()
            cos = u @ v / (np.linalg.norm(u) * np.linalg.norm(v))
            return np.degrees(np.arccos(np.clip(cos, -1, 1)))

        valor = DecimalNumber(medida(), num_decimal_places=2,
                              unit=r"^\circ", color=YELLOW)
        valor.add_updater(lambda m: m.set_value(medida()))
        rotulo = VGroup(MathTex(r"\angle ACB ="), valor).arrange()
        rotulo.to_corner(UR)
        nombres = VGroup(MathTex("A").next_to(A, LEFT),
                         MathTex("B").next_to(B, RIGHT))
        c_nombre = always_redraw(lambda: MathTex("C").next_to(
            punto_c(), normalize(punto_c() - circulo.get_center())))

        self.add(circulo, tri, angulo, C, nombres, c_nombre, rotulo)
        self.play(ang.animate.set_value(35), run_time=2)
        self.play(ang.animate.set_value(160), run_time=2)
        self.play(ang.animate.set_value(70), run_time=2)
