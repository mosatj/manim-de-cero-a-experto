from manim import *
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# matplotlib calcula las curvas de nivel; Manim las anima
X, Y = np.meshgrid(np.linspace(-3, 3, 120), np.linspace(-3, 3, 120))
Z = np.sin(X) * np.cos(Y) + 0.3 * X
NIVELES = [-1.2, -0.8, -0.4, 0, 0.4, 0.8, 1.2]


def curvas_de_nivel():
    """Lista de (nivel, polilínea n x 2) sacada de plt.contour."""
    cs = plt.contour(X, Y, Z, levels=NIVELES)
    curvas = []
    for nivel, camino in zip(cs.levels, cs.get_paths()):
        for poligono in camino.to_polygons(closed_only=False):
            if len(poligono) > 2:
                curvas.append((nivel, poligono))
    return curvas


class ContornosMatplotlib(Scene):
    def construct(self):
        ejes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1],
                    x_length=7, y_length=7, tips=False)
        self.add(ejes)
        trazos = VGroup()
        for nivel, puntos in curvas_de_nivel():
            vertices = [ejes.c2p(a, b) for a, b in puntos]
            curva = VMobject().set_points_smoothly(vertices)
            curva.set_stroke(
                interpolate_color(BLUE_D, RED, (nivel + 1.2) / 2.4),
                width=3)
            trazos.add(curva)
        rotulo = MathTex(r"z=\sin x\cos y+0{,}3x", font_size=36)
        rotulo.to_corner(UR)
        self.play(Write(rotulo))
        self.play(Create(trazos, lag_ratio=0.05), run_time=4)
        self.wait()
