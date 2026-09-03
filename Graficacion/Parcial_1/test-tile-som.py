import matplotlib.pyplot as plt
import numpy as np

# 1. Definir la paleta de colores de la madera (de más claro a más oscuro)
PALETTE = {
    0: [0xD4, 0xA3, 0x73],  # Brillo / Highlight (Bordes iluminados)
    1: [0xBC, 0x8A, 0x5F],  # Color Base / Madera normal
    2: [0x8B, 0x5E, 0x34],  # Sombra Media / Vetras de la madera
    3: [0x60, 0x38, 0x13],  # Sombra Oscura / Oclusión de esquinas y bordes inferiores
}

# 2. Diseñar el mapa de píxeles (Tile 8x8)
# Se aplica luz direccional (arriba-izquierda claro, abajo-derecha oscuro)
tile_data = np.array([
    0,1,2,3,2,1,0,1,
    0,1,2,3,2,1,0,1,
    0,1,2,3,2,1,0,1,
    0,1,2,3,2,1,0,1,
    0,1,2,3,2,1,0,1,
    0,1,2,3,2,1,0,1,
    0,1,2,3,2,1,0,1,
    0,1,2,3,2,1,0,1,
])

# 3. Convertir el mapa de índices en una imagen RGB real
rgb_image = np.zeros((8, 8, 3), dtype=np.uint8)
for i in range(8):
    for j in range(8):
        rgb_image[i, j] = PALETTE[tile_data[i, j]]

# 4. Configurar y mostrar el gráfico con Matplotlib
fig, ax = plt.subplots(figsize=(5, 5))

# Usamos 'nearest' para evitar que Matplotlib difumine los píxeles (mantiene el Pixel Art)
ax.imshow(rgb_image, interpolation='nearest')

# Configuración estética para desarrollo de videojuegos (Ver la cuadrícula de píxeles)
ax.set_xticks(np.arange(-0.5, 8, 1), minor=True)
ax.set_yticks(np.arange(-0.5, 8, 1), minor=True)
ax.grid(which='minor', color='black', linestyle='-', linewidth=0.5)
ax.tick_params(which='both', bottom=False, left=False, labelbottom=False, labelleft=False)

plt.title("Tile de Madera 8x8 (Sombreado y Oclusión)", fontsize=12, pad=10)
plt.show()
