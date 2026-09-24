from pathlib import Path
from manim import *

# La ruta se calcula desde este archivo: funciona desde
# cualquier carpeta de trabajo
AQUI = Path(__file__).resolve().parent
CSV = AQUI.parent / "datos" / "estudio.csv"


class HistogramaNotas(Scene):
    def construct(self):
        notas = np.loadtxt(CSV, delimiter=",", skiprows=1)[:, 1]
        bordes = [0, 4, 8, 12, 16, 20]
        conteo, _ = np.histogram(notas, bins=bordes)
        nombres = [f"[{a},{b})" for a, b in zip(bordes, bordes[1:])]
        # la última es cerrada
        nombres[-1] = "[16,20]"
        grafico = BarChart(values=conteo.tolist(),
                           bar_names=nombres, y_range=[0, 16, 4],
                           x_length=9, y_length=5, bar_width=0.95,
                           bar_colors=[TEAL_E, TEAL_B])
        titulo = Tex(f"Notas de {len(notas)} estudiantes")
        titulo.to_edge(UP)
        self.play(Write(titulo), Create(grafico))
        self.play(FadeIn(grafico.get_bar_labels(font_size=30)))
        self.wait()
