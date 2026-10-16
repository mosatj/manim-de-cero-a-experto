// Mediatriz de AB con regla y compás, con geometry.asy.
import geometry;
size(7cm);
pen crema=rgb("E9F2F7"), azul=rgb("6FA3C0"), granate=rgb("B04A5A");
defaultpen(crema+0.8bp+fontsize(13pt));
point A=(0,0), B=(4,0);
real r=0.7*abs(B-A);                 // abertura: más de AB/2
point[] P=intersectionpoints(circle(A,r), circle(B,r));
draw(A--B, crema+1.2bp);                              // [0]
dot(A, crema+5bp); dot(B, crema+5bp);                 // [1] [2]
label("$A$", A, W); label("$B$", B, E);               // [3] [4]
for(point Q : P) {              // [5..8] arcos junto a cada corte
  real a=degrees(Q-A), b=degrees(Q-B);
  draw(arc(A, r, a-14, a+14), azul);
  draw(arc(B, r, b-14, b+14), azul);
}
dot(P[0], azul+5bp); dot(P[1], azul+5bp);             // [9] [10]
pair M=(A+B)/2;
pair u=P[1]-P[0];
draw(P[0]-0.25u--P[1]+0.25u, granate+1.4bp);         // [11]
dot(M, granate+5bp); label("$M$", M, SE);             // [12] [13]
