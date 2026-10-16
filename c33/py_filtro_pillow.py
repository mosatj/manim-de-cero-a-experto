from manim import *
from PIL import Image, ImageDraw


def imagen_sintetica(n=96):
    """Un disco y una barra dibujados con Pillow, como matriz."""
    im = Image.new("L", (n, n), 30)
    dibujo = ImageDraw.Draw(im)
    dibujo.ellipse([12, 12, 60, 60], fill=230)
    dibujo.rectangle([62, 20, 88, 80], fill=140)
    return np.asarray(im)          # alto x ancho, valores 0-255


def bordes(matriz):
    """Filtro de Sobel: magnitud del gradiente, fila a fila."""
    k = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=float)
    m = matriz.astype(float)
    gx = np.zeros_like(m); gy = np.zeros_like(m)
    for i in range(3):
        for j in range(3):
            tro = np.roll(np.roll(m, i - 1, 0), j - 1, 1)
            gx += k[i, j] * tro
            gy += k[j, i] * tro
    mag = np.hypot(gx, gy)
    return (255 * mag / mag.max()).astype(np.uint8)


class FiltroPorFilas(Scene):
    def construct(self):
        original = imagen_sintetica()
        filtrada = bordes(original)
        filas = ValueTracker(0)

        def parcial():
            k = int(filas.get_value())
            mezcla = original.copy()
            mezcla[:k] = filtrada[:k]       # filas ya filtradas
            im = ImageMobject(mezcla).set_resampling_algorithm(
                RESAMPLING_ALGORITHMS["nearest"])
            im.height = 5
            return im

        izquierda = ImageMobject(original)
        izquierda.set_resampling_algorithm(
            RESAMPLING_ALGORITHMS["nearest"])
        izquierda.height = 5
        izquierda.shift(LEFT * 3.4)
        derecha = always_redraw(parcial)
        derecha.shift(RIGHT * 3.4)
        self.add(izquierda, derecha)
        self.add(
            Text("original", font_size=26).next_to(izquierda, DOWN),
            Text("bordes (Sobel)", font_size=26)
            .next_to(derecha, DOWN),
        )
        self.play(filas.animate.set_value(96), run_time=4,
                  rate_func=linear)
        self.wait()
