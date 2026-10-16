# Manim: de cero a experto — código del libro

Repositorio de recursos digitales del libro **«Manim: de cero a experto. Animaciones
matemáticas con Python para la enseñanza, la investigación y la creación de contenidos»**,
de Moisés Toledo (2026).

Aquí está todo el código del libro, **exactamente como aparece impreso**: el libro
lee los listados de estos mismos archivos, y todos se ejecutaron con Manim Community
(la versión con que se comprobó la edición figura en los preliminares del libro y en
`requirements.txt`).

- **Ejemplos y ejercicios resueltos:** cada uno en su propio archivo `.py`, con el nombre
  que aparece sobre el listado. Los pocos ejercicios resueltos que se hacen a mano (un
  cálculo, una demostración) están desarrollados en el libro y no llevan archivo.
- **Ejercicios propuestos:** las soluciones que son programas están en
  `cNN/soluciones/*.py`; las que no necesitan código (preguntas conceptuales, cálculos a
  mano, órdenes de terminal) están reunidas en `cNN/soluciones/conceptuales.md`, con su
  enunciado.

## Organización

```
codigo/
├── c01/ … c33/          un directorio por capítulo
│   ├── portada.py       imagen de apertura del capítulo
│   ├── *.py             un ejemplo por archivo (nombre = el que aparece sobre el listado)
│   └── soluciones/      soluciones de los ejercicios propuestos
│       ├── *.py             las que son programas
│       └── conceptuales.md  las que no necesitan código
├── apA/ … apE/          código de los apéndices
├── requirements.txt
├── ruff.toml            configuración del analizador de código
├── LICENSE              licencia MIT del código
└── renderizar_todo.py   renderiza todos los ejemplos (o los de un capítulo)
```

## Instalación (resumen del capítulo 2)

1. Instala [uv](https://docs.astral.sh/uv/) y, si vas a usar fórmulas, una distribución de
   LaTeX (MiKTeX en Windows, MacTeX en macOS, TeX Live en Linux).
2. Instala Manim:

   ```bash
   uv tool install manim
   manim checkhealth
   ```

   O, dentro de un entorno virtual: `uv venv && uv pip install -r requirements.txt`
   (incluye matplotlib, sympy y pandas, que usa el capítulo 33).
3. El capítulo 33 usa además [Asymptote](https://asymptote.sourceforge.io/) (viene con
   TeX Live y MacTeX; en MiKTeX se instala aparte).

## Descargar el código

- Sin Git: botón verde **Code → Download ZIP** en la página del repositorio.
- Con Git: `git clone https://github.com/mosatj/manim-de-cero-a-experto.git`

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

## Archivos con errores a propósito

Algunos programas del capítulo 3 (los que empiezan con `# error-esperado`) muestran
un error de Python para aprender a leerlo. `renderizar_todo.py` los ejecuta y comprueba
que el error aparezca; `_sangria.py` y `_dospuntos.py` tienen errores de sintaxis y
están excluidos del analizador en `ruff.toml`.

## Renderizar todo

```bash
python renderizar_todo.py          # todos los capítulos
python renderizar_todo.py c13 c14  # solo esos capítulos
```

## Licencia

El **código** de este repositorio se publica con la [licencia MIT](LICENSE): puedes
usarlo, modificarlo y compartirlo libremente para aprender, enseñar y crear tus propias
animaciones, citando la fuente. El **texto y las figuras del libro** están protegidos por
derechos de autor y no forman parte de esta licencia.
