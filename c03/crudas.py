# Barras invertidas: secuencias de escape y cadenas crudas
print("Línea 1\nLínea 2")        # \n es un salto de línea
print("a\tb")                    # \t es un tabulador
print("\theta")                  # ¡sorpresa!: \t + "heta"
print(r"\theta")                 # cadena cruda: la \ es literal
print(r"\frac{a}{b} + \sqrt{2}")
