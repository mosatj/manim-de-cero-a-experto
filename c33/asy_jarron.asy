// Alambre 3D de un sólido de revolución: solo path3, nada de
// superficies, para que el SVG sea vectorial.
import three;
import graph3;
settings.render=0;
settings.prc=false;
size(8cm);
currentprojection=orthographic(1.5,6,2.2);
defaultpen(white+0.6bp);
pen azul=rgb("6FA3C0"), ocre=rgb("E0B04A");
real f(real x){return 1+0.5*sin(1.5*x);}
path3 gen=graph(new triple(real x){return (x,f(x),0);}, 0, 4, 40);
pen eje=gray(0.6);
draw(O--4.6X, eje); draw(O--2Y, eje); draw(O--2Z, eje);   // [0..2]
// [3..14] doce generatrices
for(int k=0; k<12; ++k) draw(rotate(30k, X)*gen, azul+0.4bp);
// [15..23] nueve circunferencias transversales
for(real x=0; x<=4; x+=0.5)
  draw(circle((x,0,0), f(x), X), ocre+0.4bp);
label("$x$", 4.6X, S);                            // [24]
