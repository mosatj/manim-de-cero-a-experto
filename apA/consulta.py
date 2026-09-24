import inspect, manim

# 1) La firma real del constructor, tal como la ve Python
print(inspect.signature(manim.Circle.__init__))

# 2) La cadena de herencia (MRO): de la clase concreta a object
print(" -> ".join(c.__name__ for c in manim.Dot.__mro__))

# 3) ¿Dónde se define un método? En la 1.ª clase del MRO con él
mro = manim.Square.__mro__
propietaria = next(c for c in mro if "next_to" in c.__dict__)
print("Square.next_to está definido en", propietaria.__name__)

# 4) Nombres de «from manim import *» que contienen «Arrow»
print(sorted(n for n in dir(manim)
             if "Arrow" in n and n[0].isupper()))
