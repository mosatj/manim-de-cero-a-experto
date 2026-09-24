# Como las clases de Manim: fijar lo propio y reenviar el resto
def arco(radio=1.0, angulo=90, color="BLANCO", grosor=4):
    return (f"arco(radio={radio}, angulo={angulo}, "
            f"color={color}, grosor={grosor})")


def circulo(radio=1.0, color="ROJO", **kwargs):
    # un círculo es un arco de 360°; lo demás pasa tal cual
    return arco(radio=radio, angulo=360, color=color, **kwargs)


print(circulo())
print(circulo(2, grosor=8))
print(circulo(color="AZUL"))
