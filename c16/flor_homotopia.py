from manim import *


class FlorHomotopia(Scene):
    def construct(self):
        circulo = Circle(radius=2, color=BLUE, fill_opacity=0.3)
        circulo.insert_n_curves(60)   # más puntos: más suavidad

        # h(x, y, z, t): adónde ha ido (x, y, z) en el instante t
        def florecer(x, y, z, t):
            r, ang = np.hypot(x, y), np.arctan2(y, x)
            r = r * (1 + 0.25 * t * np.sin(6 * ang + PI * t))
            ang = ang + t * PI / 6
            return (r * np.cos(ang), r * np.sin(ang), z)

        self.add(Circle(radius=2).set_stroke(GREY, 1))
        self.play(Homotopy(florecer, circulo, run_time=3))
