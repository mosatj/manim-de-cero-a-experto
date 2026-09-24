# Propuesto: conversión con un parámetro por defecto
def celsius_a_fahrenheit(c, decimales=1):
    return round(c * 9 / 5 + 32, decimales)


print(celsius_a_fahrenheit(100))
print(celsius_a_fahrenheit(36.6))
print(celsius_a_fahrenheit(-40))
print(celsius_a_fahrenheit(21.37, decimales=3))
