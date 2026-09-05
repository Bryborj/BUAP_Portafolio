# Mapa 2D con profundidad y viewport

## Objetivo

**Construir un mapa 2D utilizando matplotlib, incorporando una técnica de ~sombreado y/o oclusión~ para generar una sensación de profundidad sin utilizar graficos 3D**

### Requerimentos

- Estructura: Mapa base de 40 x 40 tiles.
- Viewport: Vizualización de 8 x 8 tiles.
- Mecánica de profundidad: Aplicar sombreado u oclusión para simular volumen sin utilizar motores 3D.
- Sistema Slicing: La extración de la porción visible del mapa debe realizarse dinámicamente utilizando los ejes x e y de la camara.
- Interacción y limites: El teclado debe controlar el desplazamiento de la camara, y el código debe evitar que la cámara salga de los bordes.
- Sustentación: Explicación técnica de la mecánica de profundidad y demostración en vivo de 10m.

### Colores Hexadecimal
- Madera:
	- #D4A373 <- Brillo.
	- #BC8A5F <- Color base.
	- #8B5E34 <- Sombra clara (Las betas).
	- #603813 <- Sombra oscura / Oclusión
- Piedra:
- Pasto:
- Tierra:
- Agua:

