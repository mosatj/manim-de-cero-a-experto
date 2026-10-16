# Corrige la doble resta de frame_center en la cámara 3D (Cairo).
# Basta importar este módulo antes de renderizar la escena.
import numpy as np
from manim.camera.three_d_camera import ThreeDCamera

_contexto_original = ThreeDCamera.get_cairo_context


def _contexto_sin_centro(self, pixel_array):
    # La matriz de Cairo no debe restar el centro: project_points
    # ya lo descontó al proyectar, y los objetos fijos en pantalla
    # no deben desplazarse con él.
    guardado = self.frame_center.copy()
    self._frame_center.move_to(np.zeros(3))
    try:
        return _contexto_original(self, pixel_array)
    finally:
        self._frame_center.move_to(guardado)


def _a_subpixeles(self, mobject, points):
    # Lo mismo para imágenes y nubes de puntos, que no pasan por
    # la matriz de Cairo sino por esta conversión a píxeles.
    puntos = self.transform_points_pre_display(mobject, points)
    resultado = np.zeros((len(puntos), 2))
    ancho = self.pixel_width / self.frame_width
    alto = -self.pixel_height / self.frame_height  # y hacia abajo
    resultado[:, 0] = puntos[:, 0] * ancho + self.pixel_width / 2
    resultado[:, 1] = puntos[:, 1] * alto + self.pixel_height / 2
    return resultado


ThreeDCamera.get_cairo_context = _contexto_sin_centro
ThreeDCamera.points_to_subpixel_coords = _a_subpixeles
