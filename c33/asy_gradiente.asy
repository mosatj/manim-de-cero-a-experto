// Curvas de nivel (contour) y campo gradiente (vectorfield) de
// f(x,y) = x^2/4 + y^2.
import graph;
import contour;
import asy_registro;
size(9cm);
pen azul=rgb("6FA3C0"), granate=rgb("B04A5A");
real f(real x, real y) {return x^2/4+y^2;}
pair a=(-3,-2), b=(3,2);
real[] niveles={0.25, 0.75, 1.5, 2.5, 3.5};
draw(contour(f, a, b, niveles), azul+1bp);   // el borde las trocea
path gradiente(pair z) {return (0,0)--(z.x/2, 2*z.y);}
// 8 x 6 flechas escaladas a su celda; 3 partes cada una
add(vectorfield(gradiente, a, b, 8, 6, granate+0.7bp));
registro(a, b);
