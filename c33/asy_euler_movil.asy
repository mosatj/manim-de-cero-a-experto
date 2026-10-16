// El vértice C recorre un arco; t en [0,1] llega desde la orden
// asy -u "t=..." (usersetting). Mismas órdenes en cada fotograma.
import geometry;
import asy_registro;
size(8cm);
real t=0;
usersetting();
pen crema=rgb("E9F2F7"), ocre=rgb("E0B04A"), verde=rgb("7FB89A"),
    granate=rgb("B04A5A");
defaultpen(crema+0.8bp+fontsize(13pt));
real ang=50+80*t;                          // de 50 a 130 grados
triangle tri=triangle((0,0), (6,0), (3+3.5*Cos(ang), 3.5*Sin(ang)));
point O=circumcenter(tri), H=orthocenter(tri), G=centroid(tri);
point N=(O+H)/2;                           // centro de los 9 puntos
draw(tri, crema+1.2bp);                                  // [0]
draw(circumcircle(tri), ocre);                           // [1]
draw(circle(N, abs(O-tri.A)/2), verde);                  // [2]
pair u=unit(H-O);                     // recta de Euler: 6 de largo
draw(N-3u--N+3u, granate+1.4bp);                         // [3]
dot(O, ocre+5bp); dot(G, crema+5bp); dot(H, verde+5bp);  // [4..6]
label("$O$", O, SE); label("$H$", H, W);                 // [7] [8]
registro((-1.2,-2.8), (7.2,4.8));     // caja fija: escala fija
