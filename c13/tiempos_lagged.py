# Cálculo de los tiempos de un LaggedStart, sin Manim.
# Imita lo que hace AnimationGroup.build_animations_with_timings().

duraciones = [1.0, 1.0, 1.0, 1.0, 1.0]   # run_time de cada una
lag_ratio = 0.3

inicios = [0.0]
for d in duraciones[:-1]:
    # la siguiente arranca cuando la actual lleva lag_ratio
    inicios.append(inicios[-1] + d * lag_ratio)
finales = [i + d for i, d in zip(inicios, duraciones)]
total = max(finales)

print(f"Duración natural del grupo: {total:.2f} s")
for k, (i, f) in enumerate(zip(inicios, finales)):
    print(f"  animación {k}: de {i:.2f} s a {f:.2f} s")

# Si se fuerza run_time=4, todos los tiempos se estiran por igual
escala = 4 / total
print(f"Con run_time=4 (factor {escala:.3f}):")
for k, (i, f) in enumerate(zip(inicios, finales)):
    i, f = i * escala, f * escala
    print(f"  animación {k}: de {i:.2f} s a {f:.2f} s")
