import matplotlib.pyplot as plt
import numpy as np


# Tile de madera
def grassTile():
    # 1. Definir la paleta de colores de la madera (de más claro a más oscuro)
    PALETTE = {
        0: [0x4A, 0xDE, 0x80],  # Color Base
        1: [0x22, 0xC5, 0x5E],  # Color de volumen
        2: [0x86, 0xEF, 0xAC],  # Brillo / Puntos de luz
        3: [0x16, 0x34, 0x4A],  # Sombras / Profundidad
        4: [0x15, 0x80, 0x4D],  # Contraste / Base de sombra
    }

    # 2. Diseñar el mapa de píxeles (Tile 8x8)
    # Se aplica luz direccional (arriba-izquierda claro, abajo-derecha oscuro)
    tile_data = np.array([
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,2,0,0],
        [0,1,0,0,0,2,0,0],
        [0,1,0,0,0,0,0,0],
        [0,0,0,2,0,0,0,0],
        [0,0,0,0,0,0,3,3],
        [0,0,4,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ])
    return tile_data, PALETTE

# Tile de piedra
def dirtTile():
    # 1. Definir la paleta de colores de la piedra (de más claro a más oscuro)
    PALETTE = {
        0: [0xB4, 0x53, 0x09],  # Color Base
        1: [0x92, 0x40, 0x0E],  # Color de volumen
        2: [0xD9, 0x77, 0x06],  # Brillo / Puntos de luz
        3: [0x78, 0x35, 0x0F],  # Sombras / Profundidad
        4: [0xF5, 0x9E, 0x0B],  # Contraste / Base de sombra
    }

    # 2. Diseñar el mapa de píxeles (Tile 8x8)
    # Se aplica luz direccional (arriba-izquierda claro, abajo-derecha oscuro)
    tile_data = np.array([
        [1,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,2,2,0,0,0],
        [0,0,0,2,2,0,0,0],
        [0,0,0,0,0,0,4,0],
        [3,3,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,3,3,0],
    ])
    return tile_data, PALETTE

# Tile de pasto
def waterTile():
    # 1. Definir la paleta de colores de la pasto (de más claro a más oscuro)
    PALETTE = {
        0: [0x02, 0x84, 0xc7],  # Color Base
        1: [0x38, 0xbd, 0xf8],  # Color de volumen
        2: [0x7D, 0xD3, 0xFC],  # Brillo / Puntos de luz
        3: [0x03, 0x69, 0xA1],  # Sombras / Profundidad
        4: [0x07, 0x59, 0x85],  # Contraste / Base de sombra
    }

    # 2. Diseñar el mapa de píxeles (Tile 8x8)
    # Se aplica luz direccional (arriba-izquierda claro, abajo-derecha oscuro)
    tile_data = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 2, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [3, 3, 3, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 4, 4],
    ])
    return tile_data, PALETTE

# Tile de tierra
def SandTile():
    # 1. Definir la paleta de colores de la tierra (de más claro a más oscuro)
    PALETTE = {
        0: [0xFD, 0xE0, 0x47],  # Color Base
        1: [0xFE, 0xF0, 0x8A],  # Color de volumen
        2: [0xEA, 0xB3, 0x08],  # Brillo / Puntos de luz
        3: [0xCA, 0x8A, 0x04],  # Sombras / Profundidad
    }

    # 2. Diseñar el mapa de píxeles (Tile 8x8)
    # Se aplica luz direccional (arriba-izquierda claro, abajo-derecha oscuro)
    tile_data = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
    ])
    return tile_data, PALETTE

# Tile de agua
def WallStoneTile():
    # 1. Definir la paleta de colores del agua (de más claro a más oscuro)
    PALETTE = {
        0: [0x64, 0x74, 0x8B],  # Color Base
        1: [0x94, 0xA3, 0xB8],  # Color de volumen
        2: [0x33, 0x41, 0x55],  # Brillo / Puntos de luz
        3: [0x1E, 0x29, 0x3B],  # Sombras / Profundidad
    }

    # 2. Diseñar el mapa de píxeles (Tile 8x8)
    # Se aplica luz direccional (arriba-izquierda claro, abajo-derecha oscuro)
    tile_data = np.array([
        [2, 2, 2, 1, 2, 2, 2, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 2, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ])
    return tile_data, PALETTE

def TreeTile():
    # 1. Definir la paleta de colores de la madera (de más claro a más oscuro)
    PALETTE = {
        0: [0x16, 0x65, 0x34],  # Color Base
        1: [0x15, 0x80, 0x3D],  # Color de volumen
        2: [0x22, 0xC5, 0x5E],  # Brillo / Puntos de luz
        3: [0x86, 0xEF, 0xAC],  # Sombras / Profundidad
        4: [0x14, 0x53, 0x2D],  # Contraste / Base de sombra
    }

    # 2. Diseñar el mapa de píxeles (Tile 8x8)
    # Se aplica luz direccional (arriba-izquierda claro, abajo-derecha oscuro)
    tile_data = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 2, 2, 3, 3, 1, 4],
        [0, 1, 2, 2, 2, 2, 1, 4],
        [0, 1, 2, 2, 2, 2, 1, 4],
        [0, 1, 1, 1, 1, 1, 1, 4],
        [0, 4, 4, 4, 4, 4, 4, 4],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ])
    return tile_data, PALETTE

def CobbleTile():
    # 1. Definir la paleta de colores de la madera (de más claro a más oscuro)
    PALETTE = {
        0: [0x47, 0x55, 0x69],  # Color Base
        1: [0x64, 0x74, 0x8B],  # Color de volumen
        2: [0x94, 0xA3, 0xB8],  # Brillo / Puntos de luz
        3: [0x33, 0x41, 0x55],  # Sombras / Profundidad
        4: [0x1E, 0x29, 0x3B],  # Contraste / Base de sombra
    }

    # 2. Diseñar el mapa de píxeles (Tile 8x8)
    # Se aplica luz direccional (arriba-izquierda claro, abajo-derecha oscuro)
    tile_data = np.array([
        [1, 1, 1, 0, 2, 2, 2, 0],
        [1, 1, 1, 0, 2, 2, 2, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 3, 3],
        [0, 2, 2, 2, 0, 3, 3, 3],
        [0, 2, 2, 2, 0, 3, 3, 3],
        [0, 2, 2, 2, 0, 3, 3, 3],
        [4, 4, 4, 4, 0, 3, 3, 3],
    ])
    return tile_data, PALETTE

def LavaTile():
    # 1. Definir la paleta de colores de la madera (de más claro a más oscuro)
    PALETTE = {
        0: [0xEA, 0x58, 0x0C],  # Color Base
        1: [0xFB, 0xBF, 0x24],  # Color de volumen
        2: [0xFA, 0xCC, 0x15],  # Brillo / Puntos de luz
        3: [0xF9, 0x73, 0x16],  # Sombras / Profundidad
        4: [0xC2, 0x41, 0x0C],  # Contraste / Base de sombra
        5: [0x9A, 0x34, 0x12]   # Artefactos
    }

    # 2. Diseñar el mapa de píxeles (Tile 8x8)
    # Se aplica luz direccional (arriba-izquierda claro, abajo-derecha oscuro)
    tile_data = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 2, 2, 2, 0],
        [0, 0, 0, 0, 2, 2, 2, 0],
        [4, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 3, 3, 3, 0, 0],
        [0, 0, 3, 3, 3, 3, 5, 5],
        [0, 0, 0, 0, 0, 0, 5, 5],
    ])
    return tile_data, PALETTE

# Convierte el tile de números a colores
def converterRGB(data, palette: dict):
    # 3. Convertir el mapa de índices en una imagen RGB real
    rgb_image = np.zeros((8, 8, 3), dtype=np.uint8)
    for i in range(8):
        for j in range(8):
            rgb_image[i, j] = palette[data[i, j]]
    return rgb_image

# Retorna el tile deseado
def getTile(x: int):
    arrayTiles = [grassTile(), dirtTile(), waterTile(), SandTile(), WallStoneTile(), TreeTile(), CobbleTile(), LavaTile()]
    if x == 1234:
        return arrayTiles
    return arrayTiles[x]

def DEBUG():
    #print(f"¿Qué tile quieres visualizar?\n1. Pasto\n2. Tierra\n3. Agua\n4. Arena\n5. Muro de piedra\n6. Arbusto\n7. Adoquín\n8. Lava")
    #x = int(input("Introduce el número del tile: ")) - 1

    matriz = np.zeros((64,64,3), dtype=np.uint8)

    x = 0
    y = 0

    for i in range(8):
        for j in range(8):
            data, palette = getTile(i % 7)
            rgb_tile = converterRGB(data, palette)

            y = i * 8
            x = j * 8

            matriz[y:y+8, x:x+8] = rgb_tile

    # 4. Configurar y mostrar el gráfico con Matplotlib
    fig, ax = plt.subplots(figsize=(5, 5))

    # data, palette = getTile(x)
    ax.imshow(matriz, interpolation='nearest')

    # Configuración estética para desarrollo de videojuegos (Ver la cuadrícula de píxeles)
    #ax.set_xticks(np.arange(-0.5, 8, 1), minor=True)
    #ax.set_yticks(np.arange(-0.5, 8, 1), minor=True)
    #ax.grid(which='minor', color='black', linestyle='-', linewidth=0.5)
    #ax.tick_params(which='both', bottom=False, left=False, labelbottom=False, labelleft=False)
