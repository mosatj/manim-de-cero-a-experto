# Tiempos de una Succession con duraciones distintas, sin Manim.
duraciones = [1.0, 2.0, 0.5]
lag_ratio = 1   # Succession: cada una espera a la anterior
inicios = [0.0]
for d in duraciones[:-1]:
    inicios.append(inicios[-1] + d * lag_ratio)
finales = [i + d for i, d in zip(inicios, duraciones)]
total = max(finales)
escala = 7 / total          # run_time=7 impuesto al grupo
print(f"Duración natural: {total} s; factor: {escala:.3f}")
for k, (i, f) in enumerate(zip(inicios, finales)):
    i, f = i * escala, f * escala
    print(f"  animación {k}: {i:.2f} s -> {f:.2f} s")
