from math import exp, factorial

# Error de P_n(x) = Σ_{k≤n} x^k/k! en x = 1 frente a la cota
# de Lagrange: el resto es e^c/(n+1)! con 0 < c < 1, luego
# |e − P_n(1)| ≤ e/(n+1)!
x = 1.0
print(" n   error real      cota de Lagrange")
for n in range(1, 11):
    p = sum(x**k / factorial(k) for k in range(n + 1))
    error = abs(exp(x) - p)
    cota = exp(x) * x**(n + 1) / factorial(n + 1)
    print(f"{n:2d}   {error:.3e}       {cota:.3e}")
