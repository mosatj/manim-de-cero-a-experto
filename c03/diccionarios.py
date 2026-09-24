# Diccionarios: pares clave -> valor
estilo = {"color": "azul", "radio": 1.5, "relleno": 0.5}
print(estilo["color"])
estilo["radio"] = 2          # cambiar un valor
estilo["borde"] = 4          # añadir una clave nueva
print(estilo)
print(len(estilo), "radio" in estilo)
print(estilo.get("grosor"), estilo.get("grosor", 1))
for clave, valor in estilo.items():
    print(f"{clave:>8} -> {valor}")
