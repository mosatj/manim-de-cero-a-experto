from manim import *


class RecorridoPorCurva(Scene):
    def construct(self):
        # Lemniscata de Bernoulli, recorrida una vez
        def lemniscata(t):
            d = (1 + np.sin(t) ** 2) / 4
            return [np.cos(t) / d, np.sin(t) * np.cos(t) / d, 0]

        camino = ParametricFunction(lemniscata, t_range=[0, TAU],
                                    color=BLUE)
        # Dónde cae cada proporción del recorrido (0, 1/8, 2/8, ...)
        marcas = VGroup()
        for k in range(8):
            p = camino.point_from_proportion(k / 8)
            hacia = {2: UP, 6: DOWN}.get(k, normalize(p))
            rotulo = MathTex(f"{k}/8").scale(0.7).next_to(p, hacia)
            marcas.add(Dot(p, radius=0.06, color=GREY_B), rotulo)
        viajero = Dot(camino.get_start(), radius=0.13, color=YELLOW)
        self.add(marcas)
        self.play(Create(camino), MoveAlongPath(viajero, camino),
                  run_time=4, rate_func=linear)
        # Con otra rate_func el viaje termina a los 3/8 del camino
        self.play(MoveAlongPath(viajero, camino,
                                rate_func=lambda a: 3 * a / 8))
