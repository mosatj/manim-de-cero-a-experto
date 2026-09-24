# Una docstring explica qué hace la función; help() la muestra
def interpolar(a, b, t):
    """Devuelve el valor a una fracción t del camino de a a b.

    Con t = 0 se obtiene a; con t = 1, b; con t = 0.5, el medio.
    """
    return (1 - t) * a + t * b


help(interpolar)
print(interpolar(2, 10, 0.25))
