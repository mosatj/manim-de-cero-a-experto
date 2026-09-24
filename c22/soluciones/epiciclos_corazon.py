from manim import *


class EpiciclosCorazon(Scene):
    def construct(self):
        # Curva corazón: un polinomio trigonométrico de grado 4
        t = np.linspace(0, TAU, 256, endpoint=False)
        x = 16 * np.sin(t) ** 3
        y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) \
            - np.cos(4 * t)
        z = 0.2 * (x + 1j * y)
        c = np.fft.fft(z) / len(z)
        k = np.fft.fftfreq(len(z), d=1 / len(z))
        utiles = np.abs(c) > 1e-9           # coeficientes no nulos
        c, k = c[utiles], k[utiles]
        punta = lambda s: np.array([
            np.sum(c * np.exp(1j * k * s)).real,
            np.sum(c * np.exp(1j * k * s)).imag, 0])
        curva = ParametricFunction(punta, t_range=[0, TAU, 0.01],
                                   color=RED, stroke_width=5)
        texto = MathTex(rf"{len(c)}\ \text{{epiciclos bastan}}")
        self.play(Create(curva), run_time=3)
        self.add(texto.to_corner(UL))
        self.add(MathTex(r"k \in \{" + ", ".join(
            str(int(v)) for v in sorted(k)) + r"\}", font_size=32)
            .to_corner(DL))
