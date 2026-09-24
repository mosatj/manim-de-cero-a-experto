from manim import *


class GaleriaSolidos(ThreeDScene):
    def construct(self):
        solidos = [
            ("Sphere", Sphere(radius=0.7)),
            ("Cube", Cube(side_length=1.2)),
            ("Prism", Prism(dimensions=[0.7, 1.1, 1.5])),
            ("Cone", Cone(base_radius=0.6, height=1.3)),
            ("Cylinder", Cylinder(radius=0.5, height=1.3)),
            ("Torus", Torus(major_radius=0.6, minor_radius=0.2)),
            ("Tetrahedron", Tetrahedron(edge_length=1.5)),
            ("Line3D", Line3D([-0.7, 0, -0.5], [0.7, 0, 0.5],
                              thickness=0.05)),
            ("Arrow3D", Arrow3D([-0.7, 0, -0.5], [0.7, 0, 0.5])),
        ]
        colores = [BLUE, RED, GREEN, GOLD, TEAL, PURPLE, ORANGE,
                   WHITE, YELLOW]
        self.set_camera_orientation(phi=70 * DEGREES,
                                    theta=-80 * DEGREES, zoom=0.9)
        for k, ((nombre, solido), color) in enumerate(
                zip(solidos, colores)):
            fila, columna = divmod(k, 3)
            # Filas apiladas en z: no se tapan unas a otras
            centro = np.array([4 * (columna - 1), 0, 3 - 3 * fila])
            solido.set_color(color).move_to(centro)
            rotulo = Text(nombre, font_size=24)
            rotulo.move_to(centro + 1.2 * IN)     # debajo, en z
            # El rótulo sigue al sólido y siempre mira a la cámara
            self.add_fixed_orientation_mobjects(rotulo)
            self.add(solido)
