import sys
from pathlib import Path
from manim import *
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
DATOS = pd.read_csv(Path(__file__).parent.parent / "py_datos.csv")


class MediaMovil(Scene):
    def construct(self):
        filas = DATOS[DATOS["seccion"] == "B"]
        # rolling(3) promedia cada semana con las dos anteriores
        suave = filas["visitas"].rolling(3, min_periods=1).mean()
        ejes = Axes(x_range=[0, 7, 1], y_range=[0, 80, 20],
                    x_length=9, y_length=5, tips=False)
        cruda = ejes.plot_line_graph(filas["semana"],
                                     filas["visitas"],
                                     line_color=GREY_B)
        media = ejes.plot_line_graph(filas["semana"], suave,
                                     line_color=ORANGE,
                                     add_vertex_dots=False)
        leyenda = VGroup(
            Text("datos", font_size=24, color=GREY_B),
            Text("media móvil (3 semanas)", font_size=24,
                 color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        self.add(ejes)
        self.play(Create(cruda), FadeIn(leyenda[0]))
        self.play(Create(media), FadeIn(leyenda[1]))
        self.wait()
