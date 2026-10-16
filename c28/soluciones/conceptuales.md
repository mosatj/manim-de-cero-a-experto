# Capítulo 28 · Del guion a la pantalla: guion digital, storyboard y creación de contenidos

Soluciones de los ejercicios propuestos que no necesitan un programa (preguntas conceptuales, cálculos a mano, órdenes de terminal). Las demás soluciones están en los archivos `.py` de esta carpeta. Los números de sección y figura remiten al libro.

## Ejercicio 28.1 · nivel básico

Reescribe como objetivos de aprendizaje observables: (a) «que entiendan la derivada»; (b) «ver el teorema de Pitágoras»; (c) «conocer la distribución normal».

**Solución.** Posibles respuestas: (a) «interpretar la derivada en un punto como la pendiente de la recta tangente y estimarla a partir de dos secantes»; (b) «explicar con una disección de áreas por qué $a^2+b^2=c^2$ en un triángulo rectángulo»; (c) «reconocer la forma de la distribución normal y calcular qué proporción de datos cae a menos de una desviación típica de la media». Lo común: un verbo que se puede comprobar (interpretar, explicar, calcular, reconocer) y un contenido acotado.

## Ejercicio 28.2 · nivel básico

Identifica los cinco momentos narrativos en este guion breve: «¿Sabías que al doblar un papel 42 veces llegaría a la Luna? Parece imposible. Cada doblez duplica el grosor: 0,1 mm, 0,2, 0,4… Tras 42 dobleces, $0{,}1 \cdot 2^{42}$ mm, unos 440 000 km. Así crece una exponencial. ¿Cuántos dobleces harían falta para llegar al Sol?».

**Solución.** Gancho: «al doblar un papel 42 veces llegaría a la Luna». Pregunta (implícita): «parece imposible», ¿cómo puede ser? Desarrollo: cada doblez duplica el grosor, con la secuencia 0,1; 0,2; 0,4… Revelación: $0{,}1 \cdot 2^{42}$ mm, unos 440 000 km. Cierre: «así crece una exponencial» y la pregunta nueva sobre el Sol. (Comprobación: $2^{42}\approx 4{,}4\cdot 10^{12}$, por $0{,}1$ mm da $4{,}4\cdot 10^{11}$ mm $=4{,}4\cdot 10^{5}$ km.)

## Ejercicio 28.3 · nivel básico

Un guion tiene 620 palabras de narración. Si lees a 150 palabras por minuto y dejas un respiro de 1 s en cada uno de sus 9 bloques, ¿cuánto dura el vídeo? ¿Qué harías si el objetivo es no pasar de 4 minutos?

**Solución.** $620/150 = 4{,}13$ min $\approx 248$ s, más 9 s de respiros: unos 257 s, es decir, 4 min 17 s. Para bajar de 4 minutos hay que quitar unos 20 s de voz, unas 45–50 palabras: busca frases que repitan lo que la imagen ya muestra (redundancia) o un ejemplo prescindible. Recortar el guion es preferible a acelerar la animación.

## Ejercicio 28.4 · nivel intermedio

Escribe el guion a dos columnas (cinco bloques) de una cápsula de un minuto que muestre por qué el área de un triángulo es $\frac{b h}{2}$, partiendo de un rectángulo.

**Solución.** Una propuesta:

-  *Gancho* — Vídeo: la fórmula $A=\frac{bh}{2}$ con el «2» resaltado. Audio: «¿De dónde sale ese dos?».

-  *Pregunta* — Vídeo: un triángulo rectángulo con $b$ y $h$. Audio: «¿Por qué la mitad?».

-  *Desarrollo* — Vídeo: se dibuja el rectángulo de lados $b$ y $h$ que lo contiene. Audio: «Completa el rectángulo: su área es $b$ por $h$».

-  *Revelación* — Vídeo: la diagonal divide el rectángulo en dos triángulos iguales; uno se superpone al otro. Audio: «La diagonal lo parte en dos triángulos iguales».

-  *Cierre* — Vídeo: la fórmula enmarcada. Audio: «Por eso, la mitad. ¿Y si el triángulo no es rectángulo?».

## Ejercicio 28.7 · nivel intermedio

Un vídeo incluye una fotografía con licencia CC BY-SA, una pieza musical CC BY-NC y el resto es obra tuya. ¿Qué licencia puedes dar al vídeo? ¿Podrías monetizarlo? ¿Cómo reconocerías la fotografía?

**Solución.** La cláusula SA obliga a publicar la obra derivada con la misma licencia (CC BY-SA), pero la música NC prohíbe el uso comercial, y CC BY-SA sí lo permite: las dos condiciones son incompatibles. Hay que sustituir uno de los dos materiales: por ejemplo, música CC BY o CC0. Con la música NC no podrías monetizar el vídeo. La fotografía se reconoce con título, autor, fuente (enlace) y licencia (enlace a CC BY-SA), en la descripción y, si es posible, en pantalla o en los créditos.

## Ejercicio 28.10 · nivel avanzado

Analiza críticamente esta decisión de producción: «Para que el vídeo parezca más dinámico, acelero la voz un 25 \% y reduzco todas las pausas a 0,2 s; así cabe en 3 minutos en lugar de 4». Propón una alternativa basada en los capítulos 27 y 28.

**Solución.** Acelerar la voz y eliminar pausas aumenta la carga transitoria: la información desaparece antes de procesarse y se pierden las pausas después de los resultados, cuando se consolida lo aprendido. También perjudica la accesibilidad (subtítulos que duran menos de lo que se tarda en leerlos). La alternativa es recortar el *guion*: eliminar redundancias entre voz e imagen, prescindir de un ejemplo secundario o dividir el contenido en dos vídeos con una idea cada uno. Si aun así el vídeo dura 4 minutos y el público lo necesita, 4 minutos bien segmentados es una duración razonable (Guo y otros, 2014; Lagerstrom y otros, 2015).
