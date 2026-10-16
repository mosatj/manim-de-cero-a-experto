from manim import *
from asy_puente import importar_asy


class CompasAsy(Scene):
    """La mediatriz con regla y compás: el compás lo pone Manim."""

    def construct(self):
        fig = importar_asy("asy_compas.asy", height=7.2)
        fig.to_edge(LEFT, buff=0.8)
        for k in [3, 4, 13]:
            fig[k].set_fill("#E9F2F7")
        segmento, puntos = fig[0], fig[1:5]
        arcos, cortes = fig[5:9], VGroup(fig[9], fig[10])
        mediatriz, medio = fig[11], VGroup(fig[12], fig[13])
        centros = [fig[1], fig[2], fig[1], fig[2]]   # A, B, A, B

        pasos = VGroup(*[Text(t, font_size=32) for t in [
            "1. Abre el compás: r > AB/2",
            "2. Arcos desde A y desde B",
            "3. Une los dos cortes",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        pasos.to_edge(RIGHT, buff=0.5)

        self.play(Create(segmento), FadeIn(puntos))
        self.play(Write(pasos[0]))
        self.play(Write(pasos[1]))
        for arco, centro in zip(arcos, centros):
            # La pata del compás sigue la punta del arco
            pata = always_redraw(lambda c=centro, a=arco: Line(
                c.get_center(), a.get_end(), color="#E0B04A",
                stroke_width=3))
            self.add(pata)
            self.play(Create(arco), run_time=0.8)
            self.remove(pata)
        self.play(FadeIn(cortes, scale=1.5))
        self.play(Write(pasos[2]), Create(mediatriz), run_time=1.5)
        self.play(FadeIn(medio))
        self.wait()
