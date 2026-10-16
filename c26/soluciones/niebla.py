from manim import *


def f(x, y):
    return np.sin(x) * np.cos(y)


class Niebla(ThreeDScene):
    def construct(self):
        superficie = Surface(
            lambda u, v: np.array([u, v, f(u, v)]),
            u_range=[-4, 4], v_range=[-4, 4], resolution=24,
            checkerboard_colors=False, stroke_width=0)
        cerca, niebla = ManimColor(TEAL_A), ManimColor(BLACK)

        def nublar(sup):
            # Dirección hacia la cámara a partir de phi y theta
            phi = self.camera.get_phi()
            theta = self.camera.get_theta()
            hacia = np.array([np.sin(phi) * np.cos(theta),
                              np.sin(phi) * np.sin(theta),
                              np.cos(phi)])
            prof = np.array([np.dot(c.get_center(), hacia)
                             for c in sup])
            t = (prof - prof.min()) / (prof.max() - prof.min())
            for cara, ti in zip(sup, t):
                # Lo lejano (t = 0) se funde con el fondo
                color = interpolate_color(niebla, cerca,
                                          0.15 + 0.85 * ti)
                cara.set_fill(color, opacity=1)

        self.set_camera_orientation(phi=65 * DEGREES,
                                    theta=-60 * DEGREES)
        superficie.add_updater(nublar)
        self.add(superficie)
        self.move_camera(theta=-20 * DEGREES, run_time=3)
