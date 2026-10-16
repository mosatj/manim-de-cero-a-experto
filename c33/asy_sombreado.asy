// Superficie sombreada: para esta ruta el puente es PDF → PNG.
import three;
import graph3;
import solids;
settings.render=0;
settings.prc=false;
size(9cm);
currentprojection=orthographic(1.5,6,2.2);
defaultpen(white+0.7bp);
real f(real x){return 1+0.5*sin(1.5*x);}
path3 gen=graph(new triple(real x){return (x,f(x),0);}, 0, 4, 40);
surface s=surface(revolution(O, gen, X));
draw(s, surfacepen=material(rgb("4F7C99")+opacity(0.9),
     emissivepen=rgb("1F3A4C")), meshpen=rgb("CFE0EA")+0.15bp);
draw(O--4.8X, white+0.8bp);
draw(O--2.2Y, white); draw(O--2.2Z, white);
label("$x$", 4.8X, S); label("$y$", 2.2Y, E); label("$z$", 2.2Z, N);
