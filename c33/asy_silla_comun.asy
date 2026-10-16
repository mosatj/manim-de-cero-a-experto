// Común a la lámina (PNG) y a las curvas (SVG): misma vista, mismo
// tamaño y mismo borde, así que las dos cajas coinciden.
import three;
import graph3;
settings.render=0;
settings.prc=false;
size(9cm);
currentprojection=orthographic(4,2.4,3);
pen crema=rgb("E9F2F7"), azul=rgb("4F7C99"), ocre=rgb("E0B04A"),
    granate=rgb("B04A5A");
real a=1.5;
real f(pair z) {return 0.5*(z.x^2-z.y^2);}
triple F(real x, real y) {return (x, y, f((x,y)));}
void borde() {                 // los cuatro lados de [-a,a]^2
  pair[] esquinas={(-a,-a), (a,-a), (a,a), (-a,a)};
  for(int k=0; k<4; ++k) {
    pair P=esquinas[k], Q=esquinas[(k+1)%4];
    draw(graph(new triple(real t) {
        pair R=P+t*(Q-P); return F(R.x, R.y);}, 0, 1, 30),
         crema+0.8bp);
  }
}
