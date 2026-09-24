# Una función matemática y su tabla de valores
def f(x):
    return x ** 2 + 1


def g(x):
    return 2 * x + 3


for x in range(4):
    print(f"x={x}:  f={f(x):>2}  g={g(x):>2}  f(g(x))={f(g(x))}")
