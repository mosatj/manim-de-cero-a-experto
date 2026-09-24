from manim import *
from math import comb


class TableroGalton(Scene):
    def construct(self):
        filas, dx, dy = 6, 0.8, 0.5
        arriba, base = 3.4, -3.7
        clavos = VGroup(*[
            Dot([(k - f / 2) * dx, arriba - f * dy, 0], radius=0.07)
            for f in range(filas) for k in range(f + 1)
        ])
        techo = arriba - filas * dy          # bajo la última fila
        paredes = VGroup(*[
            Line([(k - filas / 2 - 0.5) * dx, base, 0],
                 [(k - filas / 2 - 0.5) * dx, techo, 0],
                 color=GREY_B, stroke_width=2)
            for k in range(filas + 2)
        ])
        self.add(clavos, paredes)

        rng = np.random.default_rng(5)
        pila = [0] * (filas + 1)             # bolas en cada casilla
        r = 0.13
        bolas = VGroup()
        for _ in range(8):
            saltos = rng.integers(0, 2, filas)   # 1 = derecha
            x, camino = 0.0, [np.array([0, arriba + 0.5, 0])]
            for f, s in enumerate(saltos):
                x += s - 0.5                     # medio paso
                y = arriba - f * dy - dy / 2
                camino.append(np.array([x * dx, y, 0]))
            k = int(saltos.sum())                # casilla final
            y = base + r + 2 * r * pila[k]
            camino.append(np.array([(k - filas / 2) * dx, y, 0]))
            pila[k] += 1
            trayecto = VMobject().set_points_as_corners(camino)
            bola = Dot(camino[0], radius=r, color=RED_C)
            bolas.add(bola)
            self.play(MoveAlongPath(bola, trayecto),
                      rate_func=linear, run_time=1)

        # Muchas bolas: histograma de 400 lanzamientos simulados
        n = 400
        conteo = np.bincount(rng.binomial(filas, 0.5, n),
                             minlength=filas + 1)
        escala = 0.03                         # unidades por bola
        barras = VGroup(*[
            Rectangle(width=0.8 * dx, height=max(c, 1) * escala,
                      fill_color=TEAL_D, fill_opacity=0.9,
                      stroke_width=1).move_to(
                [(k - filas / 2) * dx, base, 0], aligned_edge=DOWN)
            for k, c in enumerate(conteo)
        ])
        crecer = [GrowFromEdge(b, DOWN) for b in barras]
        self.play(FadeOut(bolas),
                  LaggedStart(*crecer, lag_ratio=0.15), run_time=2)
        # Lo esperado: n·C(filas, k)/2^filas y su campana normal
        esperados = VGroup(*[
            Dot([(k - filas / 2) * dx,
                 base + n * comb(filas, k) / 2**filas * escala, 0],
                color=YELLOW)
            for k in range(filas + 1)
        ])
        s = np.sqrt(filas / 4)               # desviación típica
        campana = FunctionGraph(
            lambda x: base + escala * n / (s * np.sqrt(TAU))
            * np.exp(-(x / dx) ** 2 / (2 * s ** 2)),
            x_range=[-3.2, 3.2], color=YELLOW)
        rotulo = MathTex(r"n = 400", font_size=40).to_corner(UR)
        self.play(FadeIn(esperados), Create(campana), Write(rotulo))
        self.wait()
