from manim import *


class LinealScene(LinearTransformationScene):
    """LinearTransformationScene con un arreglo para Manim v0.21.

    Scene usa el atributo moving_mobjects para su contabilidad de
    dibujo y LinearTransformationScene usa el MISMO nombre para su
    lista de objetos «móviles». Tras cualquier self.play() la lista
    queda llena de objetos ajenos y la transformación siguiente los
    arrastra (o falla). Vaciarla antes de cada transformación lo
    evita; a cambio, no uses add_moving_mobject con esta clase.
    """

    def apply_function(self, function, added_anims=[], **kwargs):
        self.moving_mobjects = []
        super().apply_function(function, added_anims, **kwargs)
