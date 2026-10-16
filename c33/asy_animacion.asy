// El mismo triángulo animado SOLO con Asymptote (módulo animation):
// cada fotograma es una imagen; magick los une en un GIF.
import geometry;
import animation;
size(8cm);
pen crema=rgb("E9F2F7"), ocre=rgb("E0B04A"), granate=rgb("B04A5A");
defaultpen(crema+0.8bp);
animation a;
int n=24;
for(int k=0; k<n; ++k) {
  save();                                     // guarda el lienzo
  real ang=50+80*k/(n-1);
  pair C=(3+3.5*Cos(ang), 3.5*Sin(ang));
  triangle tri=triangle((0,0), (6,0), C);
  point O=circumcenter(tri), H=orthocenter(tri);
  draw(tri); draw(circumcircle(tri), ocre);
  pair u=unit(H-O), N=(O+H)/2;
  draw(N-3u--N+3u, granate+1.4bp);
  draw(box((-1.2,-2.8), (7.2,4.8)), invisible);   // caja fija
  a.add();                                    // fotograma k
  restore();                                  // lienzo limpio
}
erase();
a.movie(delay=80);                  // GIF: 80 ms por imagen
