# Ejercicio 32.14: la escena 2 del proyecto 1, narrada, sin tocar su código.
# Basta con que el módulo «narracion» que importa la escena sea el de voz.
import sys

import narracion_voz

sys.modules["narracion"] = narracion_voz  # la escena importará este módulo
from escena2_demostracion import Demostracion  # noqa: E402


class DemostracionConVoz(Demostracion):
    """La misma clase, ahora heredera de la GuionScene con voz."""
