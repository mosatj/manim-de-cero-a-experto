# Capítulo 1 · ¿Qué es Manim?

Soluciones de los ejercicios propuestos que no necesitan un programa (preguntas conceptuales, cálculos a mano, órdenes de terminal). Las demás soluciones están en los archivos `.py` de esta carpeta. Los números de sección y figura remiten al libro.

## Ejercicio 1.1 · nivel básico

Explica con tus palabras, en dos o tres líneas cada una, la diferencia entre
(a) un lenguaje de programación y una biblioteca; (b) una animación de línea de
tiempo y una animación programática.

**Solución.** (a) Un lenguaje de programación es un idioma con reglas estrictas para dar
instrucciones a la computadora (Python, por ejemplo). Una biblioteca es código ya
escrito en ese lenguaje que se puede reutilizar: Manim es una biblioteca de Python que
aporta figuras, fórmulas y animaciones.
(b) En la línea de tiempo el autor coloca los objetos a mano en ciertos instantes
(fotogramas clave) y el programa rellena los intermedios. En la animación programática
el autor describe con código qué objetos hay y qué les ocurre, y la computadora calcula
todos los fotogramas.

## Ejercicio 1.2 · nivel básico

Clasifica cada archivo como imagen vectorial, mapa de bits o vídeo:
`logo.svg`, `foto.jpg`, `captura.png`, `articulo.pdf`
(con una gráfica hecha en un programa de cálculo), `clase.mp4`,
`animacion.gif`.

**Solución.** Vectoriales: `logo.svg` y, normalmente, la gráfica de `articulo.pdf`
(un PDF puede contener vectores y también imágenes rasterizadas incrustadas). Mapas de
bits: `foto.jpg` y `captura.png`. Vídeos: `clase.mp4` y
`animacion.gif`, que es una sucesión de mapas de bits (fotogramas) en un solo
archivo, sin sonido y con una paleta de como máximo 256 colores por fotograma.

## Ejercicio 1.3 · nivel básico

Una escena de Manim tiene tres animaciones de 2 s cada una y una pausa final de 1 s.
¿Cuántos fotogramas tiene su vídeo en calidad baja, media y 4K?

**Solución.** Duración: $3 \times 2 + 1 = 7$ s. Calidad baja (15 fps): $7 \times 15 = 105$
fotogramas. Media (30 fps): $7 \times 30 = 210$. 4K (60 fps): $7 \times 60 = 420$.

## Ejercicio 1.4 · nivel básico

Observa estas primeras líneas de tres programas encontrados en internet. ¿Para qué
versión de Manim fue escrito cada uno? ¿Cuál podrías ejecutar directamente con este
libro?

from manimlib.imports import *      # programa A
from manim import *                 # programa B
from manimlib import *              # programa C

**Solución.** A se escribió para la antigua ManimCairo (vídeos de 3Blue1Brown de 2019 o antes); B,
para Manim Community; C, para ManimGL. Solo B está pensado para la versión de este
libro, y aun así conviene comprobar que no use API obsoleta (`ShowCreation`,
`TextMobject`, `CONFIG`…), porque podría ser de una versión muy antigua de
Manim Community.

## Ejercicio 1.5 · nivel básico

En el programa `PrimerVistazo` de la sección 1.11: (a) clasifica
como escena, mobject o animación cada uno de estos nombres:
`Transform(cuadrado, circulo)`, `PrimerVistazo`, `titulo`,
`cuadrado`, `circulo`, `Write(titulo)` y `Create(cuadrado)`; (b) ¿cuántas animaciones
reproduce la escena y qué número le corresponde a cada una al usar `-n`?;
(c) `circulo` nunca se pasa a `.add()`: ¿por qué se ve un círculo al final?

**Solución.** (a) Escena: `PrimerVistazo`, que hereda de `Scene`. Mobjects: `titulo`
(un `Text`), `cuadrado` (un `Square`) y `circulo` (un
`Circle`). Animaciones: `Write(titulo)`, `Create(cuadrado)` y
`Transform(cuadrado, circulo)`.
(b) Cuatro, porque la pausa final también es una animación (`self.wait()`
reproduce un `Wait`): la 0 es `Write()`, la 1 `Create()`, la 2
`Transform()` y la 3 la pausa. Con `-n 2,2` se renderiza solo la
transformación.
(c) Lo que se ve no es `circulo`, sino `cuadrado`: `Transform()`
modifica los puntos y el estilo de `cuadrado` hasta que coinciden con los de
`circulo`, que sirve solo de molde y nunca entra en la escena.

## Ejercicio 1.6 · nivel intermedio

Para cada material, decide si usarías Manim, GeoGebra, un programa de diapositivas o
un editor de vídeo, y justifica: (a) un vídeo de 90 s que muestra cómo la serie de
Taylor de $\sin x$ se ajusta a la función al añadir términos; (b) la grabación de una
clase en el laboratorio con cortes y música; (c) una hoja interactiva en la que los
estudiantes mueven un deslizador para cambiar la pendiente de una recta.

**Solución.** (a) Manim: el autor controla el ritmo, cada polinomio se calcula con exactitud y la
animación se genera con un bucle sobre el número de términos. (b) Un editor de vídeo
(DaVinci Resolve, Shotcut, Kdenlive): se trata de montar grabaciones reales, algo para
lo que Manim no está pensado. (c) GeoGebra (o Desmos): la clave es que el estudiante
manipule el deslizador; un vídeo le quitaría la interacción.

## Ejercicio 1.7 · nivel intermedio

Estima cuánto ocuparían *sin comprimir* los fotogramas de un vídeo de 10 s en
calidad baja y en calidad 4K (3 bytes por píxel). Compáralo con los 18 KB que ocupan
los 3 s en calidad baja de la tabla 1.5 y explica por qué la
diferencia es tan grande.

**Solución.** Calidad baja: cada fotograma ocupa $854 \times 480 \times 3 = 1 229 760$ bytes
($\approx 1{,}23$ MB); en 10 s hay $10 \times 15 = 150$ fotogramas, unos 184 MB. 4K:
$3840 \times 2160 \times 3 = 24 883 200$ bytes ($\approx 24{,}9$ MB) por fotograma y
$10 \times 60 = 600$ fotogramas, casi 15 GB. Los 3 s en calidad baja de la tabla
ocuparían sin comprimir $45 \times 1{,}23 \approx 55$ MB, frente a 18 KB reales: un
factor de unas 3000 veces. El códec H.264 guarda sobre todo las diferencias entre
fotogramas, y en una escena de Manim típica casi todo es fondo negro inmóvil.

## Ejercicio 1.8 · nivel intermedio

Una animación `Transform` empieza en el segundo 1 de un vídeo y dura 2 s. Si el
vídeo va a 30 fps: (a) ¿qué número de fotograma se muestra en el instante 1,5 s
(numerando desde 0)?; (b) si $\alpha$ avanzara de manera uniforme ---lo que Manim
llama ritmo `linear`---, ¿cuánto valdría $\alpha$ en ese fotograma?; (c) por
defecto Manim usa el ritmo `smooth`, que empieza y termina despacio: ¿esperas un
$\alpha$ mayor o menor que en (b)?

**Solución.** (a) $1{,}5 \times 30 = 45$: el fotograma número 45. (b) Han pasado 0,5 s de los 2 s
que dura la animación, así que el tiempo relativo es $t = 0{,}25$ y, con ritmo
uniforme, $\alpha = 0{,}25$. (c) Menor: `smooth` arranca despacio, de modo que al
cuarto del tiempo aún se ha recorrido menos de un cuarto del camino. De hecho,
`smooth(0.25)` vale aproximadamente $0{,}07$ (y `smooth(0.5)` vale
exactamente $0{,}5$). El ejercicio 1.12 lo muestra en imágenes.

## Ejercicio 1.10 · nivel intermedio

Una profesora necesita tres versiones de la misma animación: (a) una cápsula vertical
para Reels; (b) una figura de 8 cm de ancho, en 16:9, para unos apuntes impresos a
300 ppp; (c) la versión que proyectará en su aula. Para cada una, escribe la orden de
Manim (y la configuración del archivo, si hace falta) y un cuidado de diseño propio
de ese destino.

**Solución.** (a) `manim -qh -r 1080,1920 archivo.py Escena`, con `config.frame_width = 8`
y `config.frame_height = 8 * 16 / 9` al principio del archivo; sin ese cambio del
marco todo se vería diminuto. La composición debe rehacerse en una columna, con letra
grande y una idea por pantalla.
(b) El ancho en píxeles es $8 \times 300/2{,}54 \approx 944{,}9$, es decir, 945; el
alto, $945 \times 9/16 \approx 531{,}6$, es decir, 532. La orden es
`manim -s -t -r 945,532 archivo.py Escena`: `-s` guarda solo el último
fotograma y `-t` deja el fondo transparente. Sobre papel hay que evitar el blanco y
los colores muy claros; si la figura no sale de un vídeo, TikZ o Asymptote la darían
en formato vectorial.
(c) `manim -qh archivo.py Escena` (1920$\times$1080 a 60 fps). Lo decisivo en el
aula es el contraste, el grosor del trazo y el tamaño de la letra; conviene probar el
vídeo desde el fondo del aula.

## Ejercicio 1.11 · nivel intermedio

Un divulgador prepara un vídeo de tres minutos: aparece hablando a cámara con música
de fondo; en el primer minuto se superpone a su imagen una animación de 20 s en la que
una recta tangente recorre una parábola, y la miniatura del vídeo es una ilustración
hecha a mano. (a) Reparte el trabajo entre Manim y otras herramientas. (b) La
animación de la tangente tiene nueve animaciones y él está puliendo la séptima.
Escribe, en orden, las órdenes del ciclo de trabajo que usaría hasta el render final.

**Solución.** (a) Manim produce solo la animación de la tangente, que es calculable (la recta sale
de la derivada). La grabación, la música, el montaje y la superposición son trabajo de
un editor de vídeo (DaVinci Resolve, Shotcut o Kdenlive), y la miniatura dibujada a
mano, de un programa de ilustración como Inkscape o Krita.
(b) Las animaciones se numeran desde 0, así que la séptima es la número 6. Un ciclo
razonable: `manim -pql -n 6,6 tangente.py Tangente` para ver solo ese tramo;
`manim -sql -n 0,6 tangente.py Tangente` para revisar el encuadre del estado en que
termina; `manim -pql tangente.py Tangente` para ver el borrador completo cuando
el tramo convenza, y por último `manim -qh -t tangente.py Tangente`, que con
`-t` produce un `.mov` con canal alfa listo para superponerlo en el
editor.

## Ejercicio 1.13 · nivel avanzado

Explica por qué la caché de Manim trabaja con un vídeo parcial *por cada
animación* y no con el vídeo completo. Si cambias el color del círculo en la línea 10
de `PrimerVistazo`, ¿qué vídeos parciales tendría que volver a calcular Manim y
cuáles podría reutilizar?

**Solución.** Si la caché guardara solo el vídeo completo, cualquier cambio mínimo obligaría a
rehacerlo entero. Al guardar un parcial por cada llamada a `play` (o a
`wait`), identificado por un *hash* de la animación, los objetos y la cámara,
basta recalcular los tramos afectados. Cambiar el color del círculo no altera el
`Write` del título ni el `Create` del cuadrado, cuyos parciales se reutilizan.
Sí cambia el `Transform`, porque su objetivo es el círculo, y también la pausa
final, porque en ella se ve el círculo con el color nuevo: esos dos parciales se
recalculan. Después se vuelven a unir todos en el `.mp4`.
