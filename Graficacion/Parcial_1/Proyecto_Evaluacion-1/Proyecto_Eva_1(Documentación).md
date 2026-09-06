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

## Los tiles.

### 0 Hierba / Pradera (0x00)

Propósito: Terreno transitable natural, base de la superficie continental.

- #4ade80 (Verde claro / Menta): Color de relleno base del suelo y briznas iluminadas.
- #22c55e (Verde medio): Textura media para dar volumen al césped.
- #86efac (Verde pastel brillante): Puntos de luz y destellos en las puntas de la hierba.
- #16a34a (Verde hoja oscuro): Sombras de briznas y profundidad.
- #15803d (Verde musgo profundo): Píxeles de contraste y base de sombra.

### 1 Tierra / Sendero (0x01)

Propósito: Caminos trillados, senderos de tierra, calzadas rurales.

- #b45309 (Marrón arcilla / Ocre medio): Tono base uniforme de la tierra pisada.
- #92400e (Marrón chocolate): Surcos y marcas de rodadura de carruajes o pisadas.
- #d97706 (Ámbar tostado): Elevaciones suaves de tierra suelta.
- #78350f (Marrón café profundo): Grietas y bordes sombreados del sendero.
- #f59e0b (Amarillo ocre cálido): Piedrecillas o granos de arena iluminados en el camino.

### 2 Agua / Océano (0x02)

Propósito: Masa de agua profunda, ríos, costas y obstáculos acuáticos.

- #0284c7 (Azul celeste intenso): Masa de agua y superficie principal.
- #38bdf8 (Azul cielo claro): Cresta de las olas y reflejo de luz diurna.
- #7dd3fc (Celeste brillante): Espuma superficial de las olas.
- #0369a1 (Azul marino medio): Cuerpo inferior de la masa acuática.
- #075985 (Azul abisal oscuro): Profundidad y sombra en el fondo de las ondas.

### 3 Arena / Orilla (0x03)

Propósito: Playas, dunas del desierto y transición suave entre tierra y agua.

- #fde047 (Amarillo arena suave): Base arenosa seca expuesta al sol.
- #fef08a (Amarillo pálido): Reflejo brillante de cuarzo/granos finos de arena.
- #eab308 (Dorado cálido): Ondulaciones y dunas de viento.
- #ca8a04 (Ocre mostaza sombrío): Arena mojada en la rompiente o sombras de relieve.

### 4 Muro de Piedra / Fortaleza (0x04)

Propósito: Murallas, mazmorras, fortalezas y límites infranqueables.

- #64748b (Gris pizarra medio): Bloques de cantería y ladrillos de piedra.
- #94a3b8 (Gris claro / Acero): Borde biselado superior donde impacta la luz.
- #334155 (Gris oscuro carbón): Líneas horizontales y verticales de mortero/juntas.
- #1e293b (Gris azulado profundo): Sombras oclusivas bajo los sillares.

### 5 Árbol / Follaje denso (0x05)

Propósito: Bosques, copas de vegetación densa y obstáculos de paso.

- #166534 (Verde esmeralda oscuro): Borde exterior de la copa del árbol.
- #15803d (Verde bosque): Capa principal de hojas.
- #22c55e (Verde vivo): Sección superior iluminada de las ramas.
- #86efac (Verde lima claro): Punto focal de luz en la parte superior central.
- #14532d (Verde pino sombrío): Sombra inferior proyectada por el follaje.

### 6 Adoquín / Plaza (0x06)

Propósito: Suelo de aldea, plazas urbanas, caminos de piedra y patios de castillo.

- #475569 (Gris frío medio): Fondo y masa de losetas de piedra cortada.
- #64748b (Gris losa claro): Caras de adoquines individuales.
- #94a3b8 (Gris tiza brillante): Esquinas resaltadas del empedrado.
- #334155 (Gris asfalto): Separación entre los adoquines.
- #1e293b (Azul oscuro / Negro suave): Hendiduras profundas en el pavimento.

### 7 Lava / Fuego (0x07)

Propósito: Peligro ambiental, foso del inframundo, cráteres activos y trampas.

- #ea580c (Naranja fuego): Flujo de magma fundido base.
- #fbbf24 (Amarillo ámbar incandescente): Manchas ardientes que emergen del núcleo.
- #facc15 (Amarillo oro ardiente): El punto de mayor temperatura térmica.
- #f97316 (Naranja volcánico): Transición térmica entre el núcleo y la corteza.
- #c2410c (Rojo teja ardiente): Borde de enfriamiento del magma.
- #9a3412 (Marrón rojizo quemado): Escoria y costra de roca volcánica enfriada.
