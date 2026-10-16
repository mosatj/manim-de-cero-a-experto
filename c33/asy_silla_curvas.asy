// Curvas sobre la silla: solo path3, así que el SVG es vectorial.
include "asy_silla_comun.asy";
borde();                                         // [0..3]
draw((-a,-a,0)--(a,a,0), granate+1.4bp);         // [4] recta y = x
draw((-a,a,0)--(a,-a,0), granate+1.4bp);         // [5] recta y = -x
draw(graph(new triple(real t) {               // [6] círculo r = 1,2
    return F(1.2cos(t), 1.2sin(t));}, 0, 2pi, 80), ocre+1.4bp);
