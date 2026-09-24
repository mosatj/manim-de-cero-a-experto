# Varias cláusulas except, else y finally
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("  no se puede dividir entre cero")
        return None
    except TypeError as error:
        print("  tipos incorrectos:", error)
        return None
    else:                      # solo si no hubo excepción
        return resultado
    finally:                   # siempre, pase lo que pase
        print(f"  (terminó dividir({a!r}, {b!r}))")


for a, b in [(1, 4), (1, 0), ("1", 2)]:
    print(dividir(a, b))
