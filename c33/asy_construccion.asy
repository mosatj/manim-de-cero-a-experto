// Secantes que tienden a la tangente, dibujadas en Asymptote.
// El orden de las órdenes draw/dot/label es el orden de los
// submobjects que verá Manim.
size(7cm);
// Pluma por defecto clara: la figura vivirá sobre fondo oscuro
defaultpen(white+0.6bp);
pen azul=rgb("6FA3C0"), ocre=rgb("E0B04A"), granate=rgb("B04A5A");
pair O=(0,0), A=dir(40);
draw(unitcircle, azul+1bp);              // [0] circunferencia
dot(A, ocre+5bp);                        // [1] punto A
label("$A$", A, 1.6*NE);                 // [2] la letra A
real[] angulos={160, 120, 90, 70};
for(real t : angulos){
  pair B=dir(t);
  draw(A+1.4*(B-A) -- A+1.3*(A-B), gray(0.7)+0.5bp);  // secante
  dot(B, white+3.5bp);                                 // punto B
}
pair T=rotate(90)*A;                     // dirección tangente en A
draw(A-1.5*T -- A+1.5*T, granate+1.2bp); // [11] tangente
