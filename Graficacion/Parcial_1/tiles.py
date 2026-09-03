import string
from numpy import array
import matplotlib.pyplot as plt
import numpy as np

# Hexadecimas a decimal 3 bytes
def convertHexa(h: str):
    hexCode = h.lstrip('#')
    return [int(hexCode[0:2], 16), int(hexCode[2:4], 16), int(hexCode[4:6], 16)]

# Inicializar tiles
def tileInit():
    return np.zeros((8,8,3), dtype=np.uint8)

# Tile de piedra
# Color base #808080
# Sombra #404040
# Luz #C0C0C0
stone = tileInit()
stone [:,:,:] = [128,128,128]
stone [0:2,0:2] = [64,64,64]
stone [6:8,6:8] = [192,192,192]
stone [0,0] = [192,192,192]
stone [1,5] = [192,192,192]
stone [2,3] = [192,192,192]
stone [4,0] = [192,192,192]
stone [5,4] = [192,192,192]
stone [7,2] = [192,192,192]

# Tile de pasto
# Color base #2D692D
# Sombra #183C18
# Luz #4AA14A



def getTile(x: int):
    arrayTiles = [stone]
    return arrayTiles[x]

def test_tile():
    plt.imshow(stone, interpolation='nearest')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    #test_tile()
    print(convertHexa("#FFFFFF"))