from manim import *

FUENTE = '''def buscar(a, x):
    bajo, alto = 0, len(a) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if a[medio] == x:
            return medio
        elif a[medio] < x:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1'''


def buscar_traza(a, x):
    """La misma función, pero anuncia cada línea que ejecuta."""
    v = {"bajo": None, "medio": None, "alto": None}
    yield 2, dict(v)
    v["bajo"], v["alto"] = 0, len(a) - 1
    while True:
        yield 3, dict(v)
        if not v["bajo"] <= v["alto"]:
            yield 11, dict(v)
            return
        yield 4, dict(v)
        v["medio"] = (v["bajo"] + v["alto"]) // 2
        yield 5, dict(v)
        if a[v["medio"]] == x:
            yield 6, dict(v)
            return
        yield 7, dict(v)
        if a[v["medio"]] < x:
            yield 8, dict(v)
            v["bajo"] = v["medio"] + 1
        else:
            yield 9, dict(v)
            yield 10, dict(v)
            v["alto"] = v["medio"] - 1


def tabla_variables(v):
    filas = [Text(f"{k} = {'·' if v[k] is None else v[k]}",
                  font_size=28) for k in v]
    return VGroup(*filas).arrange(DOWN, aligned_edge=LEFT)


class CodigoSincronizado(Scene):
    def construct(self):
        a, x = [2, 5, 8, 12, 16, 23, 38], 23
        codigo = Code(code_string=FUENTE, language="python",
                      paragraph_config={"font_size": 22})
        codigo.to_edge(LEFT, buff=0.4)
        lineas = codigo.code_lines
        resalte = Rectangle(width=codigo.background.width - 0.1,
                            height=0.42, stroke_width=0,
                            fill_color=YELLOW, fill_opacity=0.25)
        celdas = VGroup(*[
            VGroup(Square(0.6), Text(str(v), font_size=24))
            for v in a]).arrange(RIGHT, buff=0)
        for c in celdas:
            c[1].move_to(c[0])
        tabla = tabla_variables(dict.fromkeys(["bajo", "medio",
                                               "alto"]))
        cabecera = MathTex(rf"x = {x}", font_size=40)
        panel = VGroup(cabecera, celdas, tabla)
        panel.arrange(DOWN, buff=0.6).to_edge(RIGHT, buff=0.5)
        self.add(codigo, panel)

        def colocar(n):   # el rectángulo, a la altura de la línea n
            return resalte.copy().set_x(codigo.background.get_x())\
                .set_y(lineas[n - 1].get_y())

        resalte.become(colocar(1))
        self.play(FadeIn(resalte))
        for n, v in buscar_traza(a, x):
            nueva = tabla_variables(v).move_to(tabla)
            self.play(resalte.animate.become(colocar(n)),
                      Transform(tabla, nueva), run_time=0.6)
        encontrado = celdas[a.index(x)][0]
        self.play(encontrado.animate.set_fill(GREEN_D, 0.8))
        self.wait()
