# Capítulo 2 · Instalación y entorno de trabajo

Soluciones de los ejercicios propuestos que no necesitan un programa (preguntas conceptuales, cálculos a mano, órdenes de terminal). Las demás soluciones están en los archivos `.py` de esta carpeta. Los números de sección y figura remiten al libro.

## Ejercicio 2.1 · nivel básico

Escribe las órdenes de terminal que, partiendo de tu carpeta personal, crean una
carpeta `curso` con dos subcarpetas, `semana1` y `semana2`, y
te dejan situado en `semana2`. ¿Qué orden usarías para comprobar dónde estás
y cuál para ver las dos subcarpetas desde `semana2`?

**Solución.** Una secuencia válida en los tres sistemas es `cd`, `mkdir curso`,
`cd curso`, `mkdir semana1`, `mkdir semana2` y `cd semana2`. Con
`pwd` compruebas la carpeta actual. Para ver las dos subcarpetas hay que listar
la carpeta superior: `ls ..` (o `dir ..` en Windows).

## Ejercicio 2.2 · nivel básico

Indica a qué capa de la figura 2.1 pertenece el problema en cada
caso: (a) `uv` no se reconoce como orden; (b) el renderizado se detiene al crear
un `MathTex`; (c) `import manim` da `ModuleNotFoundError`;
(d) al escribir el programa, olvidas los dos puntos al final de
`def construct(self)`.

**Solución.** (a) Capa de `uv` (no está instalado o su carpeta no está en el PATH: hay que
reabrir la terminal). (b) Capa de LaTeX. (c) Capa de Manim: se está usando un Python
en el que Manim no está instalado (por ejemplo, falta `uv run`). (d) Ninguna capa
de la instalación: es un error de sintaxis de Python en tu programa, que se corrige
en el editor.

## Ejercicio 2.3 · nivel básico

Renderiza `PrimerVideo` en calidad baja y en calidad alta. ¿En qué carpetas
quedan los dos vídeos? ¿Por qué el segundo no borra al primero?

**Solución.** Los dos vídeos se llaman `PrimerVideo.mp4` y quedan dentro de
`media/videos/primer\_video/`: el de calidad baja (`-pql`) en la
subcarpeta `480p15` y el de calidad alta (`-pqh`) en `1080p60`.
No se pisan porque
Manim organiza los vídeos por archivo y, dentro, por calidad (resolución y fps). Sí
se sobrescribe el vídeo si vuelves a renderizar con la *misma* calidad.

## Ejercicio 2.5 · nivel intermedio

Explica la diferencia entre `uv add manim` y `uv tool install manim`. Una
docente quiere que sus 30 estudiantes tengan exactamente la misma versión de Manim
que ella para que los ejemplos del curso funcionen igual: ¿qué le recomiendas y qué
archivos debe repartir?

**Solución.** `uv add manim` instala Manim en el entorno virtual de un proyecto concreto y
anota la dependencia en `pyproject.toml` (con las versiones exactas en
`uv.lock`); las órdenes se ejecutan con `uv run`. `uv tool install
manim` instala una única copia global, disponible como orden `manim` en cualquier
carpeta. A la docente le conviene el proyecto: debe repartir `pyproject.toml`
y `uv.lock` (y sus escenas, pero no `.venv` ni `media/`).
Cada estudiante ejecuta `uv sync` en la carpeta y obtiene exactamente las mismas
versiones. Para mayor claridad puede fijar la versión con
`uv add "manim==X.Y.Z"`.

## Ejercicio 2.7 · nivel intermedio

En un cuaderno de Colab alguien ejecuta, en una sola celda, `\%pip install -q
mscene`, `import mscene`, `\%mscene -l manim` y `from mscene.manim import
*`, y después una escena con `MathTex`. Señala los dos errores de este
procedimiento y corrígelo.

**Solución.** Primer error: la importación `from mscene.manim import *` no puede ir en la misma
celda que la instalación, porque `\%mscene` reinicia la sesión al terminar; debe ir
en una celda nueva, después del reinicio. Segundo error: `-l` instala la versión
lite, sin LaTeX, con la que `MathTex` falla. Procedimiento correcto: celda 1,
`\%pip install -q mscene`, `import mscene` y `\%mscene manim`; celda 2,
`from mscene.manim import *`; celda 3, la escena, empezando por
`\%\%manim -qm NombreDeLaEscena`. Si ya se instaló la versión lite, hay que
reiniciar el entorno de ejecución desde cero, porque Mscene no reinstala Manim si ya
está presente.

## Ejercicio 2.9 · nivel avanzado

Una investigadora quiere que los vídeos de un artículo puedan reconstruirse
exactamente dentro de cinco años. Compara tres estrategias ---proyecto con
`uv.lock`, entorno de conda, contenedor de Docker con etiqueta de versión---
según qué fijan y qué dejan sin fijar.

**Solución.** Un proyecto de `uv` con `uv.lock` fija las versiones exactas de
Python y de todas las bibliotecas de Python (Manim, NumPy, PyAV…), pero no las
del sistema: la distribución de LaTeX, las fuentes instaladas o, en Linux, las
bibliotecas de Cairo y Pango pueden cambiar y alterar sutilmente el resultado. Un
entorno de conda (exportado con sus versiones) fija además Cairo y Pango, pero
tampoco LaTeX. Un contenedor de Docker con una etiqueta concreta
(`manimcommunity/manim:vX.Y.Z`), o mejor aún, identificado por su
*digest*, congela todo el sistema, LaTeX y fuentes incluidos: es la opción más
reproducible, a costa de depender de Docker. Lo ideal es combinar: el contenedor
para reconstruir y el `uv.lock` y el código en un repositorio para documentar
y poder actualizar.

## Ejercicio 2.10 · nivel avanzado

`manim checkhealth` comprueba que el ejecutable `manim` «pertenece» a Manim
Community. ¿En qué situación real fallaría esa comprobación aunque Manim Community
esté bien instalado? ¿Cómo lo comprobarías tú mismo desde la terminal?

**Solución.** Falla cuando en el PATH aparece antes otra orden llamada `manim`, típicamente la
de ManimGL, que también instala un ejecutable con ese nombre. Manim Community
seguiría accesible como `manimce` o con `python -m manim`. Para comprobarlo:
en macOS y Linux, `which -a manim` lista todas las órdenes `manim` del PATH en
orden de prioridad (en Windows, `where.exe manim`); y `manim --version` debe
empezar por `Manim Community`. Internamente, `checkhealth` abre el
ejecutable y busca en él la referencia al módulo `manim.__main__`.
