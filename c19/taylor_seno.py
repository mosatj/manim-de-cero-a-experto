from manim import *
from math import factorial


def taylor_seno(m):
    """Polinomio de Taylor de sen x en 0 hasta el grado 2m + 1."""
    return lambda x: sum((-1)**k * x**(2*k + 1) / factorial(2*k + 1)
                         for k in range(m + 1))


def tramo_visible(p, tope=3, x_max=10):
    """Mayor X tal que |p(x)| <= tope en [-X, X] (p es impar)."""
    for x in np.linspace(0, x_max, 2001):
        if abs(p(x)) > tope:
            return x - x_max / 2000
    return x_max


class TaylorSeno(Scene):
    def construct(self):
        ejes = Axes(x_range=[-10, 10, 2], y_range=[-3, 3, 1],
                    x_length=12.5, y_length=5, tips=False)
        ejes.add_coordinates(font_size=22).shift(0.9 * DOWN)
        seno = ejes.plot(np.sin, x_range=[-10, 10], color=BLUE)

        def polinomio(m):
            p = taylor_seno(m)
            X = tramo_visible(p)
            return ejes.plot(p, x_range=[-X, X], color=YELLOW)

        def rotulo(m):
            n = 2 * m + 1
            return MathTex(rf"P_{{{n}}}(x)=\sum_{{k=0}}^{{{m}}}"
                           r"\frac{(-1)^k\,x^{2k+1}}{(2k+1)!}",
                           color=YELLOW).to_corner(UL)

        curva, texto = polinomio(0), rotulo(0)
        self.play(Create(ejes), Create(seno))
        self.play(Create(curva), Write(texto))
        for m in [1, 2, 4, 7]:
            self.play(Transform(curva, polinomio(m)),
                      Transform(texto, rotulo(m)), run_time=1.5)
