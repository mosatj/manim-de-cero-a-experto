from manim import *


class AnotarTriangulo(Scene):
    def construct(self):
        A, B, C = [-3, -2, 0], [3, -2, 0], [3, 1.5, 0]
        tri = Polygon(A, B, C, color=BLUE, fill_opacity=0.2)
        base, altura, hipo = Line(A, B), Line(B, C), Line(A, C)
        # Ángulo recto en B y ángulo agudo en A
        recto = RightAngle(Line(B, A), altura, length=0.4)
        alfa = Angle(base, hipo, radius=1.1, color=YELLOW)
        guia = Angle(base, hipo, radius=1.5)  # solo para ubicar
        t_alfa = MathTex(r"\alpha", color=YELLOW)
        t_alfa.move_to(guia.point_from_proportion(0.5))
        # Llaves con rótulo en los catetos
        llave_b = Brace(base, DOWN)
        llave_a = Brace(altura, RIGHT)
        t_b = llave_b.get_tex("b")
        t_a = llave_a.get_tex("a")
        # En la hipotenusa: dirección perpendicular hacia fuera
        normal = rotate_vector(hipo.get_unit_vector(), PI / 2)
        llave_c = Brace(hipo, direction=normal, color=GREEN)
        t_c = llave_c.get_tex("c").set_color(GREEN)
        self.add(tri, recto, alfa, t_alfa, llave_a, llave_b,
                 llave_c, t_a, t_b, t_c)
        self.add(MathTex(r"a^2+b^2=c^2", font_size=56)
                 .to_corner(UL))
