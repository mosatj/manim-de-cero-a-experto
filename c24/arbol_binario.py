from manim import *


class ArbolBinario(Scene):
    def construct(self):
        claves = [8, 3, 10, 1, 6, 14, 4, 7, 13]
        estilo = {"radius": 0.3, "fill_color": TEAL_B}
        raiz = claves[0]
        g = Graph([raiz], [], labels=True, vertex_config=estilo,
                  layout={raiz: [0, 3, 0]})
        hijos = {raiz: [None, None]}       # [izquierdo, derecho]
        nivel = {raiz: 0}
        self.play(Create(g))
        for k in claves[1:]:
            ficha = LabeledDot(MathTex(str(k), color=BLACK),
                               radius=0.3, color=YELLOW)
            self.play(FadeIn(ficha.move_to([-5.5, 3, 0])),
                      run_time=0.4)
            actual = raiz
            while True:                    # bajar comparando
                lado = 0 if k < actual else 1
                sentido = LEFT if lado == 0 else RIGHT
                self.play(ficha.animate.next_to(
                              g[actual], UP + sentido, buff=0.05),
                          Indicate(g[actual], color=YELLOW),
                          run_time=0.5)
                if hijos[actual][lado] is None:
                    break
                actual = hijos[actual][lado]
            # Hueco libre: el salto horizontal se divide entre 2
            # en cada nivel para que los subárboles no se crucen
            d = nivel[actual] + 1
            dx = (-1 if lado == 0 else 1) * 3.2 / 2 ** (d - 1)
            destino = g[actual].get_center() + [dx, -1.2, 0]
            hijos[actual][lado] = k
            hijos[k], nivel[k] = [None, None], d
            self.play(ficha.animate.move_to(destino), run_time=0.5)
            self.remove(ficha)
            g.add_vertices(k, positions={k: destino}, labels=True,
                           vertex_config=estilo)
            self.play(g.animate.add_edges((actual, k)),
                      run_time=0.5)

        def inorden(v):              # izquierda, raíz, derecha
            if v is None:
                return []
            izq, der = hijos[v]
            return inorden(izq) + [v] + inorden(der)

        lista = r",\ ".join(map(str, inorden(raiz)))
        recorrido = MathTex(r"\text{inorden: }" + lista,
                            font_size=40).to_edge(DOWN)
        self.play(Write(recorrido))
        self.wait()
