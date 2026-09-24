# Propuesto: tabla de multiplicar alineada
print("   |" + "".join(f"{j:>4}" for j in range(1, 10)))
print("-" * 40)
for i in range(1, 10):
    fila = f"{i:>2} |"
    for j in range(1, 10):
        fila += f"{i * j:>4}"
    print(fila)
