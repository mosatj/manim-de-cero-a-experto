# Capítulo 32 · Proyectos integradores

Soluciones de los ejercicios propuestos que no necesitan un programa (preguntas conceptuales, cálculos a mano, órdenes de terminal). Las demás soluciones están en los archivos `.py` de esta carpeta. Los números de sección y figura remiten al libro.

## Ejercicio 32.1 · nivel básico

En el proyecto 1, ¿cuánto duraría la narración si la voz real fuera de 130 palabras por minuto? ¿Qué hay que cambiar en el código para que el vídeo se ajuste?

**Solución.** La duración de cada frase es $palabras\times60/v+0{,}4$. El guion tiene 98 palabras y 7 frases: a 150 palabras por minuto son $39{,}2+2{,}8=42{,}0$ s, como indica el programa; a 130 son $98\times60/130+2{,}8\approx48{,}0$ s. Basta cambiar `PALABRAS_POR_MINUTO = 130` en `guion.py` y volver a renderizar las escenas: `decir` lee la duración de ese módulo.

## Ejercicio 32.5 · nivel básico

Cambia la semilla del proyecto 7 a 2027 y vuelve a renderizar `EstimarPi`. ¿Qué cambia y qué no? ¿Por qué no sirve de nada poner la semilla con `--seed`?

**Solución.** Cambian los puntos, la trayectoria y la estimación final (con 2027 el error será otro, probablemente de unas milésimas); no cambia la forma de embudo de la curva ni la conclusión. Basta editar `SEMILLA` en `azar.py`: el título del vídeo la lee de ahí, así que también cambia solo. `--seed` siembra `random` y `np.random.seed`, pero el proyecto usa `np.random.default_rng(SEMILLA)`, un generador propio que recibe su semilla al crearse (sección 30.5); la bandera no lo afecta.

## Ejercicio 32.13 · nivel avanzado

Convierte la cápsula del proyecto 4 en una versión horizontal 16:9 con el menor número de cambios posible. ¿Qué archivos tocarías?

**Solución.** Solo el módulo de formato: una copia, por ejemplo `formato\_horizontal.py`, con `config.pixel_width, config.pixel_height = 1920, 1080`, `config.frame_width, config.frame_height = 16, 9` y márgenes menores (las plataformas horizontales tapan poco), conservando los nombres `arriba`, `lineas`, `zona_segura` y las constantes. En `capsula.py` se cambia la primera línea por `import formato_horizontal as fv`. Como la altura del marco pasa de 16 a 9 unidades, conviene además colocar la circunferencia a la derecha y el texto a la izquierda; esa decisión de composición es la única que no puede automatizarse. Los dos archivos están en `codigo/c32/soluciones/` (`formato\_horizontal.py` y `p4\_capsula\_horizontal.py`).

## Ejercicio 32.14 · nivel avanzado

Explica cómo sustituirías el método `decir` del proyecto 1 para narrar con `manim-voiceover` (capítulo 29) sin modificar las escenas.

**Solución.** La escena base heredaría de `VoiceoverScene` (de `manim_voiceover`) además de fijar un servicio de voz en `setup` con `self.set_speech_service(...)`. El método `decir` abriría el bloque `with self.voiceover(text=texto(clave)) as tracker:` y dentro reproduciría las animaciones con `run_time=tracker.duration`, en lugar de usar `duracion(clave)`. Las escenas no cambian porque solo llaman a `self.decir(clave, ...)`: es el beneficio de haber encapsulado la narración en la escena base. En el repositorio, `codigo/c32/soluciones/narracion\_voz.py` implementa esta escena base con el servicio de ensayo del capítulo 29, y `p1\_demostracion\_con\_voz.py` narra la escena 2 del proyecto sin tocar su código.

## Ejercicio 32.15 · nivel avanzado

Diseña la lista de verificación de un noveno proyecto: la animación del método de Runge--Kutta de orden 4 para el vídeo suplementario de un artículo.

**Solución.** Una lista razonable: (1) los valores numéricos del vídeo salen del mismo módulo que la tabla del artículo; (2) el método se ha comprobado frente a la solución exacta y se ha medido su orden (capítulo 31); (3) cada pendiente $p_1,…,p_4$ tiene un color fijo, igual en la fórmula y en la figura; (4) la notación coincide con la del artículo; (5) el vídeo cumple el formato y el tamaño que exige la revista; (6) el repositorio incluye versión de Manim, entorno y orden de render; (7) el último fotograma resume la conclusión y puede usarse como figura estática.

## Ejercicio 32.18 · nivel avanzado

Supón que la región del proyecto 8 se gira alrededor del eje $y$ en lugar del eje $x$ (método de los *cascarones cilíndricos*). Sin escribir el código, indica qué módulos del proyecto cambian, cuáles no y qué fórmula sumaría `funcion.py`.

**Solución.** Cambia la matemática y la geometría, no la arquitectura. En `funcion.py`, `volumen_exacto` pasa a $2\pi\int_0^4 x f(x) dx$ y `volumen_discos` a una suma de cascarones, $2\pi x_i f(x_i) \Delta x$, con los mismos puntos medios; la partición no cambia. En `piezas.py`, `discos_2d` se sustituye por una función que dibuje el rectángulo de cada franja (ahora su altura es $f(x_i)$ y su «radio» es $x_i$) y, en el espacio, `discos_3d` por cilindros huecos de radio $x_i$, altura $f(x_i)$ y eje vertical (`direction=UP`), mientras que `superficie` se parametriza como $(x\cos v, f(x), x\sin v)$ para girar alrededor de $y$. Las dos escenas apenas cambian: siguen llamando a las fábricas por su nombre y leyendo los valores de `funcion.py`; solo hay que revisar la orientación de la cámara, porque el sólido ahora se levanta sobre el plano horizontal. Esa es la ventaja de haber separado la matemática, las piezas y las escenas. Para quien quiera ir más allá, `codigo/c32/soluciones/p8\_cascarones.py` escribe ese cambio y comprueba que la suma converge a $2\pi\int_0^4 x f(x) dx\approx 41{,}831$.
