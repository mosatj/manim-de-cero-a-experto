// Proyecto: campo de direcciones de y' = x - y (slopefield), ejes
// con marcas y la solución exacta por (0,1). Euler lo pone Manim.
import graph;
import slopefield;
import asy_registro;
size(9cm);
pen crema=rgb("E9F2F7"), azul=rgb("6FA3C0"), ocre=rgb("E0B04A");
defaultpen(crema+0.7bp+fontsize(12pt));
real f(real x, real y) {return x-y;}
pair a=(0,0), b=(4,3.5);
add(slopefield(f, a, b, 17, 15, azul+0.7bp));      // segmentitos
real exacta(real x) {return x-1+2*exp(-x);}
draw(graph(exacta, 0, 4), ocre+1.6bp);               // y(x) exacta
xaxis("$x$", BottomTop, LeftTicks(Step=1, step=0.5));  // debajo
yaxis("$y$", LeftRight, RightTicks(Step=1, step=0.5));
registro(a, b);
