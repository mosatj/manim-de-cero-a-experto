# Capítulo 29 · Voz, sonido, presentaciones y formatos de salida

Soluciones de los ejercicios propuestos que no necesitan un programa (preguntas conceptuales, cálculos a mano, órdenes de terminal). Las demás soluciones están en los archivos `.py` de esta carpeta. Los números de sección y figura remiten al libro.

## Ejercicio 29.2 · nivel básico

Escribe la orden que produce, a partir de la escena `E` del archivo `a.py`, un vídeo 1080p a 60 fps con fondo transparente. ¿Qué extensión tendrá el archivo y con qué códec se guardará? ¿Y si añades `--format webm`?

**Solución.** `manim -qh -t a.py E`. Como el mp4 con H.264 y `yuv420p` no admite canal alfa, Manim cambia a `E.mov` con el códec QuickTime RLE (`qtrle`, píxeles `argb`), sin pérdida y bastante pesado. Con `manim -qh -t --format webm a.py E` se obtiene `E.webm` con VP9 y alfa (`yuva420p`), mucho más ligero.

## Ejercicio 29.4 · nivel intermedio

Con `ServicioEnsayo` y 0,36 s por palabra, ¿cuánto durará la frase «Primero, el guion; después, la animación, y al final, la voz.»? Compruébalo después en una escena.

**Solución.** Separa la frase en palabras: *Primero, / el / guion; / después, / la / animación, / y / al / final, / la / voz.* Son 11 palabras, y 6 de ellas terminan en un signo de puntuación. Duración: $11\times 0{,}36 + 6\times 0{,}25 = 3{,}96 + 1{,}50 = 5{,}46$ s. En una escena basta con imprimir `t.duration` dentro de un `with self.voiceover(...) as t`. Este ejercicio muestra por qué conviene medir y no estimar a ojo: el ritmo depende tanto de las pausas como de las palabras.

## Ejercicio 29.10 · nivel avanzado

Vas a entregar una animación de 10 s como secuencia de PNG a 1080p60 para un editor de vídeo. ¿Cuántas imágenes se generarán? Si cada PNG ocupa unos 60 KB, ¿cuánto ocupará la secuencia y cuánto, aproximadamente, un mp4 de la misma animación a razón de 1 Mbit/s?

**Solución.** A 60 fps, 10 s son $600$ fotogramas, luego 600 archivos PNG (`manim -qh --format png-sequence a.py E`). A 60 KB cada uno, unos $36 000$ KB, es decir, unos 35 MB. El mp4 a 1 Mbit/s ocupa $10\times 1/8 = 1{,}25$ MB: casi treinta veces menos. La secuencia de PNG solo compensa si el editor necesita imágenes sin pérdida o con transparencia (añadiendo `-t`).
