# Capítulo 30 · Flujo de trabajo profesional, rendimiento y ecosistema

Soluciones de los ejercicios propuestos que no necesitan un programa (preguntas conceptuales, cálculos a mano, órdenes de terminal). Las demás soluciones están en los archivos `.py` de esta carpeta. Los números de sección y figura remiten al libro.

## Ejercicio 30.1 · nivel básico

Escribe un `.gitignore` para un proyecto de Manim que usa uv, y explica qué debe versionarse y qué no.

**Solución.** Se ignora todo lo que se regenera: `media/` (vídeos, imágenes, fórmulas compiladas, voces sintetizadas en caché), `__pycache__/` y `*.pyc`, el entorno `.venv/` y los archivos del sistema o del editor (`.DS_Store`, `.vscode/`). El `.gitignore` del proyecto del capítulo es exactamente eso. Se versionan el código, `manim.cfg`, `pyproject.toml`, `uv.lock` (que fija las versiones exactas) y los recursos irrepetibles: imágenes, SVG y grabaciones de voz propias.

## Ejercicio 30.2 · nivel básico

Tienes el proyecto en `/leccion/` y ejecutas, desde `/`, la orden `manim -pql leccion/e01_pregunta.py Pregunta`. ¿Qué `manim.cfg` se usa? ¿Funcionará la importación de `componentes`?

**Solución.** Manim busca el archivo de carpeta como `manim.cfg` relativo al directorio de trabajo, es decir, en `/`, no en `/leccion/`: se ignora la configuración del proyecto (el fondo saldrá negro). La importación sí funciona, porque Manim añade a `sys.path` la carpeta del script antes de cargarlo, y allí está el paquete `componentes`. La solución es ejecutar siempre desde la raíz del proyecto (`cd leccion`) o pasar el archivo con `-c leccion/manim.cfg`.

## Ejercicio 30.3 · nivel básico

Escribe la orden que renderiza, en calidad media y con vista previa, solo las animaciones 2, 3 y 4 de `Demostracion`. ¿Qué capas se dibujarán?

**Solución.** `manim -pqm -n 2,4 e02_demostracion.py Demostracion`. Las animaciones se numeran desde 0 en el orden de los `.play()`: la 0 es la capa 1, así que se renderizan las capas 3, 4 y 5. Las animaciones 0 y 1 se calculan sin dibujarse para que el estado de la escena sea el correcto: al empezar el vídeo, las capas 1 y 2 ya están en pantalla.
