from manim import *


def estrella(n_muestras=512):
    """Estrella de 5 puntas muestreada a paso constante."""
    ang = np.arange(11) * PI / 5 + PI / 2
    radios = np.where(np.arange(11) % 2 == 0, 3.0, 1.25)
    vertices = radios * np.exp(1j * ang)       # polígono cerrado
    lados = np.abs(np.diff(vertices))
    s = np.concatenate([[0], np.cumsum(lados)])  # long. de arco
    u = np.linspace(0, s[-1], n_muestras, endpoint=False)
    return (np.interp(u, s, vertices.real)
            + 1j * np.interp(u, s, vertices.imag))


class Epiciclos(Scene):
    M = 15                          # número de epiciclos

    def construct(self):
        z = estrella()
        N = len(z)
        c = np.fft.fft(z) / N                   # coeficientes c_k
        k = np.fft.fftfreq(N, d=1 / N)       # frecuencias enteras
        orden = np.argsort(-np.abs(c))[:self.M]   # los mayores
        c, k = c[orden], k[orden]

        def cadena(t):
            """Centros sucesivos de la cadena de vectores en t."""
            giros = c * np.exp(1j * k * t)     # c_k e^{ikt}
            s = np.concatenate([[0], np.cumsum(giros)])
            return [np.array([w.real, w.imag, 0]) for w in s]

        t = ValueTracker(0.001)

        def dibujar_cadena():
            p = cadena(t.get_value())
            grupo = VGroup()
            for a, b in zip(p[:-1], p[1:]):
                r = np.linalg.norm(b - a)
                grupo.add(Circle(r, stroke_width=1, color=BLUE,
                                 stroke_opacity=0.5).move_to(a),
                          Line(a, b, stroke_width=2, color=WHITE))
            return grupo

        punta = lambda s: cadena(s)[-1]
        traza = always_redraw(lambda: ParametricFunction(
            punta, t_range=[0, t.get_value(), 0.01], color=YELLOW,
            stroke_width=4))
        modelo = Polygon(*[[w.real, w.imag, 0] for w in z[::8]],
                         stroke_opacity=0.25, color=GRAY)
        self.add(modelo, traza, always_redraw(dibujar_cadena))
        for fin in (2 * PI / 3, 4 * PI / 3, 2 * PI):
            self.play(t.animate.set_value(fin), run_time=4,
                      rate_func=linear)
        self.add(MathTex(rf"M = {self.M}").to_corner(UL))
