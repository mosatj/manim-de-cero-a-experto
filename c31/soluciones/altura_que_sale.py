import sys
from pathlib import Path

# variacion_altura.py está en la carpeta madre: se añade a la ruta
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from manim import *
from variacion_altura import TrianguloConAltura


class AlturaQueSale(Scene):
    """Variación continua: C recorre una paralela a la base AB."""

    def construct(self):
        a, b = (-3, -1.5), (1, -1.5)
        x_c = ValueTracker(-1.5)  # abscisa del vértice C
        figura = always_redraw(
            lambda: TrianguloConAltura(a, b, (x_c.get_value(), 1.5))
        )
        # Fracción t de AB en la que cae el pie H (0 = A, 1 = B)
        t = always_redraw(
            lambda: MathTex(
                r"t = %.2f" % ((x_c.get_value() - a[0]) / 4),
                font_size=40,
            ).to_corner(UR)
        )
        self.add(figura, t)
        self.wait(0.5)
        # Pie dentro de AB, en B, fuera a un lado y al otro
        for destino in (1, 3.5, -4.5, 3.5):
            self.play(x_c.animate.set_value(destino), run_time=3)
            self.wait(0.5)
