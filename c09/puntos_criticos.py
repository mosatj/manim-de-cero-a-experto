from manim import *

Text.set_default(font="monospace")  # rótulos tipo código


class PuntosCriticos(Scene):
    def construct(self):
        forma = Star(7, outer_radius=2.2, color=BLUE,
                     fill_opacity=0.35)
        forma.rotate(10 * DEGREES).shift(0.3 * DOWN)
        # La caja envolvente: el menor rectángulo que la contiene
        caja = SurroundingRectangle(forma, buff=0, color=GRAY)
        self.add(forma, DashedVMobject(caja, num_dashes=60))
        nombres = {
            "get_top()": UP, "get_bottom()": DOWN,
            "get_left()": LEFT, "get_right()": RIGHT,
            "get_center()": ORIGIN,
            "get_corner(UL)": UL, "get_corner(UR)": UR,
            "get_corner(DL)": DL, "get_corner(DR)": DR,
        }
        for nombre, d in nombres.items():
            p = forma.get_critical_point(d)
            # Esquinas en rojo; el resto, en amarillo
            color = YELLOW if np.linalg.norm(d) <= 1 else RED
            self.add(Dot(p, color=color, radius=0.09))
            t = Text(nombre, font_size=26, color=color)
            t.next_to(p, d if np.any(d) else DOWN, buff=0.12)
            self.add(t)
