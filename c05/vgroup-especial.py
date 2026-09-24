from manim import *

grupo = VGroup(Circle(), Square(), Triangle())
print("print(grupo) ->", grupo)                 # VGroup.__str__
print("len(grupo)   ->", len(grupo))            # Mobject.__len__
print("grupo[0]     ->", repr(grupo[0]))        # __getitem__
print("grupo[1:]    ->", repr(grupo[1:]))    # rebanada: otro VGroup
print("for m in grupo ->", [type(m).__name__ for m in grupo])
mas = grupo + Dot()                             # VGroup.__add__
print("grupo + Dot()  ->", mas, "| original:", len(grupo))
