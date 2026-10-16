// Una función con ejes y marcas de graph.asy, más dos marcas de
// registro para que Manim conozca sus coordenadas.
import graph;
import asy_registro;
size(9cm);
pen crema=rgb("E9F2F7"), azul=rgb("6FA3C0");
defaultpen(crema+0.7bp+fontsize(12pt));
real f(real x) {return x^3/6-x;}
// Los ejes se dibujan DEBAJO de lo que ya hay (above=false)
xaxis("$x$", -3.3, 3.3, Ticks(Step=1, step=0.5, OmitTick(0)),
      Arrow);
yaxis("$y$", -2.2, 2.2, Ticks(Step=1, step=0.5, OmitTick(0)),
      Arrow);
draw(graph(f, -3, 3), azul+1.4bp);
registro((-3,-2), (3,2));
