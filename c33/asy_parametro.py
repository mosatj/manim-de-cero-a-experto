from manim import *
from asy_fotogramas import fotogramas_asy
from asy_utiles import Registro, glifos, por_color


def ortocentro(t):
    """H del triángulo de asy_euler_movil.asy, con Python."""
    ang = np.radians(50 + 80 * t)
    cx, cy = 3 + 3.5 * np.cos(ang), 3.5 * np.sin(ang)
    return cx, (6 - cx) * cx / cy


class ParametroAsy(Scene):
    """Nueve fotogramas clave de Asymptote; Manim interpola."""

    def construct(self):
        valores = np.linspace(0, 1, 9)
        claves = fotogramas_asy("asy_euler_movil.asy", valores,
                                height=7.4)
        # Las marcas están en el mismo sitio en todos
        a_escena = Registro(claves[0], (-1.2, -2.8), (7.2, 4.8))
        for clave in claves:
            clave.to_edge(LEFT, buff=0.5)
            por_color(clave, "#FF00FF").set_opacity(0)  # caja fija
            glifos(clave).set_fill("#E9F2F7")
        figura = claves[0].copy()
        # [6] es el ortocentro H: Manim dibuja su recorrido
        rastro = TracedPath(figura[6].get_center, stroke_width=5,
                            stroke_color="#7FB89A")
        verdad = VMobject(stroke_width=3, color="#E9F2F7")
        verdad.set_points_smoothly([a_escena(*ortocentro(t))
                                    for t in np.linspace(0, 1, 60)])
        textos = VGroup(
            Text("9 fotogramas de Asymptote", font_size=32),
            Text("Entre ellos, Manim interpola", font_size=32),
            Text("en línea recta:", font_size=32),
            Text("el rastro de H es un polígono", font_size=32,
                 color="#7FB89A"),
            Text("la curva real (punteada)", font_size=32),
            Text("casi coincide", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        textos.to_edge(RIGHT, buff=0.3).shift(UP * 1.2)
        self.add(figura, rastro)
        self.play(FadeIn(textos[:3]))
        for clave in claves[1:]:
            self.play(Transform(figura, clave), rate_func=linear,
                      run_time=0.6)
        self.play(Create(DashedVMobject(verdad, num_dashes=40)),
                  FadeIn(textos[3:]))
        self.wait()
