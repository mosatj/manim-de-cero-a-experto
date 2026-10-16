# Mide tiempo de render, peso del archivo y memoria máxima de las escenas de
# banco_20s.py (todas duran 20 s). Uso:
#     python medir_render.py            # todas las medidas (unos minutos)
#     python medir_render.py rapido     # solo calidad baja
# Cada medida desactiva la caché de vídeos parciales: renderiza todo desde
# cero. Las fórmulas de LaTeX se compilan una vez antes de medir.
import json
import platform
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ARCHIVO = "banco_20s.py"
CALIDADES = ["-ql", "-qm", "-qh", "-qk"]
ESCENAS = ["Banco20s", "BancoImagen", "BancoSonido", "Banco3D", "BancoDenso"]
VARIANTES = [  # sobre la escena vectorial, en calidad alta
    ("solo el último fotograma (-s)", ["-qh", "-s"]),
    ("GIF", ["-qh", "--format", "gif"]),
    ("WebM", ["-qh", "--format", "webm"]),
    ("MOV con transparencia (-t)", ["-qh", "-t"]),
    ("secuencia PNG", ["-qh", "--format", "png-sequence"]),
    # Con OpenGL, el archivo se escribe por defecto (necesita pantalla o
    # un contexto gráfico; en servidores como Colab puede no estar)
    ("renderizador OpenGL", ["-qh", "--renderer", "opengl"]),
]
RAPIDO = sys.argv[1:] == ["rapido"]
if RAPIDO:
    CALIDADES, VARIANTES = ["-ql"], []


def peso(carpeta, escena):
    """Bytes del resultado: un archivo, o la carpeta de PNG sumada."""
    finales = [p for p in Path(carpeta).rglob("*")
               if p.is_file() and escena in p.name
               and "partial_movie_files" not in p.parts
               and p.suffix in {".mp4", ".gif", ".webm", ".mov", ".png"}]
    return sum(p.stat().st_size for p in finales)


def medir(escena, banderas, cache=False):
    with tempfile.TemporaryDirectory() as tmp:
        return _medir(escena, banderas, cache, tmp)


def _medir(escena, banderas, cache, tmp, repetir=False):
    orden = [sys.executable, "-m", "manim", *banderas, "--media_dir", tmp,
             ARCHIVO, escena]
    if not cache:
        orden.insert(3, "--disable_caching")
    if sys.platform == "darwin":
        orden = ["/usr/bin/time", "-l", *orden]   # memoria máxima (bytes)
    elif Path("/usr/bin/time").exists():
        orden = ["/usr/bin/time", "-v", *orden]   # en kilobytes
    inicio = time.perf_counter()
    r = subprocess.run(orden, capture_output=True, text=True)
    segundos = time.perf_counter() - inicio
    ram = 0
    for linea in r.stderr.splitlines():
        if "maximum resident set size" in linea:      # macOS
            ram = int(linea.split()[0]) / 2**20
        elif "Maximum resident set size" in linea:    # Linux
            ram = int(linea.split()[-1]) / 2**10
    ok = r.returncode == 0
    if not ok:
        print(r.stderr[-600:])
    return {"segundos": round(segundos, 1),
            "MB": round(peso(tmp, escena) / 1e6, 2),
            "RAM_MB": round(ram), "ok": ok}


resultados = []
subprocess.run([sys.executable, "-m", "manim", "-ql", "-s", ARCHIVO,
                "Banco20s"], capture_output=True)  # calienta LaTeX
for escena in ESCENAS:
    for calidad in CALIDADES:
        m = medir(escena, [calidad])
        resultados.append({"escena": escena, "caso": calidad, **m})
        print(f"{escena:12}{calidad:6}{m['segundos']:8.1f} s"
              f"{m['MB']:9.2f} MB{m['RAM_MB']:7d} MB RAM")
for nombre, banderas in VARIANTES:
    m = medir("Banco20s", banderas)
    resultados.append({"escena": "Banco20s", "caso": nombre, **m})
    print(f"{nombre:34}{m['segundos']:8.1f} s{m['MB']:9.2f} MB")
if not RAPIDO:  # la caché: misma orden dos veces en la misma carpeta
    with tempfile.TemporaryDirectory() as tmp:
        _medir("Banco20s", ["-qh"], True, tmp)
        m = _medir("Banco20s", ["-qh"], True, tmp)
    resultados.append({"escena": "Banco20s", "caso": "-qh, 2.ª vez (caché)",
                       **m})
    print(f"{'-qh, segunda vez con caché':34}{m['segundos']:8.1f} s")
equipo = {"sistema": platform.platform(), "procesador": platform.processor(),
          "maquina": platform.machine(), "python": platform.python_version()}
Path("medidas.json").write_text(json.dumps(
    {"equipo": equipo, "resultados": resultados}, indent=2,
    ensure_ascii=False), encoding="utf-8")
print("Guardado en medidas.json")
