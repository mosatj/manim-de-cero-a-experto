// Marcas de registro para Manim (clase Registro de asy_utiles.py):
// dos puntos magenta en coordenadas conocidas del dibujo.
pen marca=rgb("FF00FF")+2bp;
void registro(pair a, pair b) {
  dot(a, marca);
  dot(b, marca);
}
