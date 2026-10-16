// Un recorrido por el lenguaje. Entre corchetes, el índice
// de cada parte en el SVGMobject.
size(6cm);                          // ancho final del dibujo
pen azul=rgb("6FA3C0"), crema=rgb("E9F2F7"), granate=rgb("B04A5A");
defaultpen(crema+0.8bp+fontsize(14pt));
pair A=(0,0), B=(3,0), C=(2,2);     // pair: punto del plano
path tri=A--B--C--cycle;            // --: segmentos; cycle cierra
fill(tri, azul+opacity(0.35));      // [0] relleno translúcido
draw(tri);                          // [1] contorno
guide g=A..(1,1.6)..C;              // ..: curva suave (Hobby)
draw(g, granate+1.2bp);             // [2]
pair[] vertices={A, B, C};
for(pair P : vertices) dot(P);      // [3], [4], [5]
label("$A$", A, SW);                // [6]
transform T=shift(4,0)*rotate(30)*scale(0.6);
draw(T*tri, azul+1.2bp);            // [7] el triángulo transformado
