from manim import *
from scipy.integrate import solve_ivp

# Péndulo amortiguado: theta'' = -sin(theta) - c theta'
C = 0.4


def campo(t, y):
    theta, omega = y
    return [omega, -np.sin(theta) - C * omega]


class RetratoSciPy(Scene):
    def construct(self):
        ejes = Axes(x_range=[-4, 4, 1], y_range=[-3, 3, 1],
                    x_length=10, y_length=5.5, tips=False)
        rotulos = ejes.get_axis_labels(r"\theta", r"\omega")
        self.add(ejes, rotulos)
        sol = solve_ivp(campo, [0, 12], [3.0, 0.0],
                        dense_output=True, rtol=1e-8)
        t = np.linspace(0, 12, 600)
        theta, omega = sol.sol(t)
        orbita = ejes.plot_line_graph(theta, omega,
                                      add_vertex_dots=False,
                                      line_color=BLUE_C)
        punto = Dot(ejes.c2p(theta[0], omega[0]), color=RED)
        self.add(punto)
        # plot_line_graph devuelve un VDict: la curva es su entrada
        camino = orbita["line_graph"]
        self.play(Create(camino), MoveAlongPath(punto, camino),
                  run_time=6, rate_func=linear)
        texto = Text(f"{len(sol.t)} pasos adaptativos de solve_ivp",
                     font_size=26).to_edge(DOWN)
        self.play(FadeIn(texto))
        self.wait()
