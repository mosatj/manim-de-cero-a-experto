# Cómo se analizaría un pretest/postest. ¡Los datos son SIMULADOS!
# Sirven solo para ensayar el cálculo antes de recoger datos reales.
import numpy as np

rng = np.random.default_rng(2026)  # semilla: resultado repetible
pre_a = rng.normal(40, 12, 30).clip(0, 100)  # grupo con vídeos
post_a = (pre_a + rng.normal(25, 10, 30)).clip(0, 100)
pre_b = rng.normal(41, 12, 30).clip(0, 100)  # grupo de comparación
post_b = (pre_b + rng.normal(18, 10, 30)).clip(0, 100)


def ganancia(pre, post):
    """Ganancia normalizada de Hake (medias del grupo, 0-100)."""
    return (post.mean() - pre.mean()) / (100 - pre.mean())


def d_cohen(x, y):
    """Diferencia de medias / desviación típica combinada."""
    nx, ny = len(x), len(y)
    s = np.sqrt(
        ((nx - 1) * x.var(ddof=1) + (ny - 1) * y.var(ddof=1))
        / (nx + ny - 2)
    )
    return (x.mean() - y.mean()) / s


print("DATOS SIMULADOS (semilla 2026), n = 30 por grupo")
for nombre, pre, post in (
    ("A", pre_a, post_a),
    ("B", pre_b, post_b),
):
    print(
        f"Grupo {nombre}: pre = {pre.mean():5.1f}  post = "
        f"{post.mean():5.1f}  <g> = {ganancia(pre, post):.2f}"
    )
mejora_a, mejora_b = post_a - pre_a, post_b - pre_b
print(f"d de Cohen (mejoras): {d_cohen(mejora_a, mejora_b):.2f}")
