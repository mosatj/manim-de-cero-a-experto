from manim import *


class SolidosColores(ThreeDScene):
    def construct(self):
        esfera = Sphere(radius=1).set_color(BLUE).shift(4 * LEFT)
        cubo = Cube(side_length=1.8, fill_color=RED)
        prisma = Prism(dimensions=[1, 2, 3], fill_color=GREEN)
        prisma.shift(4 * RIGHT)
        self.set_camera_orientation(phi=60 * DEGREES,
                                    theta=-60 * DEGREES)
        self.add(esfera, cubo, prisma)
