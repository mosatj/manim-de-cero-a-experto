from manim import *


class Rombo(VMobject):
    """Un VMobject propio: solo redefine generate_points."""

    def generate_points(self):
        print("  Rombo.generate_points()")
        self.set_points_as_corners(
            [UP, RIGHT, DOWN, LEFT, UP])

    def init_colors(self):
        print("  Rombo.init_colors()")
        super().init_colors()


print("Creando Rombo(color=RED)...")
rombo = Rombo(color=RED)
print("Puntos:", len(rombo.points), "| color:", rombo.color)
