// Campo de direcciones de la logística y' = y(1-y) y cinco
// soluciones trazadas por curve() de slopefield.
import graph;
import slopefield;
size(9cm, 6cm, IgnoreAspect);
pen crema=rgb("E9F2F7"), azul=rgb("6FA3C0"), ocre=rgb("E0B04A");
defaultpen(crema+0.7bp+fontsize(12pt));
real f(real x, real y) {return y*(1-y);}
pair a=(0,0), b=(6,1.5);
add(slopefield(f, a, b, 20, 12, azul+0.6bp));
real[] iniciales={0.05, 0.2, 0.5, 1.0, 1.4};
for(real y0 : iniciales)                       // soluciones (ocre)
  draw(curve((0,y0), f, a, b), ocre+1.3bp);
xaxis("$t$", BottomTop, LeftTicks(Step=1));
yaxis("$y$", LeftRight, RightTicks(Step=0.5));
