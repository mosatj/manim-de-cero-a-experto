from manim import *


class CaminosDeTransformacion(Scene):
    def construct(self):
        columnas = zip([-4.5, 0, 4.5], [0, PI / 2, PI],
                       ["0", r"\pi/2", r"\pi"])
        for x, arco, nombre in columnas:
            a = Dot([x, -1.3, 0], radius=0.14, color=YELLOW)
            b = Dot([x, 1.3, 0], radius=0.14, color=RED)
            # path_func: (inicio, fin, alpha) -> puntos intermedios
            camino = path_along_arc(arco)
            for p, q, color in [(a, b, YELLOW), (b, a, RED)]:
                inicio = np.array([p.get_center()])
                fin = np.array([q.get_center()])
                recorrido = VMobject().set_stroke(color, 2)
                alphas = np.linspace(0, 1, 30)
                recorrido.set_points_smoothly(
                    [camino(inicio, fin, s)[0] for s in alphas])
                self.add(DashedVMobject(recorrido, num_dashes=20))
            rotulo = MathTex(r"\text{path\_arc} = " + nombre)
            self.add(rotulo.scale(0.75).move_to([x, -3, 0]), a, b)
            # Intercambio: cada punto va al lugar del otro
            self.play(a.animate(path_arc=arco).move_to(b),
                      b.animate(path_arc=arco).move_to(a))
