// Espiral de Arquímedes dibujada en Asymptote.
import graph;
size(6cm);
defaultpen(white+0.6bp);
real r(real t){return 0.18*t;}
draw(polargraph(r, 0, 6pi, 400), rgb("6FA3C0")+1bp);   // [0]
draw((-3.6,0)--(3.6,0), gray(0.5));
draw((0,-3.6)--(0,3.6), gray(0.5));
