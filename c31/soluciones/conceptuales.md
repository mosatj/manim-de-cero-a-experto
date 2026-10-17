# Capítulo 31 · Manim en la enseñanza y la investigación

Soluciones de los ejercicios propuestos que no necesitan un programa (preguntas conceptuales, cálculos a mano, órdenes de terminal). Las demás soluciones están en los archivos `.py` de esta carpeta. Los números de sección y figura remiten al libro.

## Ejercicio 31.1 · nivel básico

Clasifica según la tipología de Chacón Hernández y Fernández Cifuentes (2024) estos cuatro vídeos: (a) una prueba de la fórmula del área del círculo que solo muestra anillos que se desenrollan; (b) un ejercicio resuelto de ley de senos con datos numéricos; (c) un problema sobre la altura de un edificio que termina preguntando «¿qué medirías tú?»; (d) la prueba de (a) narrada paso a paso.

**Solución.** (a) Argumento dinámico sin apoyo verbal; (b) situación problema: solución; (c) situación problema: exploración, porque plantea la necesidad y pide una propuesta; (d) argumento dinámico con apoyo verbal. El orden sugerido de visionado sería (c), (b), (a), (d).

## Ejercicio 31.2 · nivel básico

Reescribe como objetivos de aprendizaje con verbo observable: «que el alumno conozca la derivada» y «que el alumno entienda la suma de impares».

**Solución.** Por ejemplo: «El estudiante interpreta la derivada en un punto como la pendiente límite de las secantes y la estima en una gráfica» y «El estudiante justifica con una figura por qué $1+3+…+(2n-1)=n^2$». Los verbos *interpreta*, *estima* y *justifica* describen conductas que se pueden observar y evaluar; *conocer* y *entender* no.

## Ejercicio 31.4 · nivel básico

Un profesor tiene tres escenas sobre la suma de los ángulos de un triángulo: (a) un triángulo cuyos vértices se mueven mientras se oye «¿qué cambia y qué no?»; (b) la misma figura con el ángulo en $C$ resaltado y una recta paralela a $AB$ que pasa por $C$; (c) la prueba completa con los ángulos alternos internos y la fórmula final. Indica qué papel de la tabla ? cumple cada una y en qué momento de la clase la proyectarías.

**Solución.** (a) Es la tarea: se proyecta al comenzar, con la consigna de viva voz, y deja la pregunta abierta. (b) Es una pista: sugiere la construcción auxiliar sin completar el argumento, y se muestra durante el trabajo solo a los grupos atascados. (c) Es la consolidación: se proyecta al final, cuando todos los grupos han superado un mínimo, para formalizar lo que la clase ya descubrió. Proyectar (c) al principio sería nivelar por arriba.

## Ejercicio 31.8 · nivel intermedio

Tu colega afirma que sus vídeos funcionan porque el 90 \% de sus estudiantes dijo en una encuesta que le gustaron. Redacta tres preguntas que le harías para saber qué puede afirmar realmente.

**Solución.** Por ejemplo: (1) ¿Midió el aprendizaje, además de la opinión? Una encuesta de satisfacción no mide aprendizaje. (2) ¿Con qué se compara? Sin pretest o sin grupo de comparación no puede atribuirse la mejora al vídeo. (3) ¿Quién respondió? Si solo contestaron quienes vieron los vídeos, la muestra está sesgada. Con esos datos puede afirmar que los vídeos fueron bien recibidos, no que mejoraron el aprendizaje.

## Ejercicio 31.11 · nivel avanzado

Adapta `ganancia\_normalizada.py` para que lea las notas de un archivo CSV con columnas `grupo,pre,post`, en lugar de simularlas.

**Solución.** Se sustituye la simulación por una lectura con el módulo `csv`: se recorren las filas con `csv.DictReader`, se agrupan las notas en listas según la columna `grupo` y se convierten con `np.array(..., dtype=float)`. Las funciones `ganancia` y `d_cohen` no cambian, que es justamente la ventaja de haberlas separado de los datos. Conviene imprimir además el número de estudiantes de cada grupo, porque un $d$ calculado con muy pocos datos es poco fiable. El programa, con un CSV de ejemplo, es `codigo/c31/soluciones/ganancia\_csv.py`.

## Ejercicio 31.12 · nivel avanzado

Diseña una evaluación de un vídeo de exploración para dos secciones de un mismo curso. Especifica el diseño, el instrumento, el análisis y las precauciones éticas.

**Solución.** Un diseño razonable: dos grupos intactos con pretest y postest de la misma prueba (5 a 10 ítems sobre el teorema, validados por otro docente). Un grupo ve el vídeo y hace la actividad; el otro hace la misma actividad con una figura estática. Análisis: $\langle g\rangle$ por grupo y $d$ de Cohen sobre las mejoras, informando también el pretest para mostrar si los grupos eran comparables. Precauciones: consentimiento informado, anonimato de las notas, permiso institucional y acceso posterior al vídeo para el grupo de comparación. Limitación que debe declararse: con grupos intactos no se puede afirmar causalidad.
