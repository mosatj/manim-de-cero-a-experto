// Puntos notables del triángulo con geometry.asy (P. Ivaldi).
// Pluma por defecto rgb: con un gris, lo no coloreado llega negro.
import geometry;
size(8cm);
pen crema=rgb("E9F2F7"), azul=rgb("6FA3C0"), ocre=rgb("E0B04A"),
    verde=rgb("7FB89A"), granate=rgb("B04A5A");
defaultpen(crema+0.8bp+fontsize(13pt));
triangle t=triangle((0,0), (6,0), (2,4));
point A=t.A, B=t.B, C=t.C;
point G=centroid(t), O=circumcenter(t), H=orthocenter(t);
draw(t, crema+1.2bp);                                   // [0]
label("$A$", A, SW); label("$B$", B, SE);               // [1] [2]
label("$C$", C, N);                                     // [3]
// [4..6] medianas: vértice -> punto medio del lado opuesto
draw(A--midpoint(t.BC), azul); draw(B--midpoint(t.CA), azul);
draw(C--midpoint(t.AB), azul);
// [7..9] mediatrices (hasta O) y [10] circunferencia circunscrita
draw(midpoint(t.AB)--O, ocre); draw(midpoint(t.BC)--O, ocre);
draw(midpoint(t.CA)--O, ocre); draw(circumcircle(t), ocre);
// [11..13] alturas: vértice -> pie de la altura
draw(A--foot(t.VA), verde); draw(B--foot(t.VB), verde);
draw(C--foot(t.VC), verde);
// [14] recta de Euler, de 2H-O a 2O-H (pasa por H, G y O)
draw(2H-O--2O-H, granate+1.4bp);
dot(G, azul+5bp); dot(O, ocre+5bp); dot(H, verde+5bp);  // [15..17]
label("$G$", G, 1.5*E); label("$O$", O, SE);            // [18] [19]
label("$H$", H, W);                                     // [20]
