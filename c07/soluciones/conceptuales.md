# Capítulo 7 · Tu primera escena

Soluciones de los ejercicios propuestos que no necesitan un programa (preguntas conceptuales, cálculos a mano, órdenes de terminal). Las demás soluciones están en los archivos `.py` de esta carpeta. Los números de sección y figura remiten al libro.

## Ejercicio 7.2 · nivel básico

Escribe la orden que, para la escena `Transformar` del archivo `transformar.py`: (a) abre una vista previa rápida; (b) guarda solo la última imagen en alta calidad; (c) produce un GIF de 720p llamado `transformacion.gif`; (d) renderiza en 4K con fondo transparente.

**Solución.** (a) `manim -pql transformar.py Transformar`. (b) `manim -sqh transformar.py Transformar`; la imagen queda en `media/images/transformar/`. (c) `manim -qm --format gif -o transformacion transformar.py Transformar`. (d) `manim -qk -t transformar.py Transformar`, que produce un archivo `.mov` con canal alfa.

## Ejercicio 7.5 · nivel intermedio

Con el archivo `varias\_escenas.py`: (a) ¿qué orden renderiza las dos escenas en calidad media con una sola llamada? (b) ¿En qué carpetas quedan los vídeos? (c) ¿Qué ocurre si escribes `manim -ql varias_escenas.py` sin nombre de escena?

**Solución.** (a) Con la bandera `-a`: `manim -qm -a` seguido del nombre del archivo; también puedes nombrar las dos escenas, una tras otra, después del archivo. (b) En `media/videos/varias\_escenas/720p30/EscenaUno.mp4` y `EscenaDos.mp4`: la carpeta lleva el nombre del archivo y la de la calidad. (c) Como hay dos escenas, Manim muestra una lista numerada y pregunta cuál renderizar; puedes responder con un número, con varios separados por comas o con `*` para todas.

## Ejercicio 7.6 · nivel intermedio

Escribe un `manim.cfg` para un proyecto en el que todos los renders deben: usar fondo blanco, calidad media, guardar solo la última imagen y dejar los resultados en una carpeta `renders/`. ¿Qué cambia si luego ejecutas `manim -qh archivo.py Escena`?

**Solución.** El archivo, en la carpeta del script, debe contener la sección `[CLI]` y, una por línea, las claves `background_color = WHITE`, `quality = medium_quality`, `save_last_frame = True` y `media_dir = ./renders`. Si después ejecutas `manim -qh ...`, la bandera tiene prioridad sobre el archivo: esa vez la imagen sale en calidad alta (1920 $\times$ 1080), pero se mantienen el fondo blanco, el modo de última imagen y la carpeta. Ojo: con fondo blanco, los objetos blancos por defecto (como `Text`) dejan de verse; hay que darles color. El archivo y una escena para probarlo están en `codigo/c07/soluciones/proyecto\_cfg/`.
