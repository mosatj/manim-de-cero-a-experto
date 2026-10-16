// Incentro y circunferencia inscrita con geometry.asy.
import geometry;
size(7cm);
pen crema=rgb("E9F2F7"), azul=rgb("6FA3C0"), ocre=rgb("E0B04A");
defaultpen(crema+0.8bp+fontsize(13pt));
triangle t=triangle((0,0), (6,0), (1.5,4));
point I=incenter(t);
draw(t, crema+1.2bp);                                     // [0]
// [1..3] bisectrices: del vértice al lado opuesto
vertex[] V={t.VA, t.VB, t.VC};
for(vertex v : V) {
  point[] Q=intersectionpoints(bisector(v), t);  // dónde corta
  draw(Q[0]--Q[1], azul);
}
draw(incircle(t), ocre+1.2bp);                            // [4]
dot(I, ocre+5bp); label("$I$", I, NE);                    // [5] [6]
