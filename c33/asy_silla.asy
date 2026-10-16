// La lámina: superficie sombreada (va por PDF y PNG).
include "asy_silla_comun.asy";
surface s=surface(f, (-a,-a), (a,a), 16, Spline);
draw(s, surfacepen=material(azul+opacity(0.95), specularpen=black,
     emissivepen=rgb("1F3A4C")), meshpen=crema+0.15bp);
borde();
