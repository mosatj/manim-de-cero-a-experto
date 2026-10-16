import sys
from pathlib import Path

CARPETA = Path(__file__).resolve().parent.parent / "proyecto7"
sys.path.insert(0, str(CARPETA))
from manim import *
from azar import puntos  # los mismos datos del proyecto
from vista import TableroPuntos
from estilo import DENTRO, PI_REF, TRAZO

N = 2000


def bajo_parabola(xy):
    """Lo único que cambia respecto al proyecto: la región."""
    return xy[:, 1] <= xy[:, 0] ** 2


class AreaParabola(Scene):
    def construct(self):
        datos = puntos(N)
        mascara = bajo_parabola(datos)
        tablero = TableroPuntos(lado=4.6)
        tablero.shift(LEFT * 2.8 + DOWN * 0.2)
        tablero.remove(tablero.arco)  # la frontera ya no es un arco
        origen = tablero.cuadrado.get_corner(DL)
        curva = ParametricFunction(
            lambda t: origen
            + tablero.lado * np.array([t, t**2, 0]),
            t_range=[0, 1], color=PI_REF, stroke_width=3,
        )
        tablero.add(curva)
        area = mascara.mean()  # el cuadrado tiene área 1
        texto = MathTex(
            r"\int_0^1 x^2\,dx \approx",
            rf"{area:.4f}",
            r"\quad\left(\tfrac13 = 0{,}3333\right)",
            font_size=36, color=TRAZO,
        ).shift(RIGHT * 3)
        texto[1].set_color(DENTRO)
        self.play(Create(tablero))
        self.play(tablero.anadir(datos, mascara), run_time=3)
        self.play(Write(texto))
        self.wait()
