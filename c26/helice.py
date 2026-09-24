from manim import *


class Helice(ThreeDScene):
    def construct(self):
        ejes = ThreeDAxes(x_range=[-2, 2], y_range=[-2, 2],
                          z_range=[0, 4], x_length=4, y_length=4,
                          z_length=4).shift(2 * IN)

        def r(t):                   # r(t) = (cos t, sen t, t/π)
            return ejes.c2p(np.cos(t), np.sin(t), t / PI)

        curva = ParametricFunction(r, t_range=[0, 4 * PI],
                                   color=YELLOW)
        cilindro = Cylinder(radius=1, height=4, fill_opacity=0.15,
                            show_ends=False, stroke_width=0.2)
        cilindro.move_to(ejes.c2p(0, 0, 2))
        t0 = 3.75 * PI                  # punto de cara a la cámara
        # Vector tangente r'(t0) = (-sen t0, cos t0, 1/π)
        velocidad = np.array([-np.sin(t0), np.cos(t0), 1 / PI])
        tangente = Arrow3D(r(t0), r(t0) + 1.5 * velocidad,
                           color=RED, thickness=0.03)
        punto = Dot3D(r(t0), color=RED)
        self.set_camera_orientation(phi=70 * DEGREES,
                                    theta=-40 * DEGREES, zoom=1.4)
        self.add(ejes, cilindro, curva, punto, tangente)
