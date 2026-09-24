class Polinomio:
    """coef[k] es el coeficiente de x**k."""

    def __init__(self, *coef):
        self.coef = list(coef)

    def __call__(self, x):         # p(2): el objeto es «llamable»
        return sum(a * x**k for k, a in enumerate(self.coef))

    def __add__(self, otro):
        n = max(len(self.coef), len(otro.coef))
        a = self.coef + [0] * (n - len(self.coef))
        b = otro.coef + [0] * (n - len(otro.coef))
        return Polinomio(*[x + y for x, y in zip(a, b)])

    def derivada(self):
        coef = [k * a for k, a in enumerate(self.coef)]
        return Polinomio(*coef[1:])

    def __str__(self):
        texto = ""
        for k in reversed(range(len(self.coef))):  # grado mayor 1.º
            a = self.coef[k]
            if a == 0:
                continue
            signo = " - " if a < 0 else " + "
            num = "" if abs(a) == 1 and k > 0 else str(abs(a))
            pot = "" if k == 0 else ("x" if k == 1 else f"x^{k}")
            texto += signo + num + pot
        if not texto:
            return "0"
        return texto[3:] if texto[1] == "+" else "-" + texto[3:]


p = Polinomio(1, -3, 2)              # 2x² - 3x + 1
q = Polinomio(0, 0, 0, 1)            # x³
print("p =", p, "| p(2) =", p(2), "| p' =", p.derivada())
print("p + q =", p + q, "| valores:", [p(x) for x in range(4)])
