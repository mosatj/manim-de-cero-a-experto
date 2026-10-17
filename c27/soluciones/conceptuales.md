# Capítulo 27 · Comunicación visual y diseño de animaciones

Soluciones de los ejercicios propuestos que no necesitan un programa (preguntas conceptuales, cálculos a mano, órdenes de terminal). Las demás soluciones están en los archivos `.py` de esta carpeta. Los números de sección y figura remiten al libro.

## Ejercicio 27.1 · nivel básico

Indica qué principio de Mayer incumple cada decisión: (a) una música de fondo animada durante la explicación de un límite; (b) una leyenda en la esquina que dice «azul: $f$, rojo: $f'$»; (c) el texto completo de la narración en pantalla; (d) una fórmula de seis términos que aparece entera con un solo `Write()`; (e) la voz dice «la derivada» cinco segundos después de que aparezca $f'$.

**Solución.** (a) Coherencia: material ajeno que compite por la atención. (b) Contigüidad espacial: el rótulo debe ir junto a cada curva. (c) Redundancia: el canal visual se satura leyendo lo que ya se oye. (d) Segmentación: conviene escribir la fórmula por partes, con pausas, o con `lag_ratio`. (e) Contigüidad temporal: la voz debe nombrar $f'$ en el instante en que aparece.

## Ejercicio 27.2 · nivel básico

¿Qué principio clásico de la animación corresponde a cada herramienta? `rate_func=smooth`, `lag_ratio=0.2`, `path_arc=PI/2`, `running_start`, atenuar el resto con `.fade()`, `Indicate(scale_factor=1.5)`.

**Solución.** `smooth`: entrada y salida lentas. `lag_ratio`: continuidad y superposición de acciones. `path_arc`: arcos. `running_start`: anticipación. Atenuar el resto: puesta en escena. `scale_factor` alto: exageración (con mesura).

## Ejercicio 27.3 · nivel básico

Con la salida del programa `contraste.py`, responde: (a) ¿qué colores de la tabla no deberías usar para texto sobre el fondo negro de Manim?; (b) si cambias el fondo a blanco, ¿por qué `YELLOW` deja de servir?; (c) ¿por qué un 3:1 puede bastar para una curva gruesa y no para un subíndice?

**Solución.** (a) `BLUE\_E` (3,6:1, solo trazos gruesos), `PURE\_BLUE` (2,4:1) y `DARK\_GRAY` (2,2:1). (b) Su contraste sobre blanco es 1,4:1: amarillo claro sobre blanco casi no se distingue; con fondo blanco hay que usar colores oscuros. (c) Las pautas WCAG piden 4,5:1 para texto normal y 3:1 para texto grande y elementos gráficos: un subíndice es texto pequeño, con trazos finos que pierden contraste al suavizarse los bordes; una curva gruesa ocupa muchos píxeles y se percibe con menos contraste.

## Ejercicio 27.4 · nivel básico

Para cada decisión, di qué maestro de la sección 27.9 la desaconsejaría y propón el cambio en Manim: (a) todas las llamadas a `self.play` duran 1 s y no hay ningún `.wait()`; (b) el vídeo empieza con la definición $\varepsilon$–$\delta$ de límite; (c) cuatro histogramas superpuestos con transparencia; (d) un punto que avanza hacia la derecha pegado al borde derecho del cuadro; (e) un párrafo de cinco líneas centradas; (f) un `NumberPlane` con su estilo por defecto bajo una curva fina del mismo color.

**Solución.** (a) Williams y Lasseter: el tiempo da significado; varía `run_time`, haz breves los acentos y añade `.wait()` después de cada resultado. (b) Sanderson: nunca empieces con definiciones; abre con una pregunta concreta (¿a qué se acerca $\sin x/x$ cuando $x$ se acerca a 0?) y deja la definición para el final. (c) Tufte: múltiplos pequeños, cuatro paneles con la misma escala y `.arrange\_in\_grid()`. (d) Zettl: deja aire delante del vector de movimiento; empieza el recorrido a la izquierda. (e) Bringhurst y Lupton: líneas cortas en bandera a la izquierda (`aligned_edge=LEFT`, `Tex` con `tex_environment="flushleft"`), y probablemente menos texto, porque explicar es tarea de la voz. (f) Tufte, diferencia mínima eficaz: baja la cuadrícula con `background_line_style` (gris, fina, translúcida) y engruesa la curva.

## Ejercicio 27.8 · nivel intermedio

Analiza, sin programar, esta escena: doce puntos grises en fila; tres se vuelven rojos y a la vez otros tres empiezan a girar; una leyenda en la esquina explica qué significa cada cosa; la cámara se acerca mientras todo ocurre. Propón una versión mejor en tres pasos.

**Solución.** Hay tres focos simultáneos (color, giro, cámara), lo que viola la puesta en escena y satura la memoria de trabajo; la leyenda viola la contigüidad; el giro puede capturar la mirada aunque no sea lo importante (Lowe, 2003). Versión en tres pasos: (1) mover juntos los tres puntos del primer grupo (destino común) y colorearlos, con un rótulo junto a ellos; (2) repetir con el segundo grupo, sustituyendo el giro por un desplazamiento en otra dirección; (3) solo entonces acercar la cámara, con los demás objetos quietos.
