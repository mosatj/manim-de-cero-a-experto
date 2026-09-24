from manim import *


def sierpinski(a, b, c, nivel):
    """Lista de triángulos rellenos del nivel pedido."""
    if nivel == 0:
        return [Polygon(a, b, c, stroke_width=0, fill_opacity=1)]
    ab, bc, ca = (a + b) / 2, (b + c) / 2, (c + a) / 2
    return (sierpinski(a, ab, ca, nivel - 1)
            + sierpinski(ab, b, bc, nivel - 1)
            + sierpinski(ca, bc, c, nivel - 1))


class SierpinskiZoom(MovingCameraScene):
    def construct(self):
        marco = self.camera.frame
        A = np.array([-4, -3.4, 0])  # vértice inferior izquierdo
        B, C = A + 8 * RIGHT, A + 4 * RIGHT + 4 * np.sqrt(3) * UP
        figura = VGroup(*sierpinski(A, B, C, 6))
        figura.set_color_by_gradient(BLUE, TEAL, YELLOW)
        self.add(figura)
        self.wait()
        # La esquina inferior izquierda es la figura a escala 1/2
        for _ in range(2):
            centro = A + (marco.get_center() - A) / 2
            self.play(marco.animate.scale(1 / 2).move_to(centro),
                      run_time=2)
