# Manim 0.21: de cero a experto — código del libro

Repositorio de recursos digitales del libro **«Manim 0.21: de cero a experto. Animaciones
matemáticas con Python para la enseñanza, la investigación y la creación de contenidos»**,
de Moisés Toledo (2026).

Cada ejemplo, ejercicio resuelto y solución de ejercicio propuesto del libro está aquí en
su propio archivo, **exactamente como aparece impreso**: el libro lee el código de estos
mismos archivos, y todos se ejecutaron con Manim Community **v0.21.0**.

## Organización

```
codigo/
├── c01/ … c32/          un directorio por capítulo
│   ├── portada.py       imagen de apertura del capítulo
│   ├── *.py             un ejemplo por archivo (nombre = el que aparece sobre el listado)
│   └── soluciones/      soluciones de los ejercicios propuestos
├── apA/ … apE/          código de los apéndices
├── requirements.txt
└── renderizar_todo.py   renderiza todos los ejemplos (o los de un capítulo)
```

## Instalación (resumen del capítulo 2)

1. Instala [uv](https://docs.astral.sh/uv/) y, si vas a usar fórmulas, una distribución de
   LaTeX (MiKTeX en Windows, MacTeX en macOS, TeX Live en Linux).
2. Instala Manim:

   ```bash
   uv tool install manim==0.21.0
   manim checkhealth
   ```

   O, dentro de un entorno virtual: `uv venv && uv pip install -r requirements.txt`.

## Ejecutar un ejemplo

Desde la carpeta del capítulo:

```bash
cd c07
manim -pql primera_escena.py PrimeraEscena     # vista previa rápida
manim -pqh primera_escena.py PrimeraEscena     # alta calidad
manim -s  primera_escena.py PrimeraEscena      # solo el fotograma final (PNG)
```

Los archivos que no importan Manim (capítulos 3–6) son programas de Python normales:

```bash
python c03/saludo.py
```

## Renderizar todo

```bash
python renderizar_todo.py          # todos los capítulos
python renderizar_todo.py c13 c14  # solo esos capítulos
```

## Licencia

El texto del libro está protegido por derechos de autor. El código de este repositorio
puede usarse libremente para aprender, enseñar y crear tus propias animaciones.
