# while: repetir mientras la condición sea verdadera
x = 1.0
pasos = 0
while x < 100:
    x = x * 1.5
    pasos += 1
print(f"Tras {pasos} pasos, x = {x:.2f}")
